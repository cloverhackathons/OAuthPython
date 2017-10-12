# OAuthPython

## Requirements

* Python 2.7
* pip
* [Sandbox Clover developer account](https://sandbox.dev.clover.com/developers)

## Set Up

[Create a Clover web app](https://docs.clover.com/build/web-apps/) from your [sandbox Developer Dashboard](https://sandbox.dev.clover.com/developers/).

* On the app's **Settings** page, note _App ID_ and _App Secret_. Set them as `CLIENT_ID` and `CLIENT_SECRET` in `config.py`.
* Under **Web Configuration**, set _Site URL_ and _CORS Domain_ to `http://localhost:5000`.

Run:
* `pip install -r requirements.txt`
* `python oauth.py`
