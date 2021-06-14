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
    url =  "https://api.ciscospark.com/v1/webhooks"
    r = requests.get(url, headers=headers)
    print(r.content)
    items = json.loads(r.content)
    for item in items["items"]:
        webhook_ids.append(item["id"])
    return webhook_ids



def registerwebhook():
    url =  "https://api.ciscospark.com/v1/webhooks"
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print(r.content)


def deletewebhooks(webhook_ids):
    for id in webhook_ids:
        print("deleting webhook id : ",id)
        url =  "https://api.ciscospark.com/v1/webhooks/" + id
        r = requests.delete(url, headers=headers)
        print(r.content)




#Display webhook
webhook_ids = displaywebhook()

#Delete webhook
deletewebhooks(webhook_ids)

#Display webhook
webhook_ids = displaywebhook()

#Register webhook
registerwebhook()

#Display webhook
webhook_ids = displaywebhook()
print("\nCurrently alive webhooks are : ",webhook_ids)