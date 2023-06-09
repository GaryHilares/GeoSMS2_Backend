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
from api.control import exceptions, cooldown

dotenv.load_dotenv(".env")
app = flask.Flask(__name__, template_folder="website")


@app.route("/", methods=["GET"])
def index():
    """
    Handles the requests for '/'.

    :returns: HTML for the '/' page.
    """
    return flask.render_template("homepage.html")


@app.route("/command", methods=["POST"])
def command_request_handler():
    """
    Handles the requests for '/command'.

    :returns: JSON response for the '/command' API route.
    """
    request = flask.request
    mobile_number = request.form.get("num")
    sms = request.form.get("sms")
    response = None
    try:
        if not cooldown.is_ready(mobile_number):
            return flask.jsonify({"error": "El cliente está en tiempo fuera."}), 403
        response = run_command(sms)
    except exceptions.UnknownCommandException:
        response = flask.jsonify({"error": "Comando desconocido."}), 404
    except exceptions.WrongArgumentsException:
        response = flask.jsonify({"error": "Argumentos incorrectos."}), 404
    except TypeError:
        response = flask.jsonify({"error": "Argumentos del tipo incorrecto."}), 404
    except SyntaxError:
        response = flask.jsonify({"error": "Argumentos del tipo incorrecto."}), 404
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
