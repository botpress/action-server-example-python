from flask import Flask
import logging
import sys
from flask import jsonify
from flask import request

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

app = Flask(__name__)

action_handlers = {""}


@app.route("/", methods=['GET'])
def hello():
    return "Hello, World!"


@app.route("/actions/<bot_id>", methods=['GET'])
def actions(bot_id):
    logging.info(f"Requesting actions for bot {bot_id}")
    # Here, bot_it is unused, but you could use it to restrict the list of actions
    # allowed, based on the requesting bot id

    return jsonify(
        [
            {
                "name": "action1",
                "description": "Some action from the Python server",
                "category": "category1",
                "parameters": [
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


@app.route("/action/run", methods=['POST'])
def run_action():
    request_body = request.json

    print(request_body)

    action_name = request_body["actionName"]
    bot_id = request_body["botId"]
    token = request_body["token"]
    action_args = request_body["actionArgs"]
    incoming_event = request_body["incomingEvent"]

    return jsonify({"incomingEvent": incoming_event})
