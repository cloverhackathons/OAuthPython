# OAuthPython

## Requirements

* Python 3.7.3 (backwards compatible with 2.7)
* pip
* [Sandbox Clover developer account](https://sandbox.dev.clover.com/developers)

## Set Up

From the [Sandbox developer dashboard](https://sandbox.dev.clover.com/developers), create a Clover web app. When creating the app, select the [permissions](https://docs.clover.com/clover-platform/docs/permissions) that you want the OAuth token to have.

* On the app's **Settings** page, note _App ID_ and _App Secret_. Set them as `CLIENT_ID` and `CLIENT_SECRET` in `config.py`.
* Under **Web Configuration**, set _Site URL_ to `http://localhost:3000`.

Run:
* `pip install -r requirements.txt`
* `python oauth.py`

In your web browser, open [http://localhost:3000/](http://localhost:3000/).
