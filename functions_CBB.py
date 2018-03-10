# this is the webhook for a TestBot

from flask import Flask, request, make_response, jsonify
import ast
import datetime
import random
from pymongo import MongoClient

BASIC_CURRENCY = 'UAH'

# Exchange rates to be substituted with calls to some API
usd_uah = 26.9
eur_uah = 33.1

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
        "amount": 500,
        "currency": "UAH"
      },
      "sum_basic_currency": "",
      "user2": "Tim"
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
    "sessionId": "ad0d56ff-2dc1-4720-8516-067ce9c1cd55",
    'originalRequest': {
        'data': {
            'update_id': 686221086,
            'message': {
                'message_id': 499,
                'text': '000000',
                'from': {
                    'id': 178180819,
                    'last_name': 'D.',
                    'is_bot': False,
                    'language_code': 'ru-RU',
                    'first_name': 'Iurii'},
                'chat': {
                    'id': 178180819,
                    'last_name': 'D.',
                    'type': 'private',
                    'first_name': 'Iurii'
                },
                'date': 1519572336
            }
        },
        'source': 'telegram'
    }
}

myinput2 = {
  'originalRequest': {
    'source': 'telegram',
    'data': {
      'message': {
        'date': 1520676018,
        'text': 'delete payment 5',
        'message_id': 1732,
        'chat': {
          'id': 178180819,
          'last_name': 'D.',
          'type': 'private',
          'first_name': 'Iurii'
        },
        'from': {
          'id': 178180819,
          'language_code': 'ru-RU',
          'last_name': 'D.',
          'first_name': 'Iurii',
          'is_bot': False
        }
      },
      'update_id': 686221788
    }
  },
  'timestamp': '2018-03-10T10:00:19.058Z',
  'lang': 'en',
  'status': {
    'code': 200,
    'errorType': 'success',
    'webhookTimedOut': False
  },
  'id': 'd9b23db8-36be-4113-a0b9-041004afca79',
  'sessionId': '0d600684-016b-4c3c-9b7a-f27151c366c4',
  'result': {
    'metadata': {
      'intentId': '347ac348-c667-45be-8dd7-34693f6ce66e',
      'webhookForSlotFillingUsed': 'false',
      'webhookUsed': 'true',
      'intentName': 'delete_payment'
    },
    'speech': '',
    'fulfillment': {
      'speech': '',
      'messages': [
        {
          'speech': '', 'type': 0
        }
      ]
    },
    'parameters': {
      'payment2delete': '5'
    },
    'score': 1.0,
    'resolvedQuery': 'delete payment 5',
    'contexts': [
      {
        'parameters': {
          'payment2delete.original': '5',
          'telegram_chat_id': '178180819',
          'payment2delete': '5'
        },
        'lifespan': 4,
        'name': 'generic'
      }
    ],
    'source': 'agent',
    'actionIncomplete': False,
    'action': 'commonbalancebot-delete_payment'
  }
}

myinput3 = {
  'originalRequest': {
    'source': 'telegram',
    'data': {
      'callback_query': {
        'from': {
          'last_name': 'D.',
          'first_name': 'Iurii',
          'language_code': 'ru-RU',
          'is_bot': False,
          'id': 178180819
        },
        'message': {
          'date': 1519933138,
          'entities': [
            {
              'type': 'bold',
              'length': 10,
              'offset': 0
            }
          ],
          'from': {
            'username': 'YetAnotherTestChatBot',
            'id': 452144171,
            'is_bot': True,
            'first_name': 'TestTestTestBot'
          },
          'text': "Hi, Iurii!\nI'm a CommonBalanceBot - here to help you with tracking transactions with your friends.\nTo start you need a log. Should I create one for you?",
          'message_id': 589,
          'chat': {
            'id': 178180819,
            'last_name': 'D.',
            'type': 'private',
            'first_name': 'Iurii'
          }
        },
        'id': '765280791023790620',
        'data': 'Create log',
        'chat_instance': '-8728995663043026465'
      },
      'update_id': 686221134
    }
  },
  'timestamp': '2018-03-01T19:39:01.592Z',
  'lang': 'en',
  'sessionId': '82821da0-d1ef-4caf-8db4-f3602b989e8d',
  'status': {
    'errorType': 'success',
    'code': 200,
    'webhookTimedOut': False
  },
  'id': '91a324b3-403a-40a0-9aa4-b4a4c1d15de9',
  'result': {
    'actionIncomplete': False,
    'source': 'agent',
    'speech': '',
    'action': 'commonbalancebot-create_log',
    'resolvedQuery': 'Create log',
    'fulfillment': {
      'messages': [
        {
          'speech': '', 'type': 0
        }
      ],
      'speech': ''
    },
    'metadata': {
      'webhookUsed': 'true',
      'webhookForSlotFillingUsed': 'false',
      'intentId': 'ec5eb6ae-7785-44fb-9165-67d87d1c509c',
      'intentName': 'create_log'
    },
    'parameters': {},
    'score': 1.0,
    'contexts': [
      {
        'name': 'cookie',
        'lifespan': 19,
        'parameters': {
          'welcomed.original': '',
          'welcomed': 'yes'
        }
      }
    ]
  }
}

myinput4 = {'transactions': [{'transaction_balance': {}, 'total_balance': {'Ann': 0, 'Tim': 0, 'Dan': 0}, 'who_paid': '', 'who_received': 'all', 'amount': 0, 'timestamp': 'start', 'transaction_number': 0}, {'transaction_balance': {'Ann': -179.33333333333334, 'Tim': 358.66666666666663, 'Dan': -179.33333333333334}, 'total_balance': {'Ann': -179.33, 'Tim': 358.67, 'Dan': -179.33}, 'who_paid': 'Tim', 'who_received': 'all', 'amount': 538.0, 'timestamp': '2018-02-23T10:24:59.404Z', 'transaction_number': 1}, {'transaction_balance': {'Ann': -166.66666666666666, 'Tim': -166.66666666666666, 'Dan': 333.33333333333337}, 'total_balance': {'Ann': -346.0, 'Tim': 192.0, 'Dan': 154.0}, 'who_paid': 'Dan', 'who_received': 'all', 'amount': 500.0, 'timestamp': '2018-02-23T10:25:13.811Z', 'transaction_number': 2}, {'transaction_balance': {'Ann': 200.0, 'Tim': -200.0, 'Dan': 0}, 'total_balance': {'Ann': -146.0, 'Tim': -8.0, 'Dan': 154.0}, 'who_paid': 'Ann', 'who_received': 'Tim', 'amount': 200.0, 'timestamp': '2018-02-23T10:25:33.219Z', 'transaction_number': 3}, {'transaction_balance': {'Ann': 538.0, 'Tim': -269.0, 'Dan': -269.0}, 'total_balance': {'Ann': 392.0, 'Tim': -277.0, 'Dan': -115.0}, 'who_paid': 'Ann', 'who_received': 'all', 'amount': 807.0, 'timestamp': '2018-02-23T10:25:50.724Z', 'transaction_number': 4}, {'transaction_balance': {'Ann': -277.0, 'Tim': 277.0, 'Dan': 0}, 'total_balance': {'Ann': 115.0, 'Tim': 0.0, 'Dan': -115.0}, 'who_paid': 'Tim', 'who_received': 'Ann', 'amount': 277.0, 'timestamp': '2018-02-23T20:07:13.708Z', 'transaction_number': 5}, {'total_balance': {'Ann': 0.0, 'Tim': 0.0, 'Dan': 0.0}, 'transaction_balance': {'Ann': -115.0, 'Tim': 0, 'Dan': 115.0}, 'amount': 115.0, 'who_paid': 'Dan', 'who_received': 'Ann', 'timestamp': '2018-02-23T20:07:24.209Z', 'transaction_number': 6}], 'users': ['Tim', 'Dan', 'Ann']}

