# this is the webhook for a TestBot

#import os
#import json
#import requests
from flask import Flask, request, make_response, jsonify
#from keys import nutrionix_app_id, nutrionix_app_key
#import pygal
#from pygal.style import DefaultStyle
#import cairosvg
#import pymongo
#from pymongo import MongoClient
import ast


myinput1 = {
  "id": "d75f7d46-155f-4a2f-add5-75b5fc4f2596",
  "timestamp": "2018-02-22T09:01:10.433Z",
  "lang": "en",
  "result": {
    "source": "agent",
    "resolvedQuery": "Dan 50 UAH Tim",
    "action": "testbot",
    "actionIncomplete": False,
    "parameters": {
      "user1": "Dan",
      "sum": {
        "amount": 200,
        "currency": "UAH"
      },
      "sum_basic_currency": "",
      "user2": ""
    },
    "contexts": [],
    "metadata": {
      "intentId": "83b7244a-7595-4f67-8b72-85199ded352a",
      "webhookUsed": "false",
      "webhookForSlotFillingUsed": "false",
      "intentName": "add_payment"
    },
    "fulfillment": {
      "speech": "Dan paid 50 USD to Tim",
      "messages": [
        {
          "type": 0,
          "speech": "Dan paid 50 USD to Tim"
        }
      ]
    },
    "score": 0.9300000071525574
  },
  "status": {
    "code": 200,
    "errorType": "success",
    "webhookTimedOut": False
  },
  "sessionId": "ad0d56ff-2dc1-4720-8516-067ce9c1cd55"
}

myinput2 = {
  "id": "5edfed55-16f3-44de-bf21-31ef27c0f2c0",
  "timestamp": "2018-02-23T08:44:50.44Z",
  "lang": "en",
  "result": {
    "source": "agent",
    "resolvedQuery": "balance Victor",
    "action": "balance",
    "actionIncomplete": False,
    "parameters": {
      "user": ""
    },
    "contexts": [],
    "metadata": {
      "intentId": "2261701a-bce0-44b1-b4fd-806037e04de6",
      "webhookUsed": "false",
      "webhookForSlotFillingUsed": "false",
      "intentName": "balance"
    },
    "fulfillment": {
      "speech": "Showing current balance for user Victor",
      "messages": [
        {
          "type": 0,
          "speech": "Showing current balance for user Victor"
        }
      ]
    },
    "score": 0.9200000166893005
  },
  "status": {
    "code": 200,
    "errorType": "success",
    "webhookTimedOut": False
  },
  "sessionId": "ad0d56ff-2dc1-4720-8516-067ce9c1cd55"
}

