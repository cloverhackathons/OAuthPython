# OAuthPython

## Requirements

* Python 2.7
* pip
* [Sandbox Clover developer account](https://sandbox.dev.clover.com/developers)

## Set Up

Follow these [instructions](https://docs.clover.com/build/web-apps/) for creating a Clover web app and installing it to your sandbox test merchant. When creating the app, select the [permissions](https://docs.clover.com/build/permissions/) you want the OAuth token to have.

* On the app's **Settings** page, note _App ID_ and _App Secret_. Set them as `CLIENT_ID` and `CLIENT_SECRET` in `config.py`.
* Under **Web Configuration**, set _Site URL_ and _CORS Domain_ to `http://localhost:3000`.

Run:
* `pip install -r requirements.txt`
* `python oauth.py`

In your web browser, visit [http://localhost:3000/](http://localhost:3000/).