def req_inside(req):
    '''
        Function helps to get user id, user 1st name or other parameters from JSON got via webhook
        Path depends on wheather user "tapped" an answer or entered it from keyboard
        Returns correct path
    '''
    if "message" in req["originalRequest"]["data"]:
        req_digg = req["originalRequest"]["data"]["message"]["from"]
    else:
        req_digg = req["originalRequest"]["data"]["callback_query"]["from"]
    return req_digg

def commonbalancebot_speech2(ourspeech, oursource, outputcontext):
    '''
        Composes response for different platforms for CommonBalanceBot
    '''
    res = {
        'speech': ourspeech,
        'displayText': ourspeech,
        'source': oursource,

        'messages': [
            {
                'type': 0,
                'platform': 'telegram',
                'speech': ourspeech
            },
            {
                'type': 0,
                'speech': ourspeech
            }
        ],
        'contextOut': outputcontext
    }

    return res

def commonbalancebot_speech(ourspeech, oursource, outputcontext):
    '''
        Composes response for different platforms for CommonBalanceBot
    '''
    #print("ourspeech: {}".format(ourspeech))
    basic_txt_message = ourspeech["speech"]
    if "rich_messages" in ourspeech:
        rich_messages = ourspeech["rich_messages"]
    else:
        rich_messages = []

    res = {
        'speech': basic_txt_message,
        'displayText': basic_txt_message,
        'source': oursource,

        'messages': [message for message in rich_messages],
        'contextOut': outputcontext
    }
    return res

def create_log(req):
    '''
        Function gets JSON from webhook (user ID and 1st name are taken from there), and
        1. Creates a collection in DB "CBB" under randomly generated name in format
        <greek letter>-<animal>-<today's date>, and inserts 2 documents into this collection:
        1.1. Document with log info and
        1.2. Document with log creation data - see below
        2. Checks collectin "clients" in DB "CBB" for a document with such user ID and either creates such or
        appends new log_name

    '''
    # Response to be returned
    response = {"status": None, "payload": None}

    # 1. Get user ID (will be creator_id) and user 1st name from JSON
    creator_id = req_inside(req)["id"]
    user_first_name = req_inside(req)["first_name"]

    # 2. Generate collection name
    first_part = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "kappa", "omicron", "sigma", "tau", "upsilon", "phi", "chi", "psi", "omega"]
    second_part = ["cat", "dog", "frog", "chicken", "rabbit", "wolf", "bear", "bat", "beaver", "bison", "pig", "horse", "cow", "monkey", "fox", "mouse", "goat", "lion", "puma", "tiger", "bat", "zebra", "seal"]
    todays_date = datetime.datetime.now().strftime("%d%m%y")
    collection_name = "{}-{}-{}".format(random.choice(first_part), random.choice(second_part), todays_date)

    # 3. Create collection
    try:
        client = MongoClient()
        db = client.CBB
        collection = db[collection_name]

        # 4. Prepare documents
        log_info = {
            'log': 'info',
            'log_status': 'active',
            'creator_id': creator_id,
            'log_name': collection_name,
            'active_users': [user_first_name],
            'initial_balance': {user_first_name: 0}
        }

        create_log_action = {
            # '_id': 0, = creation date, used for sorting
            'creator_id': creator_id,
            'action_type': 'create_log'
        }

        # 5. Insert documents to collection
        log_info_id = collection.insert_one(log_info).inserted_id
        create_log_action_id = collection.insert_one(create_log_action).inserted_id

        # 6. Check if such user is already in our "clients" collection
        clients = db["clients"]
        ourclient = clients.find_one({"user_id": creator_id})
        if ourclient: # existing user
            logs = ourclient["logs"]
            logs.append(collection_name)
            clients.update_one({"user_id": creator_id}, {'$set': {"logs": logs}})
            clients.update_one({"user_id": creator_id}, {'$set': {"log_last_used": collection_name}})
        else: # new user
            newclient = {
                "channel": "telegram",
                "user_id": creator_id,
                "first_name": user_first_name,
                "logs": [
                    collection_name
                ],
                "log_last_used": collection_name
            }
            client_insert_id = clients.insert_one(newclient).inserted_id

    except Exception as error:
        response = {"status": "error", "payload": "create_log(): {}".format(error)}
        return response

    # 7. Final Ok response
    payload = {
        "speech": "Log \"{}\" successfully created, but at the moment contains only 1 user - you ({}) ;) \nTo continue please add users".format(collection_name, user_first_name),
        "rich_messages": [
            {
                "platform": "telegram",
                "type": 1,
                "title": "Log \"{}\" successfully created!".format(collection_name),
                "subtitle": "But at the moment it contains only 1 user - you ({}) ;) \nTo continue please add users :)".format(user_first_name),
                "buttons": [
                    {
                        "postback": "Add new user",
                        "text": "Add user"
                    },
                    {
                        "postback": "Help",
                        "text": "Help"
                    }
                ]
            }
        ]
    }
    response = {"status": "ok", "payload": payload}
    return response

def delete_log(req):
    '''
        Function 'soft-deletes' log with mutual transactions:
        1) updates info in the 1st document in collection with log info ("log_status": "active" >> "inactive")
        2) inserts a document with log deletion data - see below
        3) removes a log from the list of logs in collection "clients" >> document for user_id >> field "logs"
    '''
    # Response to be returned
    response = {"status": None, "payload": None}

    # 1. Get user id and log name from req
    creator_id = req_inside(req)["id"]
    collection_name = req["result"]["resolvedQuery"]

    # 2. Check if collection exists
    try:
        client = MongoClient()
        db = client.CBB
        # If such collection exists in general
        if collection_name in db.collection_names():
            log_info = db[collection_name].find_one({"log": "info"})
            print("***********************")
            print("log_info: {}".format(log_info))

            # If such collection exists for creator_id
            if log_info["creator_id"] != creator_id:
                response = {"status": "error", "payload": {"speech": "You don't have a log named '{}'".format(collection_name)}}
                return response

            # If it exists and hasn't been deleted (inactivated)
            if log_info["log_status"] == "inactive":
                print()
                print("log_info[\"log_status\"]: {}".format(log_info["log_status"]))
                response = {"status": "error", "payload": {"speech": "Log already deleted"}}
                return response

            # 3. Delete (inactivate) it
            db[collection_name].update_one({"log": "info"}, {'$set': {"log_status": "inactive"}})

            # 4. Update data in collection "clients" >> document for this client ID
            client_info = db.clients.find_one({"user_id": creator_id})
            # All client's logs
            client_logs = client_info["logs"]
            # Log last used
            log_last_used = client_info["log_last_used"]
            if collection_name in client_logs:
                client_logs.remove(collection_name)
                # Update log_last_used field
                if len(client_logs) == 0:
                    log_last_used = ""
                else:
                    # for now; later maybe log_last_used may be defined as the log with the most recent document
                    log_last_used = client_logs[len(client_logs)-1]

                db.clients.update_one({"user_id": creator_id}, {'$set': {"logs": client_logs}})
                db.clients.update_one({"user_id": creator_id}, {'$set': {"log_last_used": log_last_used}})
        else:
            response = {"status": "error", "payload": {"speech": "Failed to delete log \"{}\". Log not found".format(collection_name)}}
            return response
    except Exception as error:
        response = {"status": "error", "payload": {"speech": "delete_log()-1: {}".format(error)}}
        return response

    # 4. Prepare document to be inserted
    delete_log_action = {
        # '_id': 0, = creation date, used for sorting
        'creator_id': creator_id,
        'action_type': 'delete_log'
    }

    # 5. Insert document into DB
    try:
        delete_log_action_id =  db[collection_name].insert_one(delete_log_action).inserted_id
    except Exception as error:
        response = {"status": "error", "payload": {"speech": "delete_log()-2: {}".format(error)}}
        return response

    # 6. Prepare final Ok response
    if len(client_logs) == 0:
        payload = {
            "speech": "Log {} was deleted. You have no logs left.\nTo continue please create a log".format(collection_name),
            "rich_messages": [
                {
                    "platform": "telegram",
                    "type": 1,
                    "title": "Log {} was deleted".format(collection_name),
                    "subtitle": "You have no logs left. To continue please create a log",
                    "buttons": [
                        {
                            "postback": "Create log",
                            "text": "Create log"
                        },
                        {
                            "postback": "Help",
                            "text": "Help"
                        }
                    ]
                }
            ]
        }
    elif len(client_logs) == 1:
        payload = {
            "speech": "Log {} was deleted. You were switched to log {}.\nWhat should I do next?".format(collection_name, log_last_used),
            "rich_messages": [
                {
                    "platform": "telegram",
                    "type": 1,
                    "title": "Log {} was deleted".format(collection_name),
                    "subtitle": "You were switched to log {}.\nWhat should I do next?".format(log_last_used),
                    "buttons": [
                        {
                            "postback": "Add payment",
                            "text": "Add payment"
                        },
                        {
                            "postback": "Balance",
                            "text": "Balance"
                        },
                        {
                            "postback": "Statement",
                            "text": "Statement"
                        },
                        {
                            "postback": "Help",
                            "text": "Help"
                        }
                    ]
                }
            ]
        }
    else:
        other_logs = ""
        for log in client_logs:
            if log != log_last_used:
                if other_logs != "":
                    other_logs += ", "
                other_logs += "\"{}\"".format(log)
        payload = {
            "speech": "Log {} was deleted. You were switched to log {}.\nYou also have logs {}. What should I do next?".format(collection_name, log_last_used, other_logs),
            "rich_messages": [
                {
                    "platform": "telegram",
                    "type": 1,
                    "title": "Log {} was deleted".format(collection_name),
                    "subtitle": "You were switched to log {}.\nWhat should I do next?".format(log_last_used),
                    "buttons": [
                        {
                            "postback": "Switch log",
                            "text": "Switch log"
                        },
                        {
                            "postback": "Add payment",
                            "text": "Add payment"
                        },
                        {
                            "postback": "Balance",
                            "text": "Balance"
                        },
                        {
                            "postback": "Help",
                            "text": "Help"
                        }
                    ]
                }
            ]
        }

    response = {"status": "ok", "payload": payload}
    return response

