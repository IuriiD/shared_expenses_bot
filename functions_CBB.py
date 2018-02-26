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
        "amount": 20,
        "currency": "USD"
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

myinput3 = {
  'transactions': [
    {
      'total_balance': {
        'Tim': 0, 'Ann': 0, 'Dan': 0
      },
      'timestamp': 'today',
      'amount': 0,
      'who_paid': '',
      'who_received': 'all',
      'transaction_balance': {},
      'transaction_number': 0
    },
    {
      'total_balance': {
        'Tim': -66.67, 'Ann': -66.67, 'Dan': 133.33
      },
      'timestamp': '2018-02-22T09:01:10.433Z',
      'amount': 200,
      'who_paid': 'Dan',
      'who_received': 'all',
      'transaction_balance': {
        'Tim': -66.66666666666667, 'Ann': -66.66666666666667, 'Dan': 133.33333333333331
      },
      'transaction_number': 2
    }
  ],
  'users': ['Tim', 'Dan', 'Ann']
}

myinput4 = {'transactions': [{'transaction_balance': {}, 'total_balance': {'Ann': 0, 'Tim': 0, 'Dan': 0}, 'who_paid': '', 'who_received': 'all', 'amount': 0, 'timestamp': 'start', 'transaction_number': 0}, {'transaction_balance': {'Ann': -179.33333333333334, 'Tim': 358.66666666666663, 'Dan': -179.33333333333334}, 'total_balance': {'Ann': -179.33, 'Tim': 358.67, 'Dan': -179.33}, 'who_paid': 'Tim', 'who_received': 'all', 'amount': 538.0, 'timestamp': '2018-02-23T10:24:59.404Z', 'transaction_number': 1}, {'transaction_balance': {'Ann': -166.66666666666666, 'Tim': -166.66666666666666, 'Dan': 333.33333333333337}, 'total_balance': {'Ann': -346.0, 'Tim': 192.0, 'Dan': 154.0}, 'who_paid': 'Dan', 'who_received': 'all', 'amount': 500.0, 'timestamp': '2018-02-23T10:25:13.811Z', 'transaction_number': 2}, {'transaction_balance': {'Ann': 200.0, 'Tim': -200.0, 'Dan': 0}, 'total_balance': {'Ann': -146.0, 'Tim': -8.0, 'Dan': 154.0}, 'who_paid': 'Ann', 'who_received': 'Tim', 'amount': 200.0, 'timestamp': '2018-02-23T10:25:33.219Z', 'transaction_number': 3}, {'transaction_balance': {'Ann': 538.0, 'Tim': -269.0, 'Dan': -269.0}, 'total_balance': {'Ann': 392.0, 'Tim': -277.0, 'Dan': -115.0}, 'who_paid': 'Ann', 'who_received': 'all', 'amount': 807.0, 'timestamp': '2018-02-23T10:25:50.724Z', 'transaction_number': 4}, {'transaction_balance': {'Ann': -277.0, 'Tim': 277.0, 'Dan': 0}, 'total_balance': {'Ann': 115.0, 'Tim': 0.0, 'Dan': -115.0}, 'who_paid': 'Tim', 'who_received': 'Ann', 'amount': 277.0, 'timestamp': '2018-02-23T20:07:13.708Z', 'transaction_number': 5}, {'total_balance': {'Ann': 0.0, 'Tim': 0.0, 'Dan': 0.0}, 'transaction_balance': {'Ann': -115.0, 'Tim': 0, 'Dan': 115.0}, 'amount': 115.0, 'who_paid': 'Dan', 'who_received': 'Ann', 'timestamp': '2018-02-23T20:07:24.209Z', 'transaction_number': 6}], 'users': ['Tim', 'Dan', 'Ann']}

def add_payment_old(req):
    '''
        Function gets 1) info about transaction from JSON from webhook (user1=payer, user2(optinally)=receiver of
        direct payment, otherwise user1 pays for all (including him/herself), payment sum (in basic currency or other
        currency that has to be converted into basic currency) and 2) retrieves transaction log from txt file and
        updates it with a new transaction. Returns dictionary with transactions (log) which is saved in txt file
    '''
    # Get our log (txt file will be substituted with Mongo DB)
    with open("log.txt", "r+") as logfromtxt:
        log = ast.literal_eval(logfromtxt.read())

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
                "transaction_number": len(log["transactions"]),
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

    return log

def fetch_balance(transaction):
    '''
        Supportive function that takes a transaction block and returns balances for users
    '''
    total_balance = transaction["total_balance"]
    output = ""
    for user, user_balance in total_balance.items():
        output += "\n{}: {}".format(user, user_balance)
    return output

