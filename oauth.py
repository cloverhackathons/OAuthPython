import flask
import requests
import config

ENV = config.SANDBOX
CLIENT_ID = config.CLIENT_ID
CLIENT_SECRET = config.CLIENT_SECRET

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def landing_page():
    """Depending on whether `code` is present, redirects to oauth_callback or to
    Clover merchant login."""

    code = flask.request.args.get('code', None)

    if not code:
        return flask.redirect("%s/oauth/authorize?client_id=%s" % (ENV, CLIENT_ID))
    else:
        return flask.redirect("/oauth_callback?code=%s" % code)


@app.route('/oauth_callback', methods=['GET'])
def oauth_callback():
    """
    Uses code param to 
    """
    code = flask.request.args.get('code', None)

    if not code:
        return flask.redirect("/")

    request = "%s/oauth/token?client_id=%s&client_secret=%s&code=%s" % (ENV, CLIENT_ID, CLIENT_SECRET, code)

    try:
        response = requests.get(request)
        access_token = response.json().get("access_token")
        print "Access token: ", access_token
    except Exception, e:
        print e

    if access_token:
        return access_token
    else:
        return "Could not retrieve access_token."


################################################################################

if __name__ == "__main__":

    app.run(debug=True)