def add_payment(req):
    '''
        Function gets
        1) req - info about transaction from JSON via webhook (user1=payer, user2[optinally]=receiver of
        direct payment, otherwise user1 pays for all (including him/herself), payment sum (in basic currency or other
        currency that has to be converted into basic currency),
        2) collection name and
        calculates what each user gets after this transaction and inserts in collection a document with add
        payment data - see below
    '''
    # Response to be returned
    response = {"status": None, "payload": None}

    # 1. Get parameters from JSON
    user1 = req.get('result').get('parameters').get('user1') # USER1 is payer, required
    user2 = req.get('result').get('parameters').get('user2') # USER2 is receiver in direct transactions, otherwise USER1 pays for all (including himself), optional
    sum = req.get('result').get('parameters').get('sum') # {"amount": 100, "currency": "USD"}
    sum_basic_currency = req.get('result').get('parameters').get('sum_basic_currency')
    creator_id = req_inside(req)["id"] # request is supposed to be not from Dialogflows' web demo but from integration platform
    client = MongoClient()
    db = client.CBB
    collection = db.clients.find_one({"user_id": creator_id})

    print('user1 (payer): ' + user1)
    print('user2 (receiver): ' + user2)
    print('sum: ' + str(sum))
    print('sum_basic_currency: ' + str(sum_basic_currency))

    # 2. Check if such collection (log) exists, belongs to sender and if collection is not deleted (=="active")
    if not collection or collection["log_last_used"] == "":
        payload = {
            "speech": "Sorry but you don't have any logs. Would you like me to create one for you?",
            "rich_messages": [
                {
                    "platform": "telegram",
                    "type": 1,
                    "title": "Sorry but you don't have any logs",
                    "subtitle": "Would you like me to create one for you?",
                    "buttons": [
                        {
                            "postback": "Create log",
                            "text": "Create log"
                        },
                        {
                            "postback": "Help",
                            "text": "Help"
                        }
                    ]
                }
            ]
        }
        response = {"status": "error", "payload": payload}
        return response
    else:
        collection_name = collection["log_last_used"]

    print("collection_name: {}".format(collection_name))

    try: # If such collection exists for creator_id
        log_info = db[collection_name].find_one({"log": "info"})
        if log_info["creator_id"] != creator_id:
            response = {"status": "error", "payload": {"speech": "You don't have a log named '{}'".format(collection_name)}}
            return response

        if log_info["log_status"] == "inactive":
            response = {"status": "error", "payload": {"speech": "Log has been deleted"}}
            return response
    except Exception as error:
        response = {"status": "error", "payload": {"speech": "add_payment()-1: {}".format(error)}}
        return response

    # 3. Check if user1 and/or user2 belong to active_users (the 1st document in collection, log_info)
    log_info = db[collection_name].find_one({"log": "info"})
    users = log_info["active_users"]
    our_users = ""
    for x in range(len(users)):
        if x == 0:
            our_users += users[x]
        else:
            our_users += ", " + users[x]
    if user1 not in users and (user2 != "" and user2 not in users):
        response = {"status": "error",
                    "payload": {"speech": "Sorry, who are {} and {}? Can't find them in our user list ({})".format(user1, user2, our_users)}}
        return response
    if user1 not in users:
        response = {"status": "error", "payload": {"speech": "Sorry, who is {}? Can't find him/her in our user list ({})".format(user1, our_users)}}
        return response
    if user2 != "" and user2 not in users:
        response = {"status": "error",
                    "payload": {"speech": "Sorry, who is {}? Can't find him/her in our user list ({})".format(user2, our_users)}}
        return response

    # 4. Check if user1 is not the only user (other users hasn't been added yet)
    if len(users) == 1:
        payload = {
            "speech": "Sorry but you can't add payments yet because at the moment your log \"{}\" contains only 1 user - you ;) \nTo continue please add users".format(
                collection_name),
            "rich_messages": [
                {
                    "platform": "telegram",
                    "type": 1,
                    "title": "Please add users",
                    "subtitle": "Sorry but you can't add payments yet because at the moment your log \"{}\" contains only 1 user - you ;)".format(collection_name),
                    "buttons": [
                        {
                            "postback": "Add new user",
                            "text": "Add user"
                        },
                        {
                            "postback": "Help",
                            "text": "Help"
                        }
                    ]
                }
            ]
        }
        response = {"status": "error", "payload": payload}
        return response


    # 5. If currency != basic (for eg., UAH), convert to basic currency
    if sum == "":
        amount = float(sum_basic_currency)
    else:
        if sum["currency"] == BASIC_CURRENCY:
            amount = sum["amount"]
        elif sum["currency"] == "USD":
            amount = sum["amount"] * usd_uah
        elif sum["currency"] == "EUR":
            amount = sum["amount"] * eur_uah

    # 6. User is supposed to enter positive values for payments
    # Negative values will be *-1
    if amount<0:
        amount *= -1
    print('sum_converted: ' + str(amount))

    # 7. Calculate what users get in this transaction
    # If user2 == empty, then user1 (payer) pays for all, else user1 pays directly to user2, other users' (if such) balance remains unchanged
    if user2 == "": # means that user1 paid for all = he gets his sum - sum/users_quantity, for eg. if 2 users and user1 paid $50, his balance will be +25$
        who_received = "all"
        #every_user_gets = amount / len(log["users"])
        payer_gets = amount - amount / len(users)
        recipient_gets = amount / len(users) * -1
    else:
        if user1 == user2:
            response = {"status": "error", "payload": "Giving money to yourself may be funny but doesn't change balance. Please define who benefits from this transaction"}
            return response
        who_received = user2
        payer_gets = amount
        recipient_gets = amount * -1

    print('payer_gets: ' + str(payer_gets))
    print('recipient_gets: ' + str(recipient_gets))

    # 8. Prepare document to be inserted to DB
    add_payment_action = {
        # '_id': 0, = creation date, used for sorting
        'creator_id': creator_id,
        'users': users,
        'modified': {
            'status': False,
            'date': None
        },
        'deleted': {
            'status': False,
            'date': None
        },
        'payment_n': 0, # is updated using update_balance(); for deleted payments = -1
        'action_type': 'add_payment',
        'transaction_balance': {}, # updated below in cycle
        'total_balance': {}, # updated below in cycle
        'who_paid': user1,
        'who_received': who_received,
        'amount': amount
    }

    for user in users:
        if user != user1: # calculate what recipient(s) gets/get
            if user2 == "": # "pay for all", each recepient gets amount / usersN
                add_payment_action["transaction_balance"].update({user: recipient_gets})
            else:
                if user == user2: # direct transaction between user1 and user2
                    add_payment_action["transaction_balance"].update({user: recipient_gets})
                else: # direct transaction between user1 and user2, other users get 0
                    add_payment_action["transaction_balance"].update({user: 0})
        else: # calculate what payer looses
            add_payment_action["transaction_balance"].update({user: payer_gets})

    # 9. Insert document into DB
    add_payment_action_id = db[collection_name].insert_one(add_payment_action).inserted_id

    print("add_payment_action: {}".format(add_payment_action))

    # 10. Final Ok response
    response = {"status": "ok", "payload": add_payment_action_id}

    return response

