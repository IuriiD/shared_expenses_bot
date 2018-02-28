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