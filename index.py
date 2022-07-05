"""
NAME
    Index - This file includes functions that handle requests.

FILE
    index.py

FUNCTIONS
    index: Handles the requests for '/'.
    command_request_handler: Handles the requests for '/command'.

"""
import dotenv
import flask
from api.command_runner import run_command
from api.classes import exceptions

dotenv.load_dotenv('.env')
app = flask.Flask(__name__)


@app.route('/', methods=["GET"])
def index():
    """
    Handles the requests for '/'.

    :returns: HTML for the '/' page.
    """
    return (
        """
        <h1>GeoSMS 2.0</h1>
        <form action="/command" method="POST">
            <input type="text" name="sms" placeholder="Command">
            <input type="submit" value="Send">
        </form>
        """
    )


@app.route('/command', methods=["POST"])
def command_request_handler():
    """
    Handles the requests for '/command'.

    :returns: JSON response for the '/command' API route.
    """
    request = flask.request
    sms = request.form.get('sms')
    print(sms)
    response = None
    try:
        response = run_command(sms)
    except exceptions.UnknownCommandException:
        response = flask.jsonify({"error": "Unknown command"}), 404
    except exceptions.WrongArguments:
        response = flask.jsonify({"error": "Wrong arguments"}), 404
    return response


if __name__ == "__main__":
    app.run(debug=True)