def update_balance(req):
    '''
        Function recalculates values in 'total_balance' for the whole log, taking into consideration
        added payments, changes in initial balance, deletion and modification of payments
    '''
    # Response to be returned
    response = {"status": None, "payload": None}

    # 1. Get name of our collection/log
    creator_id = req_inside(req)["id"] # request is supposed to be not from Dialogflows' web demo but from integration platform
    client = MongoClient()
    db = client.CBB
    collection = db.clients.find_one({"user_id": creator_id})

    if not collection or collection["log_last_used"] == "":
        payload = {
            "speech": "Sorry but you don't have any logs. Would you like me to create one for you?",
            "rich_messages": [
                {
                    "platform": "telegram",
                    "type": 1,
                    "title": "Sorry but you don't have any logs",
                    "subtitle": "Would you like me to create one for you?",
                    "buttons": [
                        {
                            "postback": "Create log",
                            "text": "Create log"
                        },
                        {
                            "postback": "Help",
                            "text": "Help"
                        }
                    ]
                }
            ]
        }
        response = {"status": "error", "payload": payload}
        return response
    else:
        collection_name = collection["log_last_used"]

    try:
        # 2. Get initial balance from the 1st document by "_id" (date)
        initial_balance = db[collection_name].find_one({"log": "info"})[
            "initial_balance"]  # dictionary - {"Tim": 0, "Dan": 0}
        print("Initial balance: {}".format(initial_balance))

        # 3. Iterate through documents (actions) and get documents with "action_type" == "add_payment" and
        # "deleted.status" == False
        filter1 = {"action_type": "add_payment"}
        filter2 = {"deleted.status": False}
        payments = db[collection_name].find({"$and": [filter1, filter2]})

        payment_n = 0  # payments counter

        # Iterate through selected payments
        for payment in payments:
            action_id = payment["_id"]

            # Get transaction balance (what each active user gets)
            transaction_balance = payment["transaction_balance"]
            print("transaction_balance: {}".format(transaction_balance))
            total_balance = {}

            # Calculate current total balance for each user after this payment
            for user, user_gets in transaction_balance.items():
                if user in initial_balance:  # for existing users
                    total_balance.update({user: (initial_balance[user] + user_gets)})
                    initial_balance[user] = total_balance[user]
                else:  # In case user was added
                    total_balance[user] = user_gets
                    initial_balance[user] = user_gets

            print("Initial balance-X: {}".format(initial_balance))

            # If user was deleted and is not present in transaction_balance dict, delete it from
            # initial_balance dict (which is being updated in cycle)
            for user in list(initial_balance):
                if user not in transaction_balance.keys():
                    del initial_balance[user]

            # Payment counter
            payment_n += 1

            # 4. Update total_balance in corresponding document in DB
            try:
                db[collection_name].update_one({"_id": action_id}, {'$set': {"total_balance": total_balance}})
                db[collection_name].update_one({"_id": action_id}, {'$set': {"payment_n": payment_n}})
            except Exception as error:
                response = {"status": "error", "payload": {"speech": "update_balance(): {}".format(error)}}
                return response

    except Exception as error:
        response = {"status": "error", "payload": {"speech": "update_balance(): {}".format(error)}}
        #print(str(response))
        return response

    # 5. Prepare Ok response
    response = {"status": "ok", "payload": {"speech": "Total balance recalculated successfully"}}
    return response

def balance(req, user="all"):
    '''
        Function gets
        1) JSON from webhook to determine active log and
        2) specific user name (optional, in case no user is passed - balance is displayer for all active users),
        and returns balance for users/respective user
    '''
    # Response to be returned
    response = {"status": None, "payload": None}

    # 1. Get name of our collection/log
    creator_id = req_inside(req)["id"]
    client = MongoClient()
    db = client.CBB
    collection = db.clients.find_one({"user_id": creator_id})

    if not collection or collection["log_last_used"] == "":
        payload = {
            "speech": "Sorry but you don't have any logs. Would you like me to create one for you?",
            "rich_messages": [
                {
                    "platform": "telegram",
                    "type": 1,
                    "title": "Sorry but you don't have any logs",
                    "subtitle": "Would you like me to create one for you?",
                    "buttons": [
                        {
                            "postback": "Create log",
                            "text": "Create log"
                        },
                        {
                            "postback": "Help",
                            "text": "Help"
                        }
                    ]
                }
            ]
        }
        response = {"status": "error", "payload": payload}
        return response
    else:
        collection_name = collection["log_last_used"]

    try:
        # 2. Check if "user" == specific user (not "all") and if so - if he/she is among our active users
        active_users = db[collection_name].find_one({"log": "info"})["active_users"]
        if user != "all":
            if user not in active_users:
                response = {"status": "error", "payload": {"speech": "User {} not found".format(user)}}
                return response

        # 3. Get the last document of type add_payment which is not deleted and retrieve "total_balance" field
        filter1 = {"action_type": "add_payment"}
        filter2 = {"deleted.status": False}
        output_filter = {"_id": 0, "total_balance": 1}
        payments = db[collection_name].find({"$and": [filter1, filter2]}, output_filter).sort([('_id', -1)]).limit(1)
        # if no payments have been added yet
        if payments.count() == 0:
            # if we don't have payments yet then:
            # 1) there might be only 1 user (log creator) with initial balance in the 1st document
            # 2) another user(-s) may have been added but they will have their 1st total_balance only after the 1st payment
            # For now if no payments exist yet, let's take active_users from the 1st doc and set their balance to 0
            balance_data = {}
            for active_user in active_users:
                balance_data[active_user] = 0
            print("balance_data: {}".format(balance_data))
        else:
            for payment in payments: # 1 cycle only
                balance_data = payment["total_balance"]

        # But another variant is also possible when user who participated in payments was removed (with balance 0),
        # so we needn't display his zero balance any more
        for another_user in list(balance_data):
            if another_user not in active_users:
                del balance_data[another_user]
        '''
        interim_balance_data = balance_data
        print("interim_balance_data: {}".format(interim_balance_data))
        print("balance_data: {}".format(balance_data))
        for another_user in interim_balance_data.keys():
            print("another_user: {}".format(another_user))
            print("active_users: {}".format(active_users))
            print("balance_data1: {}".format(balance_data))
            if another_user not in active_users:
                del balance_data[another_user]
                print("balance_data2: {}".format(balance_data))
        '''

        # The variant when balance is fetched after new user was added (which will be absent in the last payment document)
        for my_user in active_users:
            if my_user not in balance_data.keys():
                balance_data[my_user] = float(0)

        print("BALANCE DATA 1982")
        print("balance_data: {}".format(balance_data))

        # 4. Formulate response
        if user == "all":
            balance = ""
            for everyuser, everyuser_balance in balance_data.items():
                if balance != "":
                    balance += "\n"
                balance += "{}: {}".format(everyuser, "{0:.2f}".format(everyuser_balance))
        else:
            balance = "{}: {}".format(user, "{0:.2f}".format(balance_data[user]))

        payload = {
            "speech": "Current balance: {}".format(balance),
            "rich_messages": [
                {
                    "platform": "telegram",
                    "type": 1,
                    "title": "Current balance:",
                    "subtitle": "{}\nWhat should I do next?".format(balance),
                    "buttons": [
                        {
                            "postback": "Add payment",
                            "text": "Add payment"
                        },
                        {
                            "postback": "Balance",
                            "text": "Balance"
                        },
                        {
                            "postback": "Statement",
                            "text": "Statement"
                        },
                        {
                            "postback": "Help",
                            "text": "Help"
                        }
                    ]
                }
            ]
        }

    except Exception as error:
        response = {"status": "error", "payload": {"speech": "balance(): {}".format(error)}}
        return response

    # 5. Prepare Ok response
    response = {"status": "ok", "payload": payload}
    return response

