import flask
import requests
import config

CLIENT_ID = config.CLIENT_ID
CLIENT_SECRET = config.CLIENT_SECRET
ENV = "https://sandbox.dev.clover.com"

if not CLIENT_ID or not CLIENT_SECRET:
    raise ValueError("Set your CLIENT_ID and CLIENT_SECRET in config.py.")

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def landing_page():
    """Depending on whether `code` parameter is present, redirects to
    oauth_callback or to Clover merchant login."""

    # A request from an authorized merchant includes a code in its query string.
    code = flask.request.args.get('code')

    # If the request doesn't include a code, redirect the merchant to Clover's
    # authorize endpoint.
    if not code:
        return flask.redirect("%s/oauth/authorize?client_id=%s" % (ENV, CLIENT_ID))

    # If the request does include a code, redirect to this app's oauth_callback
    # in order to request an access_token.
    else:
        return flask.redirect("/oauth_callback?code=%s" % code)


@app.route('/oauth_callback', methods=['GET'])
def oauth_callback():
    """Uses `code` with CLIENT_ID and CLIENT_SECRET to request access_token."""

    code = flask.request.args.get('code')

    # The merchant shouldn't reach this endpoint without a code, but just in case:
    if not code:
        return flask.redirect("/")

    # Use the code with your app ID and app secret to request an access_token.
    request = "%s/oauth/token?client_id=%s&client_secret=%s&code=%s" % (ENV, CLIENT_ID, CLIENT_SECRET, code)

    try:
        response = requests.get(request)
        access_token = response.json().get("access_token")
        print "Access token: ", access_token
    except Exception as e:
        print e

    if access_token:
        return "Access token: "+access_token
    else:
        return "Could not retrieve access_token."


################################################################################

if __name__ == "__main__":

    app.run(port=3000)
