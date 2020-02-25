from flask import Flask
import logging
import sys
from flask import jsonify

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

app = Flask(__name__)

action_handlers = {""}


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/actions/<bot_id>")
def actions(bot_id):
    logging.info(f"Requesting actions for bot {bot_id}")
    # Here, bot_it is unused, but you could use it to restrict the list of actions
    # allowed, based on the requesting bot id

    return jsonify(
        [
            {
                "name": "action1",
                "description:": "Some action from the Python server",
                "category": "category1",
                "params": [
                    {
                        "name": "param1",
                        "type": "string",
                        "required": True,
                        "default": "bonjour",
                        "description": "description of param1",
                    }
                ],
            }
        ]
    )