def statement(req):
    '''
        Function a text statement with all transactions (log creation, payments, adding/deleting users;
        deleting/modifying payments are not displayed)
    '''
    # Response to be returned
    response = {"status": None, "payload": None}
    statement = ""

    # 1. Get name of our collection/log
    creator_id = req_inside(req)["id"]
    client = MongoClient()
    db = client.CBB
    collection = db.clients.find_one({"user_id": creator_id})

    if not collection or collection["log_last_used"] == "":
        payload = {
            "speech": "Sorry but you don't have any logs. Would you like me to create one for you?",
            "rich_messages": [
                {
                    "platform": "telegram",
                    "type": 1,
                    "title": "Sorry but you don't have any logs",
                    "subtitle": "Would you like me to create one for you?",
                    "buttons": [
                        {
                            "postback": "Create log",
                            "text": "Create log"
                        },
                        {
                            "postback": "Help",
                            "text": "Help"
                        }
                    ]
                }
            ]
        }
        response = {"status": "error", "payload": payload}
        return response
    else:
        collection_name = collection["log_last_used"]


    try:
        # 2. Check if collection is active (hasn't been deleted)
        log_info = db[collection_name].find_one({"log": "info"})
        if log_info["log_status"] == "inactive":
            response = {"status": "error", "payload": {"speech": "Log has been deleted"}}
            return response

        # 3. Get documents with "action_type" "log" (log creation info), 'add_payment', "add_user" and "delete_user"
        filter = {
            "$or": [
                {"log": "info"},
                {
                    "$and": [
                        {"action_type": "add_payment"},
                        {"deleted.status": False}
                    ]
                },
                {"action_type": "add_user"},
                {"action_type": "delete_user"}
            ]
        }
        actions = db[collection_name].find(filter)
        for action in actions:
            # Log creation info
            if "log" in action:
                # Date/time log was created
                timestamp = "{} {}".format(action["_id"].generation_time.date(), action["_id"].generation_time.time())

                # Log name
                log_name = action["log_name"]

                # Initial users and initial balance ("active" users field can be being updated)
                initial_users = ""
                initial_balance = ""
                for user, user_balance in action["initial_balance"].items():
                    if initial_users != "":
                        initial_users += ", "
                        initial_balance += "\n"
                    initial_users += user
                    initial_balance += "{}: {}".format(user, "{0:.2f}".format(user_balance))

                # Compose block for "log" action
                log_statement = "Date/Time: {}\nLog \"{}\" was created\nUsers: {}\nBalance:\n{}".format(timestamp, log_name, initial_users, initial_balance)
                statement += log_statement

            # add_payment
            if "action_type" in action and action["action_type"] == "add_payment":
                # Payments counter
                payment_number = action["payment_n"]

                # Payment's date/time
                timestamp = "{} {}".format(action["_id"].generation_time.date(), action["_id"].generation_time.time())

                # Payer
                who_paid = action["who_paid"]

                # Beneficiary(-ies)
                if action["who_received"] == "all":
                    who_received = "for all"
                else:
                    who_received = "to {}".format(action["who_received"])

                # Payment sum
                amount_basic_currency = action["amount"]

                # Balance
                balance = ""
                for user, user_balance in action["total_balance"].items():
                    if balance != "":
                        balance += "\n"
                    balance += "{}: {}".format(user, "{0:.2f}".format(user_balance))

                # Compose block for "add_payment" action
                payment_statement = "Date/Time: {}\nTransaction #: {}\n{} paid {} {} {}\nBalance: \n{}".format(timestamp, payment_number, who_paid, amount_basic_currency, BASIC_CURRENCY, who_received, balance)
                statement += "\n{}\n".format("*"*27)
                statement += payment_statement

            # add_user
            if "action_type" in action and action["action_type"] == "add_user":
                # Action's date/time
                timestamp = "{} {}".format(action["_id"].generation_time.date(), action["_id"].generation_time.time())

                # User added
                user_added = action["new_user"]

                # Users after addition
                active_users = ""
                for user in action["users_after_addition"]:
                    if active_users != "":
                        active_users += ", "
                    active_users += user

                    # Compose block for "add_user" action
                add_user_statement = "Date/Time: {}\nUser {} was added with balance 0\nActive users: {}".format(timestamp, user_added, active_users)
                statement += "\n{}\n".format("*" * 27)
                statement += add_user_statement

            # delete user
            if "action_type" in action and action["action_type"] == "delete_user":
                # Action's date/time
                timestamp = "{} {}".format(action["_id"].generation_time.date(), action["_id"].generation_time.time())

                # User added
                deleted_user = action["deleted_user"]

                # Users after deletion
                active_users = ""
                for user in action["users_after_deletion"]:
                    if active_users != "":
                        active_users += ", "
                    active_users += user

                # Compose block for "add_user" action
                add_user_statement = "Date/Time: {}\nUser {} was removed\nActive users: {}".format(timestamp, deleted_user, active_users)
                statement += "\n{}\n".format("*" * 27)
                statement += add_user_statement

        payload = {
            "speech": "Here's our statement:\n\n{}".format(statement),
            "rich_messages": [
                {
                    "platform": "telegram",
                    "type": 0,
                    "speech": "Here's our statement:\n\n{}".format(statement),
                },
                {
                    "platform": "telegram",
                    "type": 1,
                    "title": "What should I do next?",
                    "buttons": [
                        {
                            "postback": "Add payment",
                            "text": "Add payment"
                        },
                        {
                            "postback": "Balance",
                            "text": "Balance"
                        },
                        {
                            "postback": "Help",
                            "text": "Help"
                        }
                    ]
                }
            ]
        }

    except Exception as error:
        response = {"status": "error", "payload": {"speech": "statement(): {}".format(error)}}
        return response

    # 5. Prepare Ok response
    response = {"status": "ok", "payload": payload}
    return response

