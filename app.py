import os
from aiohttp import web
import aiohttp_jinja2
import jinja2
from telethon.errors import SessionPasswordNeededError, AuthRestartError

from telegram_client import create_client

routes = web.RouteTableDef()

# In-memory store of phone_code_hashes
phone_code_hash_map = {}


@routes.get("/")
@aiohttp_jinja2.template("index.html")
async def index(request):
    return {}


@routes.post("/send-code")
@aiohttp_jinja2.template("code.html")
async def send_code(request):
    data = await request.post()
    phone = data.get("phone")
    client = create_client(phone)
    await client.connect()

    try:
        if not await client.is_user_authorized():
            sent = await client.send_code_request(phone)
            phone_code_hash_map[phone] = sent.phone_code_hash
            return {"phone": phone, "message": "Code sent. Please check Telegram."}
        else:
            return web.HTTPFound(f"/profile?phone=+{phone.lstrip('+')}")

    except AuthRestartError:
        path = f"sessions/+{phone.lstrip('+')}.session"
        if os.path.exists(path):
            os.remove(path)

        return aiohttp_jinja2.render_template("index.html", request, {
            "error": "Telegram canceled the login attempt. Please try again."
        })

    except Exception as e:
        print("Error during send_code:", e)
        return aiohttp_jinja2.render_template("index.html", request, {
            "error": str(e)
        })



@routes.post("/verify-code")
async def verify_code(request):
    data = await request.post()
    phone = data.get("phone")
    code = data.get("code")
    phone_code_hash = phone_code_hash_map.get(phone)

    if not phone_code_hash:
        return web.Response(text="Missing phone_code_hash. Please restart login.")

    client = create_client(phone)
    await client.connect()

    try:
        await client.sign_in(phone=phone.strip(), code=code, phone_code_hash=phone_code_hash)
        await client.disconnect()  # ✅ Ensures session is saved
        return web.HTTPFound(f"/profile?phone={phone}")
    except SessionPasswordNeededError:
        return aiohttp_jinja2.render_template("password.html", request, {"phone": phone})
    except Exception as e:
        return web.Response(text=f"Login failed: {e}")

@routes.post("/verify-password")
async def verify_password(request):
    data = await request.post()
    phone = data.get("phone")
    password = data.get("password")

    client = create_client(phone)
    await client.connect()

    try:
        await client.sign_in(password=password)
        await client.disconnect()
        return web.HTTPFound(f"/profile?phone=+{phone.lstrip('+')}")
    except Exception as e:
        return aiohttp_jinja2.render_template("password.html", request, {
            "phone": phone,
            "error": str(e)
        })


@routes.get("/profile")
@aiohttp_jinja2.template("profile.html")
async def profile(request):
    phone = request.query.get("phone")
    client = create_client(phone)
    await client.connect()

    if not await client.is_user_authorized():
        return web.Response(text="Unauthorized", status=401)

    me = await client.get_me()
    return {
        "id": me.id,
        "first_name": me.first_name,
        "username": me.username,
        "phone": phone
    }


def create_app():
    app = web.Application()

    base_dir = os.path.dirname(os.path.abspath(__file__))

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(os.path.join(base_dir, "templates")))
    app.router.add_static('/static', path=os.path.join(base_dir, 'static'), name='static')
    app.add_routes(routes)
    return app


if __name__ == "__main__":
    web.run_app(create_app(), port=8080)