def balance(user):
    '''
        Function gets
        1) specific user name (optional, in case no user is passed - displays balance for all users),
        2) reads our transactions log from a txt (later - DB) and
        returns a string with this balance
    '''
    # Get our log (txt file will be substituted with Mongo DB)
    with open("log.txt", "r") as logfromtxt:
        log = ast.literal_eval(logfromtxt.read())

    # Get last transaction
    last_transaction = log["transactions"][len(log["transactions"])-1]
    #print('last_transaction: ' + str(last_transaction))

    if user == "all":
        balance = "Current balance:"
        for everyuser, everyuser_balance in last_transaction["total_balance"].items():
            balance += "\n{}: {}".format(everyuser, everyuser_balance)
    else:
        balance = "Current balance for user {}: {}".format(user, last_transaction["total_balance"][user])

    return balance

def statement():
    '''
        Function reads log.txt and returns a text statement with all transactions
    '''
    with open("log.txt", "r") as logfromtxt:
        log = ast.literal_eval(logfromtxt.read())

    for x in range(len(log["transactions"])):
        if x == 0:
            start_transaction = log["transactions"][0]
            report = "Start\nDate/Time: {}\nBalance:{}".format(start_transaction["timestamp"], fetch_balance(start_transaction))
        else:
            every_transaction = log["transactions"][x]
            transaction_number = every_transaction["transaction_number"]
            date_time = every_transaction["timestamp"]
            who_paid = every_transaction["who_paid"]
            amount = every_transaction["amount"]
            who_received = every_transaction["who_received"]
            if who_received == "all":
                what_happened = "{} paid {} {} for all".format(who_paid, amount, BASIC_CURRENCY)
            else:
                what_happened = "{} paid {} {} to {}".format(who_paid, amount, BASIC_CURRENCY, who_received)
            report += "\n###########################\nTransaction #: {}\nDate/Time: {}\n{}\nBalance:{}".format(transaction_number, date_time, what_happened, fetch_balance(every_transaction))

    return report

def commonbalancebot_speech(ourspeech, oursource, outputcontext):
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

def create_log(creator_id, users):
    '''
        Function creates a collection in DB "CBB" under randomly generated name in format <greek letter>-<animal>-<today's date>
        and inserts 2 documents:
        1) document with log info and
        2) document with log creation data - see below
    '''
    # Response to be returned
    response = {"status": None, "payload": None}

    # 1. Generate collection name
    first_part = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta", "eta", "theta", "kappa", "omicron", "sigma", "tau", "upsilon", "phi", "chi", "psi", "omega"]
    second_part = ["cat", "dog", "frog", "chicken", "rabbit", "wolf", "bear", "bat", "beaver", "bison", "pig", "horse", "cow", "monkey", "fox", "mouse", "goat", "lion", "puma", "tiger", "bat", "zebra", "seal"]
    todays_date = datetime.datetime.now().strftime("%d%m%y")
    collection_name = "{}-{}-{}".format(random.choice(first_part), random.choice(second_part), todays_date)

    # 2. Create collection
    try:
        client = MongoClient()
        db = client.CBB
        collection = db[collection_name]
    except Exception as error:
        response = {"status": "error", "payload": "Failed to create log"}
        return response

    # 3. Prepare documents
    log_info = {
        'log': 'info',
        'log_status': 'active',
        'creator_id': creator_id,
        'active_users': users,
        'initial_balance': {}
    }
    for user in users:
        log_info["initial_balance"].update({user: 0})

    create_log_action = {
        # '_id': 0, = creation date, used for sorting
        'creator_id': creator_id,
        'action_type': 'create_log'
    }

    # 4. Insert documents to collection
    try:
        log_info_id = collection.insert_one(log_info).inserted_id
        create_log_action_id = collection.insert_one(create_log_action).inserted_id
    except Exception as error:
        response = {"status": "error", "payload": error}

    # 5. Final Ok response
    response = {"status": "ok", "payload": {"collection_name": collection_name, "action_id": create_log_action_id}}
    return response