def add_user(req):
    '''
        Function gets JSON from webhook and extracts user_id (which is further used to get last used log)
        and the name of new user to add, and
        1) updates a list of active users in the 1st document (with "log": "info")
        2) inserts a new document with information on adding a new user
        3) returns a message about user addition
    '''
    # Response to be returned
    response = {"status": None, "payload": None}

    print()
    print("req: {}".format(req))
    print()

    # 1. Get input parameters (creator_id, collection_name, user)
    creator_id = req_inside(req)["id"]
    user = req["result"]["parameters"]["user"]

    client = MongoClient()
    db = client.CBB
    collection = db.clients.find_one({"user_id": creator_id})

    print()
    print("creator_id: {}, user: {}, collection_name: {}".format(creator_id, user, collection))
    print()

    # user may be not registered yet or may have deleted all logs ("log_last_used" == "")
    if not collection or collection["log_last_used"] == "":
        payload = {
            "speech": "Sorry but you don't have any logs. Would you like me to create one for you?",
            "rich_messages": [
                {
                    "platform": "telegram",
                    "type": 1,
                    "title": "Sorry but you don't have any logs",
                    "subtitle": "Would you like me to create one for you?",
                    "buttons": [
                        {
                            "postback": "Create log",
                            "text": "Create log"
                        },
                        {
                            "postback": "Help",
                            "text": "Help"
                        }
                    ]
                }
            ]
        }
        response = {"status": "error", "payload": payload}
        return response
    else:
        collection_name = collection["log_last_used"]

    try:
        # 2. Get our active users list and check if user is not already there
        active_users = db[collection_name].find_one({"log": "info"})["active_users"]
        print("active_users: {}".format(active_users))
        if user in active_users:
            response = {"status": "error", "payload": {"speech": "Sorry, but we already have user {}".format(user)}}
            return response
        else:
            # 3. Update the list of active users
            active_users.append(user)
            db[collection_name].update_one({"log": "info"}, {'$set': {"active_users": active_users}})

            # 4. Prepare a document about adding new user
            add_user_action = {
                # '_id': 0, = creation date, used for sorting
                'creator_id': creator_id,
                'new_user': user,
                'users_after_addition': active_users,
                'action_type': 'add_user'
            }

            print("add_user_action")
            print(add_user_action)
            print()

            # 5. Insert documents to collection
            add_user_id = db[collection_name].insert_one(add_user_action).inserted_id
    except Exception as error:
        response = {"status": "error", "payload": {"speech": "add_user(): {}".format(error)}}
        return response

    # 5. Final Ok response
    payload = {
        "speech": "User {} successfully added. What\'s next?".format(user),
        "rich_messages": [
            {
                "platform": "telegram",
                "type": 1,
                "title": "User {} successfully added".format(user),
                "subtitle": "What\'s next?\nP.s. Enter \"add user X\" to add another user, X",
                "buttons": [
                    {
                        "postback": "Add payment",
                        "text": "Add payment"
                    },
                    {
                        "postback": "Balance",
                        "text": "Balance"
                    },
                    {
                        "postback": "Statement",
                        "text": "Statement"
                    },
                    {
                        "postback": "Help",
                        "text": "Help"
                    }
                ]
            }
        ]
    }

    response = {"status": "ok",
                "payload": payload}
    return response

def delete_user(req):
    '''
        Function gets JSON from webhook and extracts user_id (which is further used to get last used log)
        and the name of user to be removed, and
        1) updates a list of active users in the 1st document (with "log": "info")
        2) inserts a new document with information on deleting a user
        3) returns a message about user deletion
    '''

    # Response to be returned
    response = {"status": None, "payload": None}

    # 1. Get input parameters (creator_id, user to be deleted, creator 1st name)
    creator_id = req_inside(req)["id"]
    user_first_name = req_inside(req)["first_name"]
    user = req["result"]["parameters"]["user"]

    client = MongoClient()
    db = client.CBB
    collection = db.clients.find_one({"user_id": creator_id})

    # 2. Check if log exists
    if not collection or collection["log_last_used"] == "":
        payload = {
            "speech": "Sorry but you don't have any logs. Would you like me to create one for you?",
            "rich_messages": [
                {
                    "platform": "telegram",
                    "type": 1,
                    "title": "Sorry but you don't have any logs",
                    "subtitle": "Would you like me to create one for you?",
                    "buttons": [
                        {
                            "postback": "Create log",
                            "text": "Create log"
                        },
                        {
                            "postback": "Help",
                            "text": "Help"
                        }
                    ]
                }
            ]
        }
        response = {"status": "error", "payload": payload}
        return response
    else:
        collection_name = collection["log_last_used"]

    # 3. Check if user is not trying to delete him/herself (which is not allowed)
    if user == user_first_name:
        response = {"status": "error", "payload": {"speech": "Sorry, but you can't delete yourself (you are a log owner)"}}
        return response

    try:
        # 4. Get our active users list and check if user to be deleted is present there
        active_users = db[collection_name].find_one({"log": "info"})["active_users"]
        print("active_users: {}".format(active_users))
        if user not in active_users:
            response = {"status": "error", "payload": {"speech": "Sorry, but I can't find user {}".format(user)}}
            return response
        else:
            # 5. Only users with 0 balance can be removed
            filter1 = {"action_type": "add_payment"}
            filter2 = {"deleted.status": False}
            output_filter = {"_id": 0, "total_balance": 1}
            payments = db[collection_name].find({"$and": [filter1, filter2]}, output_filter).sort(
                [('_id', -1)]).limit(1)

            # If no last payment was found (no payments have been added yet)
            #  then all users are supposed to have 0 balance which is Ok
            if payments.count() == 0:
                balance_data = {}
                for active_user in active_users:
                    balance_data[active_user] = 0
                deleted_user_balance = balance_data[user]
                print("balance_data: {}".format(balance_data))
            else:
                # Get last total balance
                for payment in payments: # executes only once
                    balance_data = payment["total_balance"]
                    deleted_user_balance = balance_data[user]

            if deleted_user_balance != 0:
                response = {"status": "error", "payload": {"speech": "Sorry but only users with 0 (zero) balance can be removed"}}
                return response

            # 6. Update the list of active users
            active_users.remove(user)
            users_left = ""
            for user_left in active_users:
                if users_left != "":
                    users_left += ", "
                users_left += user_left

            db[collection_name].update_one({"log": "info"}, {'$set': {"active_users": active_users}})

            # 7. Prepare document about adding new user
            delete_user_action = {
                # '_id': 0, = creation date, used for sorting
                'creator_id': creator_id,
                'deleted_user': user,
                'users_after_deletion': active_users,
                'action_type': 'delete_user'
            }

            # 8. Insert documents to collection
            delete_user_id = db[collection_name].insert_one(delete_user_action).inserted_id
    except Exception as error:
        response = {"status": "error", "payload": "delete_user(): {}".format(error)}
        return response

    # 9. Final Ok response
    # Buttons in card should correspond to how many users are left: if only 1 then "add payment" button is not good
    buttons = []
    if len(active_users) == 1:
        buttons.append(
            {
                "postback": "Add new user",
                "text": "Add user"
            }
        )
    else:
        buttons.append(
            {
                "postback": "Add payment",
                "text": "Add payment"
            }
        )

    buttons.extend(
        (
            {
                "postback": "Balance",
                "text": "Balance"
            },
            {
                "postback": "Statement",
                "text": "Statement"
            },
            {
                "postback": "Help",
                "text": "Help"
            }
        )
    )

    payload = {
        "speech": "User {} successfully removed. Users left: {}. What\'s next?".format(user, users_left),
        "rich_messages": [
            {
                "platform": "telegram",
                "type": 1,
                "title": "User {} successfully removed".format(user),
                "subtitle": "Users left: {}. What\'s next?".format(users_left),
                "buttons": buttons
            }
        ]
    }

    response = {"status": "ok",
                "payload": payload}

    return response

