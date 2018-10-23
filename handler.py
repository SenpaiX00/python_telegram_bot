#Handler is the Python code with functions that must be coupled with the YAML (.yml) file
import json
import os
import sys
import boto3
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendored"))

import requests

TOKEN = os.environ['TELEGRAM_TOKEN']
URL = "https://api.telegram.org/bot{}".format(TOKEN)

#Test to ensure the AWS API Gateway and webhooks are working into Telegram API.
def bot(event, context):
    print(URL)
    try:
        data = json.loads(event["body"])
        message = str(data["message"]["text"])
        chat_id = data["message"]["chat"]["id"]
        first_name = data["message"]["chat"]["first_name"]

        #response = "Please /start, {}".format(first_name)

        #if "start" or "Start" in message:
         #   response = "Hello {}".format(first_name)     
        if "hi" in message:
            response = "sup? {}".format(first_name)
            MonthlyBudget(data)
        else:
            "How can I help {}".format(first_name)

        data = {"text": response.encode("utf8"), "chat_id": chat_id}
        url = URL + "/sendMessage"
        requests.post(url, data)

    except Exception as e:
        print(e)

    return {"statusCode": 200}

#IN DEVELOPMENT
def MonthlyBudget(data):
    try:
        message = str(data["message"]["text"])
        chat_id = data["message"]["chat"]["id"]
        first_name = data["message"]["chat"]["first_name"]
        response = int(message)
        data = {"text": response.encode("utf8"), "chat_id": chat_id}
        url = URL + "/sendMessage"
        requests.post(url, data)
    
    except Exception as e:
        return e

#IN DEVELOPMENT
#def ChangeBudgetForThisMonth:

#def NewSpend:

#def RemoveSpend:

#def RemainingBudgetCalculation:



