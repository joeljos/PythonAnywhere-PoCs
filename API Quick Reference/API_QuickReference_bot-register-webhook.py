"""
Copyright (c) 2021 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

import requests
import json
import cred

payload = {
    "name": "Joel's API Quick Reference bot's Webhook Firehose",
    "targetUrl": "http://joeljos.pythonanywhere.com/api_quick_reference",
    "resource": "all",
    "event": "all"
}

headers = {
    "Content-type": "application/json; charset=utf-8",
    "Authorization": "Bearer " + cred.bearer
}


def displaywebhook():
    webhook_ids = []
    url = "https://api.ciscospark.com/v1/webhooks"
    r = requests.get(url, headers=headers)
    print(r.content)
    items = json.loads(r.content)
    for item in items["items"]:
        webhook_ids.append(item["id"])
    return webhook_ids


def registerwebhook():
    url = "https://api.ciscospark.com/v1/webhooks"
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(r.content)


def deletewebhooks(webhook_ids):
    for id in webhook_ids:
        print("deleting webhook id : ", id)
        url = "https://api.ciscospark.com/v1/webhooks/" + id
        r = requests.delete(url, headers=headers)
        print(r.content)


# Display webhook
webhook_ids = displaywebhook()

# Delete webhook
deletewebhooks(webhook_ids)

# Display webhook
displaywebhook()

# Register webhook
registerwebhook()

# Display webhook
webhook_ids = displaywebhook()
print("\nCurrently alive webhooks are : ", webhook_ids)
