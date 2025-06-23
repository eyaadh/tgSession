from livereload import Server
import os

server = Server()

# Watch templates and static folders
server.watch('templates/')
server.watch('static/')

# Serve aiohttp on another port
os.system("python app.py &")  # or however you run aiohttp

# Start livereload proxy on port 5500 (or whatever you prefer)
server.serve(root='.', port=5500)
