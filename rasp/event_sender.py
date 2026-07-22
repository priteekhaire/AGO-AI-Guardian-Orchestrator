import json
import boto3
from config import EVENT_BUS, EVENT_SOURCE, DETAIL_TYPE

client = boto3.client("events")


def send_event(attack, payload):
    response = client.put_events(
        Entries=[
            {
                "Source": EVENT_SOURCE,
                "DetailType": DETAIL_TYPE,
                "EventBusName": EVENT_BUS,
                "Detail": json.dumps({
                    "severity": "HIGH",
                    "attack": attack,
                    "instance": "AGO-Demo-Server",
                    "status": "OPEN",
                    "payload": payload
                })
            }
        ]
    )

    return response