def delete_payment(req):
    '''
        Function gets JSON from webhook and extracts user_id (which is further used to get the name of the log)
        and the number of payment to be removed, then finds the corresponding payment
        (document with "action_type": "add_payment" and "payment_n": payment2delete) and
        1) changes deleted.status from False to True, and also sets deleted.date to current date/time
        2) changes "payment_n" to "DELETED" (>> update_balance() )
        3) returns a message about payment deletion
    '''

    # Response to be returned
    response = {"status": None, "payload": None}

    # 1. Get input parameters (creator_id, user to be deleted, creator 1st name)
    creator_id = req_inside(req)["id"]
    #user_first_name = req_inside(req)["first_name"]
    #user = req["result"]["parameters"]["user"]
    payment2delete = req["result"]["parameters"]["payment2delete"]
    print("payment2delete: {}".format(payment2delete))

    client = MongoClient()
    db = client.CBB
    collection = db.clients.find_one({"user_id": creator_id})

    # 2. Check if log exists
    if not collection or collection["log_last_used"] == "":
        payload = {
            "speech": "Sorry but you don't have any logs. Would you like me to create one for you?",
            "rich_messages": [
                {
                    "platform": "telegram",
                    "type": 1,
                    "title": "Sorry but you don't have any logs",
                    "subtitle": "Would you like me to create one for you?",
                    "buttons": [
                        {
                            "postback": "Create log",
                            "text": "Create log"
                        },
                        {
                            "postback": "Help",
                            "text": "Help"
                        }
                    ]
                }
            ]
        }
        response = {"status": "error", "payload": payload}
        return response
    else:
        collection_name = collection["log_last_used"]
    print("collection_name: {}".format(collection_name))

    # 3. Find document with "action_type": "add_payment" and "payment_n": payment2delete
    try:
        payment2delete = int(payment2delete)

        filter1 = {"action_type": "add_payment"}
        filter2 = {"payment_n": payment2delete}
        deleted_payment = db[collection_name].find_one({"$and": [filter1, filter2]})
        print("deleted_payment: {}".format(deleted_payment))

        if not deleted_payment:
            response = {"status": "error", "payload": {"speech": "Sorry, but I failed to find payment {}".format(payment2delete)}}
            return response
        else:
            # 4. Change deleted.status from False to True, set deleted.date to current date/time, payment_n >> "DELETED"
            current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            db[collection_name].update_one({"_id": deleted_payment["_id"]}, {'$set': {"deleted.status": True}})
            db[collection_name].update_one({"_id": deleted_payment["_id"]}, {'$set': {"deleted.date": current_datetime}})
            db[collection_name].update_one({"_id": deleted_payment["_id"]},
                                           {'$set': {"payment_n": "DELETED"}})

    except Exception as error:
        response = {"status": "error", "payload": {"speech": "delete_payment(): {}".format(error)}}
        return response

    # 5. Final Ok response
    payload = {
        "speech": "Payment {} successfully removed. What\'s next?".format(payment2delete),
        "rich_messages": [
            {
                "platform": "telegram",
                "type": 1,
                "title": "Payment {} successfully removed".format(payment2delete),
                "subtitle": "What\'s next?",
                "buttons": [
                    {
                        "postback": "Add new payment",
                        "text": "Add payment"
                    },
                    {
                        "postback": "Balance",
                        "text": "Balance"
                    },
                    {
                        "postback": "Statement",
                        "text": "Statement"
                    },
                    {
                        "postback": "Help",
                        "text": "Help"
                    }
                ]
            }
        ]
    }
    response = {"status": "ok", "payload": payload}

    return response

'''
    Functions left to create:
    edit_payment()
    delete_payment()
    set_initial_balance() ?
    change_basic_currency()
    set_exchange_rates()
    send_report_to_email()
'''

def check_for_logs(req):
    '''
        Function gets JSON from a webhook, searches in DB in collection "clients" for this user ID and channel and
        returns document for that user (or None)
    '''
    # Response to be returned
    response = {"status": None, "payload": None}

    # 1. Get user ID and first name from request
    user_id = req_inside(req)["id"]
    user_first_name = req_inside(req)["first_name"]

    channel = req["originalRequest"]["source"]

    # 2. Check DB "CBB" / collection "clients" for such user_id and return created logs and last used log (if such)
    client = MongoClient()
    db = client.CBB
    clients = db["clients"]

    try:
        criterion1 = {"user_id": user_id}
        criterion2 = {"channel": channel}
        output_filter = {"_id": 0, "logs": 1, "log_last_used": 1}
        ourclient = clients.find_one({"$and": [criterion1, criterion2]}, output_filter)

    except Exception as error:
        response = {"status": "error", "payload": "check_for_logs(): {}".format(error)}
        return response

    # 3. Final Ok response
    response = {"status": "ok", "payload": [ourclient, user_first_name]}
    return response

def welcome_response(req_for_uid):
    '''
        Function gets results of request to DB "CBB" / collection "clients" for user_id and returns a message
        depending on result:
        1) new user without logs - suggest to create a log;
        2) existing user with 1 log - continue with it;
        3) existing user with >1 logs - continue with it but remind about other logs
    '''
    # Response to be returned
    response = {"status": None, "payload": None}

    ourclient = req_for_uid[0]
    user_first_name = req_for_uid[1]

    if not ourclient: # new user, without any log
        payload = {
            "speech": "Hi, {}. I'm a CommonBalanceBot - here to help you with tracking shared expenses with your friends.\nTo start you need a log. Should I create one for you?".format(
                user_first_name),
            "rich_messages": [
                {
                    "platform": "telegram",
                    "type": 1,
                    "title": "Hi, {}!".format(user_first_name),
                    "subtitle": "I'm a CommonBalanceBot - here to help you with tracking shared expenses with your friends.\nTo start you need a log. Should I create one for you?",
                    "buttons": [
                        {
                            "postback": "Create log",
                            "text": "Create log"
                        },
                        {
                            "postback": "Help",
                            "text": "Help"
                        }
                    ]
                }
            ]
        }

    else: # existing user
        if len(ourclient["logs"]) == 0:  # with 0 logs
            payload = {
                "speech": "Welcome back, {}. To start you need a log. Should I create one for you?".format(
                    user_first_name),
                "rich_messages": [
                    {
                        "platform": "telegram",
                        "type": 1,
                        "title": "Welcome back, {}!".format(user_first_name),
                        "subtitle": "To start you need a log. Should I create one for you?",
                        "buttons": [
                            {
                                "postback": "Create log",
                                "text": "Create log"
                            },
                            {
                                "postback": "Help",
                                "text": "Help"
                            }
                        ]
                    }
                ]
            }

        elif len(ourclient["logs"]) == 1: # with 1 log
            payload = {
                "speech": "Welcome back, {}!\nContinuing with your log \"{}\"...".format(user_first_name, ourclient["logs"][0]),
                "rich_messages": [
                    {
                        "platform": "telegram",
                        "type": 1,
                        "title": "Welcome back, {}!".format(user_first_name),
                        "subtitle": "Continuing with your log \"{}\".\nWhat should I do next?".format(ourclient["logs"][0]),
                        "buttons": [
                            {
                                "postback": "Add payment",
                                "text": "Add payment"
                            },
                            {
                                "postback": "Balance",
                                "text": "Balance"
                            },
                            {
                                "postback": "Statement",
                                "text": "Statement"
                            },
                            {
                                "postback": "Help",
                                "text": "Help"
                            }
                        ]
                    }
                ]
            }

        elif len(ourclient["logs"]) == 2: # with 2 logs
            log_last_used = ourclient["log_last_used"]
            for log in ourclient["logs"]:
                if log != log_last_used:
                    another_log = log
            payload = {
            "speech": "Welcome back, {}!\nContinuing with your log \"{}\". \nEnter \"open {}\" to switch to that another log".format(user_first_name, log_last_used, another_log),
            "rich_messages": [
                {
                    "platform": "telegram",
                    "type": 1,
                    "title": "Welcome back, {}!".format(user_first_name),
                    "subtitle": "Continuing with your log \"{}\".\nBy the way you also have a log \"{}\".\nWhat should I do next?".format(log_last_used, another_log),
                    "buttons": [
                        {
                            "postback": "Open log {}".format(another_log),
                            "text": "Open \"{}\"".format(another_log)
                        },
                        {
                            "postback": "Add payment",
                            "text": "Add payment"
                        },
                        {
                            "postback": "Balance",
                            "text": "Balance"
                        },
                        {
                            "postback": "Help",
                            "text": "Help"
                        }
                    ]
                }
            ]
        }

        else: # with >2 logs
            log_last_used = ourclient["log_last_used"]
            all_logs = ""
            for log in ourclient["logs"]:
                if log != log_last_used:
                    if all_logs != "":
                        all_logs += ", "
                    all_logs += "\"{}\"".format(log)

            payload = {
                "speech": "Welcome back, {}!\nContinuing with your log \"{}\". To switch to another log ({}) please enter \"open <log name>\"".format(user_first_name, log_last_used, all_logs),
                "rich_messages": [
                    {
                        "platform": "telegram",
                        "type": 1,
                        "title": "Welcome back, {}!".format(user_first_name),
                        "subtitle": "Continuing with your log \"{}\".\nBy the way you have other logs: {}.\nWhat should I do next?".format(
                            log_last_used, all_logs),
                        "buttons": [
                            {
                                "postback": "Switch log",
                                "text": "Switch log"
                            },
                            {
                                "postback": "Add payment",
                                "text": "Add payment"
                            },
                            {
                                "postback": "Balance",
                                "text": "Balance"
                            },
                            {
                                "postback": "Help",
                                "text": "Help"
                            }
                        ]
                    }
                ]
            }

    # 3. Final Ok response
    response = {"status": "ok", "payload": payload}
    return response