def add_payment(req):
    # Get our log (txt file will be substituted with Mongo DB)
    with open("log.txt", "r+") as logfromtxt:
        log = ast.literal_eval(logfromtxt.read())

    BASIC_CURRENCY = 'UAH'
    # Exchange rates to be substituted with calls to some API
    usd_uah = 26.9
    eur_uah = 33.1

    if 'originalRequest' in req:
        first_name = req.get('originalRequest').get('data').get('message').get('from').get('first_name')
        last_name = req.get('originalRequest').get('data').get('message').get('from').get('last_name')
        uid = req.get('originalRequest').get('data').get('message').get('from').get('id')

    user1 = req.get('result').get('parameters').get('user1') # USER1 is payer, required
    user2 = req.get('result').get('parameters').get('user2') # USER2 is receiver in direct transactions, otherwise USER1 pays for all (including himself), optional
    sum = req.get('result').get('parameters').get('sum') # {"amount": 100, "currency": "USD"}
    sum_basic_currency = req.get('result').get('parameters').get('sum_basic_currency')
    timestamp = req.get('timestamp')

    print('user1 (payer): ' + user1)
    print('user2 (receiver): ' + user2)
    print('sum: ' + str(sum))
    print('sum_basic_currency: ' + str(sum_basic_currency))

    # If currency != basic (for eg., UAH), convert to basic currency
    if sum == "":
        amount = float(sum_basic_currency)
    else:
        if sum["currency"] == BASIC_CURRENCY:
            amount = sum["amount"]
        elif sum["currency"] == "USD":
            amount = sum["amount"] * usd_uah
        elif sum["currency"] == "EUR":
            amount = sum["amount"] * eur_uah

    print('sum_converted: ' + str(amount))

    # In our 1st model we'll have 2 already registered users, Tim and Dan
    if user2 == "": # means that user1 paid for all = he gets his sum - sum/users_quantity, for eg. if 2 users and user1 paid $50, his balance will be +25$
        who_received = "all"
        #every_user_gets = amount / len(log["users"])
        payer_gets = amount - amount / len(log["users"])
        recipient_gets = amount / len(log["users"]) * -1
    else:
        who_received = user2
        payer_gets = amount
        recipient_gets = amount * -1

    print('payer_gets: ' + str(payer_gets))
    print('recipient_gets: ' + str(recipient_gets))
    #print("log: " + str(log))

    nexttransaction = {
                "timestamp": timestamp,
                "transaction_number": len(log["transactions"]) + 1,
                "who_paid": user1,
                "who_received": who_received,
                "amount": amount,
                "transaction_balance": {},
                "total_balance": {}
    }

    for user in log["users"]:
        if user != user1: # calculate what recipient(s) gets/get
            if user2 == "": # "pay for all", each recepient gets amount / usersN
                nexttransaction["transaction_balance"].update({user: recipient_gets})
                user_balance_was = log["transactions"][len(log["transactions"])-1]["total_balance"][user]
                user_balance_now = float("{0:.2f}".format(user_balance_was + recipient_gets))
            else:
                if user == user2: # direct transaction between user1 and user2
                    nexttransaction["transaction_balance"].update({user: recipient_gets})
                    user_balance_was = log["transactions"][len(log["transactions"]) - 1]["total_balance"][user]
                    user_balance_now = float("{0:.2f}".format(user_balance_was + recipient_gets))
                else: # direct transaction between user1 and user2, other users get 0
                    nexttransaction["transaction_balance"].update({user: 0})
                    user_balance_was = log["transactions"][len(log["transactions"]) - 1]["total_balance"][user]
                    user_balance_now = float("{0:.2f}".format(user_balance_was + 0))
        else: # calculate what payer looses
            nexttransaction["transaction_balance"].update({user: payer_gets})
            user_balance_was = log["transactions"][len(log["transactions"])-1]["total_balance"][user]
            user_balance_now = float("{0:.2f}".format(user_balance_was + payer_gets))
        print("Balance of user {} was {}, became {}".format(user, user_balance_was, user_balance_now))
        nexttransaction["total_balance"][user] = user_balance_now

    #print("nexttransaction: " + str(nexttransaction))

    log["transactions"].append(nexttransaction)
    #print("New log: " + str(log))

    with open("log.txt", "w") as logdump:
        logdump.write(str(log))

    print(str(log["transactions"][len(log["transactions"])-1]["total_balance"]))
    print(" ")
    return True

def balance(req):
    # Get our log (txt file will be substituted with Mongo DB)
    with open("log.txt", "r") as logfromtxt:
        log = ast.literal_eval(logfromtxt.read())

    # Check if balance should be displayed for specific user
    user = req.get('result').get('parameters').get('user')
    print('user: ' + user)

    # Get last transaction
    last_transaction = log["transactions"][len(log["transactions"])-1]
    print('last_transaction: ' + str(last_transaction))

    balance = ""
    if user == "":
        balance = "Current balance:"
        for everyuser, everyuser_balance in last_transaction["total_balance"].items():
            balance += "\n{}: {}".format(everyuser, everyuser_balance)
    else:
        balance = "Current balance for user {}: {}".format(user, last_transaction["total_balance"][user])

    return balance

#add_payment(myinput1)

print(balance(myinput2))