# Telegram Session Hijacking Demo (Educational)

This project is a demonstration of a Telegram session hijacking technique, designed to illustrate the concepts of phishing, overcoming multi-factor authentication (MFA), and session hijacking. It's built as a part of a [blog post](http://blog.eyaadh.net/2025/06/hey-everyone-long-time-no-see-right-so.html) to educate users on how such attacks are carried out and why even MFA-enabled accounts can be vulnerable to social engineering.

**Disclaimer:** This project is for **educational and research purposes only**. Do not use it for any malicious or illegal activities. Unauthorized access to computer systems or accounts is illegal and unethical.

## Features & Technologies

This demo simulates a simplified Telegram Web login flow to capture user sessions. It leverages the following Python libraries:

* **Telethon**: An asynchronous MTProto client that allows direct interaction with Telegram's API, mimicking a real Telegram client to handle authentication and session management.
* **Aiohttp**: An asynchronous HTTP client/server framework used to serve the fake Telegram Web login pages and handle user input.
* **Livereload**: A development utility that automatically reloads web pages in the browser when changes are made to code or templates, greatly enhancing the development experience.

## Project Structure

```

.
├── sessions/
│   └── (session files will be stored here)
├── static/
│   └── images/
│       ├── monkey-blink.png
│       ├── monkey-peeking.png
│       ├── monkey-right.png
│       ├── monkey-front.png
│       ├── monkey-left.png
│       └── monkey-covering.png
├── templates/
│   ├── profile.html
│   ├── index.html
│   ├── code.html
│   ├── password.html
├── app.py
├── telegram_client.py
└── main.py

````

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.8+
* `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/eyaadh/tgSession.git](https://github.com/eyaadh/tgSession.git)
    cd tgSession
    ```

2.  **Install dependencies:**
    ```bash
    pip3 install -r requirements.txt
    ```

### Configuration

Create a `.env` file in the root directory of the project and add your Telegram API credentials:

````
API_ID=123456
API_HASH=64e5f247fbd71144c718363803XXXXXX
````
* **How to get `API_ID` and `API_HASH`:**
    1.  Go to [my.telegram.org](https://my.telegram.org/).
    2.  Log in with your Telegram account.
    3.  Click on "API development tools".
    4.  Create a new application. The `API_ID` and `API_HASH` will be displayed there.

### How to Run

You have two options to run the demo:

1.  **With Live Reload (Recommended for Development):**
    This will run both the `aiohttp` web server and the `livereload` proxy for automatic browser refreshes.
    ```bash
    python main.py
    ```
    Access the application in your browser at `http://localhost:5500`.

2.  **Run Web Application Only:**
    This will run just the `aiohttp` web server. You'll need to manually refresh your browser to see changes.
    ```bash
    python app.py
    ```
    Access the application in your browser at `http://localhost:8080`.

## Contributing

Feel free to explore, learn from, and contribute to this educational project. Pull requests are welcome!