def delete_log_response(req_for_uid, contexts):
    '''
        Function gets results of request to DB "CBB" / collection "clients" for user_id and returns a message
        depending on result:
        1) new user without logs - can't delete a log
        2) existing user with 1 log - please confirm deletion of the log
        3) existing user with >1 logs - choose a log to be deleted
    '''
    # Response to be returned
    response = {"status": None, "payload": None}

    ourclient = req_for_uid[0]
    user_first_name = req_for_uid[1]

    if not ourclient or (ourclient and len(ourclient["logs"]) == 0): # new user, without any log or existing user with 0 logs
        payload = {
            "speech": "Sorry but you don't have any logs. Would you like me to create one for you?",
            "rich_messages": [
                {
                    "platform": "telegram",
                    "type": 1,
                    "title": "Sorry but you don't have any logs",
                    "subtitle": "Would you like me to create one for you?",
                    "buttons": [
                        {
                            "postback": "Create log",
                            "text": "Create log"
                        },
                        {
                            "postback": "Help",
                            "text": "Help"
                        }
                    ]
                }
            ]
        }

    else: # existing user
        if len(ourclient["logs"]) == 1: # with 1 log
            payload = {
                "speech": "So, you decided to delete log \"{}\". Are you sure?\nTo delete this log please retype its name".format(ourclient["logs"][0]),
                "rich_messages": [
                    {
                        "platform": "telegram",
                        "type": 0,
                        "speech": "So, you decided to delete log \"{}\". Are you sure?\nTo delete this log please retype its name".format(
                            ourclient["logs"][0]),
                    }
                ]
            }

            # Update contexts - add context "deletion_confirmed" (to distinguish between when user retypes a log name to confirm its deletion
            # and enters a log name to select which log to delete from several existing
            contexts.append(
                {
                    'parameters': {},
                    'name': 'deletion_confirmed',
                    'lifespan': 2
                }
            )

        else: # with several logs
            log_list = ""
            buttons = []
            for log in ourclient["logs"]:
                if log_list != "":
                    log_list += ", "
                log_list + "\"{}\"".format(log)

                buttons.append(
                    {
                        "postback": log,
                        "text": log
                    }
                )

                payload = {
                    "speech": "Please select which log you would like to delete ({})".format(log_list),
                    "rich_messages": [
                        {
                            "platform": "telegram",
                            "type": 1,
                            "title": "Please select which log you would like to delete",
                            "buttons": buttons
                        }
                    ]
                }

                # Update contexts - add context "log2delete_chosen" (to distinguish between when user retypes a log name to confirm its deletion
                # and enters a log name to select which log to delete from several existing
                contexts.append(
                    {
                        'parameters': {},
                        'name': 'log2delete_chosen',
                        'lifespan': 2
                    }
                )

    # 3. Final Ok response
    response = {"status": "ok", "payload": payload, "contexts": contexts}
    return response

def besidethepoint():
    '''
        Function which returns response for cases when user's input was not mapped to any other intent
    '''
    payload = {
        "speech": "Sorry I didn't get that. What would you like me to do next?",
        "rich_messages": [
            {
                "platform": "telegram",
                "type": 1,
                "title": "Sorry I didn't get that :(",
                "subtitle": "What should I do next?",
                "buttons": [
                    {
                        "postback": "Create log",
                        "text": "Create log"
                    },
                    {
                        "postback": "Add payment",
                        "text": "Add payment"
                    },
                    {
                        "postback": "Balance",
                        "text": "Balance"
                    },
                    {
                        "postback": "Help",
                        "text": "Help"
                    }
                ]
            }
        ]
    }

    response = {"status": "ok", "payload": payload}
    return response

def faq():
    '''
        Function displays bot's commands and other info
    '''
    payload = {
        "speech": "SharedExpensesBot was created to help with tracking shared expenses for a group of people.\nHe understands the following commands:\n\nActions with logs:\ncreate log\delete log\n\nActions with users:\nadd user\nremove user\n\nActions with payments:\nadd payment\nmodify payment\ndelete payment\n\nData presentation:\nBalance\nStatement\nStatement to email\nThanks for using SharedExpensesBot!\nIurii Dziuban - March 2018 / iuriid.github.io",
        "rich_messages": [
            {
                "platform": "telegram",
                "type": 0,
                "speech": "\n\nSharedExpensesBot was created to help with tracking shared expenses for a group of people.\nHere's what it can do:\n",
            },
            {
                "platform": "telegram",
                "type": 1,
                "title": "Actions with logs",
                "buttons": [
                    {
                        "postback": "Create log",
                        "text": "Create log"
                    },
                    {
                        "postback": "Delete log",
                        "text": "Delete log"
                    }
                ]
            },
            {
                "platform": "telegram",
                "type": 1,
                "title": "Actions with users",
                "buttons": [
                    {
                        "postback": "Add new user",
                        "text": "Add user"
                    },
                    {
                        "postback": "Remove user",
                        "text": "Remove user"
                    }
                ]
            },
            {
                "platform": "telegram",
                "type": 1,
                "title": "Actions with payments",
                "buttons": [
                    {
                        "postback": "Add payment",
                        "text": "Add payment"
                    },
                    {
                        "postback": "Modify payment",
                        "text": "Modify payment"
                    },
                    {
                        "postback": "Delete payment",
                        "text": "Delete payment"
                    }
                ]
            },
            {
                "platform": "telegram",
                "type": 1,
                "title": "Data presentation",
                "buttons": [
                    {
                        "postback": "Balance",
                        "text": "Balance"
                    },
                    {
                        "postback": "Statement",
                        "text": "Statement"
                    },
                    {
                        "postback": "Send statement to email",
                        "text": "Statement to email"
                    }
                ]
            },
            {
                "platform": "telegram",
                "type": 0,
                "speech": "Thanks for using SharedExpensesBot!\nIurii Dziuban - March 2018 / iuriid.github.io\n\n",
            },
        ]
    }

    response = {"status": "ok", "payload": payload}
    return response
##################### TESTING ##############################################
#creator_id = myinput3["originalRequest"]["data"]["message"]#["chat"]["id"]
#print(creator_id)
users = ['Tim', 'Dan', 'Ann']
collection_name1 = "zeta-beaver-260218"
collection_name = "kappa-bat-280218"

#print(create_log(creator_id, users))
#print(add_payment(myinput1, collection_name))
#print(delete_log(collection_name, creator_id))
#print(add_user(collection_name, creator_id, "Ron"))
#print(update_balance(collection_name))
#print(balance(collection_name))
#print(statement(collection_name))
#print(delete_user(collection_name, creator_id, "Ron"))
#print(statement(collection_name))
#print(check_for_logs(myinput2))
print(delete_payment(myinput2))
