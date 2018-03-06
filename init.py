from pymongo import MongoClient

############# Documents inserted to DB "CBB" ############

# Example of document in "clients" collection
ourclient = {
  "channel": "telegram",
  "user_id": 178180819,
  "first_name": "Iurii",
  "logs": [
    "kappa-bat-280218",
    "zeta-beaver-260218"
  ],
  "log_last_used": "kappa-bat-280218"
}

###################################################################

# 1. Create a Mongo DB called "CBB" (for CommonBalanceBot)
try:
  client = MongoClient()
  db = client.CBB

  # 2. Create collection "clients" to store info about logs for each user ID
  clients = db["clients"]

  client_insert_id = clients.insert_one(ourclient).inserted_id
  print("Client {} ({}) inserted successfully, _id: {}".format(ourclient["first_name"], ourclient["user_id"], client_insert_id))

except Exception as error:
  print("Error: {}".format(error))


#################### TEMP ############################################

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
    for payment in payments:
        balance_data = payment["total_balance"]