def delete_log(collection_name, creator_id):
    '''
        Function 'soft-deletes' common transactions log:
        1) updates info in the 1st document in collection with log info
        2) inserts a document with log deletion data - see below
    '''
    # 1. Response to be returned
    response = {"status": None, "payload": None}

    # 2. Check if collection exists
    client = MongoClient()
    db = client.CBB
    if collection_name in db.collection_names(): # If such collection exists in general
        try: # If such collection exists for creator_id
            log_info = db[collection_name].find_one({"log": "info"})
            if log_info["creator_id"] != creator_id:
                response = {"status": "error", "payload": "You don't have a log named '{}'".format(collection_name)}
                return response
        except Exception as error:
            response = {"status": "error", "payload": error}
            return response

        try: # If it exists but hasn't yet been deleted (inactivated)
            log_info = db[collection_name].find_one({"log": "info"})
            if log_info["log_status"] == "inactive":
                response = {"status": "error", "payload": "Log already deleted"}
                return response
        except Exception as error:
            response = {"status": "error", "payload": error}
            return response

        try: # Try to delete (inactivate) it
            db[collection_name].update_one({"log": "info"}, {'$set': {"log_status": "inactive"}})
        except Exception as error:
            response = {"status": "error", "payload": error}
            return response
    else:
        response = {"status": "error", "payload": "Log not found"}
        return response

    # 3. Prepare document to be inserted
    delete_log_action = {
        # '_id': 0, = creation date, used for sorting
        'creator_id': creator_id,
        'action_type': 'delete_log'
    }

    # 4. Insert document into DB
    try:
        delete_log_action_id =  db[collection_name].insert_one(delete_log_action).inserted_id
    except Exception as error:
        response = {"status": "error", "payload": error}
        return response

    # 5. Prepare final Ok response
    response = {"status": "ok", "payload": delete_log_action_id}
    return response

def add_payment(req, collection_name):
    '''
        Function gets
        1) info about transaction from JSON via webhook (user1=payer, user2[optinally]=receiver of
        direct payment, otherwise user1 pays for all (including him/herself), payment sum (in basic currency or other
        currency that has to be converted into basic currency),
        2) users list
        3) collection name and
        4) transaction creator ID,
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
    creator_id = req.get("originalRequest").get("data").get("message").get("from").get("id")
    print('user1 (payer): ' + user1)
    print('user2 (receiver): ' + user2)
    print('sum: ' + str(sum))
    print('sum_basic_currency: ' + str(sum_basic_currency))

    # 2. Check if such collection (log) exists, belongs to sender and if collection is not deleted (=="active")
    client = MongoClient()
    db = client.CBB
    if collection_name in db.collection_names():
        try: # If such collection exists for creator_id
            log_info = db[collection_name].find_one({"log": "info"})
            if log_info["creator_id"] != creator_id:
                response = {"status": "error", "payload": "You don't have a log named '{}'".format(collection_name)}
                return response

            if log_info["log_status"] == "inactive":
                response = {"status": "error", "payload": "Log has been deleted"}
                return response
        except Exception as error:
            response = {"status": "error", "payload": error}
            return response

    else:
        response = {"status": "error", "payload": "Log not found"}
        return response

    # 3. Check if user1 and/or user2 belong to active_users (the 1st document in collection, log_info)
    log_info = db[collection_name].find_one({"log": "info"})
    active_users = log_info["active_users"]
    our_users = ""
    for x in range(len(users)):
        if x == 0:
            our_users += users[x]
        else:
            our_users += ", " + users[x]
    if user1 not in active_users and (user2 != "" and user2 not in active_users):
        response = {"status": "error",
                    "payload": "Sorry, who are {} and {}? Can't find them in our user list ({})".format(user1, user2, our_users)}
        return response
    if user1 not in active_users:
        response = {"status": "error", "payload": "Sorry, who is {}? Can't find him/her in our user list ({})".format(user1, our_users)}
        return response
    if user2 != "" and user2 not in active_users:
        response = {"status": "error",
                    "payload": "Sorry, who is {}? Can't find him/her in our user list ({})".format(user2, our_users)}
        return response

    # 4. If currency != basic (for eg., UAH), convert to basic currency
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

    # 5. Calculate what users get in this transaction
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
    #print("log: " + str(log))

    # 6. Prepare document to be inserted to DB
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

    # 7. Insert document into DB
    add_payment_action_id = db[collection_name].insert_one(add_payment_action).inserted_id

    # 8. Final Ok response
    response = {"status": "ok", "payload": add_payment_action_id}

    return response

##################### TESTING ##############################################
creator_id = myinput1["originalRequest"]["data"]["message"]["from"]["id"]
users = ['Tim', 'Dan', 'Ann']
#print(create_log(creator_id, users))

collection_name = "chi-horse-260218"
print(add_payment(myinput1, collection_name))

#print(delete_log(collection_name, 123))