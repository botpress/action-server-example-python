from flask import Flask
import logging
import sys
from flask import jsonify
from flask import request
import requests
import os

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

app = Flask(__name__)

action_handlers = {""}

employees = [
    {
        "id": "mhopkins",
        "first_name": "Mike",
        "last_name": "Hopkins",
        "age": 34,
        "department": "IT",
    },
    {
        "id": "lsimpson",
        "first_name": "Lisa",
        "last_name": "Simpson",
        "age": 31,
        "department": "Sales",
    },
    {
        "id": "fhamilton",
        "first_name": "Frank",
        "last_name": "Hamilton",
        "age": 29,
        "department": "HR",
    },
]


@app.route("/", methods=["GET"])
def hello():
    print(os.environ['BOTPRESS_SERVER_URL'])
    return "Hello, World!"


@app.route("/actions/<bot_id>", methods=["GET"])
def actions(bot_id):
    logging.info(f"Requesting actions for bot {bot_id}")
    # Here, bot_it is unused, but you could use it to restrict the list of actions
    # allowed, based on the requesting bot id

    return jsonify(
        [
            {
                "name": "list_employees",
                "description": "Lists employees",
                "category": "HR",
                "parameters": [],
            },
            {
                "name": "get_employee",
                "description": "Get details of an employee",
                "category": "HR",
                "parameters": [
                    {
                        "name": "employee_id",
                        "type": "string",
                        "required": True,
                        "description": "The unique identifier for the employee to get",
                    }
                ],
            },
        ]
    )


@app.route("/action/run", methods=["POST"])
def run_action():
    request_body = request.json

    action_name = request_body["actionName"]
    bot_id = request_body["botId"]
    token = request_body["token"]
    action_args = request_body["actionArgs"]
    incoming_event = request_body["incomingEvent"]

    if action_name == "list_employees":
        incoming_event["state"]["temp"]["employees"] = [
            f'{e["first_name"]} {e["last_name"]}' for e in employees
        ]
    elif action_name == "get_employee":
        employee_id = action_args["employee_id"]
        incoming_event["state"]["temp"]["employee"] = next(
            e for e in employees if e["id"] == employee_id
        )
    else:
        raise RuntimeError(f"Could not find handler for action: {action_name}")

    return jsonify({"incomingEvent": incoming_event})
