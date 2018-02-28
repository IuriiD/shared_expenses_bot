from pymongo import MongoClient

# 0. Create a Mongo DB called "CBB" and a test collection
client = MongoClient()
db = client.CBB
testcollection = db["actions-examples-25022018"]
testcollection.drop()

log_info = {
  'log': 'info',
  'log_status': 'active',
  'creator_id': 178180819,
  'active_users': ['Ann', 'Tim', 'Dan'],
  'initial_balance': {
    'Ann': 0,
    'Tim': 0,
    'Dan': 0
  }
}

create_log_action = {
  # '_id': 0, = creation date, used for sorting
  'creator_id': 178180819,
  'action_type': 'create_log', # all variants: 'create_log', 'delete_log', 'add_payment', 'modify_payment', 'delete_payment', 'add_user', 'delete_user'
}

delete_log_action = {
  # '_id': 0, = creation date, used for sorting
  'creator_id': 178180819,
  'users': ['Tim', 'Dan', 'Ann'],
  'action_type': 'delete_log', # all variants: 'create_log', 'delete_log', 'add_payment', 'modify_payment', 'delete_payment', 'add_user', 'delete_user'
  'total_balance': {
    'Ann': 0,
    'Tim': 0,
    'Dan': 0
  }
}

add_payment_action = {
  # '_id': 0, = creation date, used for sorting
  'creator_id': 178180819,
  'users': ['Tim', 'Dan', 'Ann'],
  'modified': {
    'status': False,
    'date': None
  },
  'deleted': {
    'status': False,
    'date': None
  },
  'action_type': 'add_payment', # all variants: 'create_log', 'delete_log', 'add_payment', 'modify_payment', 'delete_payment', 'add_user', 'delete_user'
  'transaction_balance': {
    'Ann': -179.33333333333334,
    'Tim': 358.66666666666663,
    'Dan': -179.33333333333334
  },
  'total_balance': {
    'Ann': -179.33,
    'Tim': 200.33,
    'Dan': -179.33
  },
  'who_paid': 'Tim',
  'who_received': 'all',
  'amount': 538.0
}

modify_payment_action = {
  # '_id': 0, = creation date, used for sorting
  'creator_id': 178180819,
  'users': ['Tim', 'Dan', 'Ann'],
  'modified': {
    'status': True,
    'date': '2018-02-23T10:24:59.404Z'
  },
  'deleted': {
    'status': False,
    'date': None
  },
  'action_type': 'modify_payment', # all variants: 'create_log', 'delete_log', 'add_payment', 'modify_payment', 'delete_payment', 'add_user', 'delete_user'
  'transaction_balance': {
    'Ann': -179.33333333333334, # some new data
    'Tim': 358.66666666666663, # some new data
    'Dan': -179.33333333333334 # some new data
  },
  'total_balance': {
    'Ann': -179.33,
    'Tim': 200.33,
    'Dan': -179.33
  },
  'who_paid': 'Tim', # some new data
  'who_received': 'all', # some new data
  'amount': 538.0 # some new data
}

delete_payment_action = {
  # '_id': 0, = creation date, used for sorting
  'creator_id': 178180819,
  'users': ['Tim', 'Dan', 'Ann'],
  'modified': {
    'status': False,
    'date': None
  },
  'deleted': {
    'status': True,
    'date': '2018-02-23T10:24:59.404Z'
  },
  'action_type': 'delete_payment', # all variants: 'create_log', 'delete_log', 'add_payment', 'modify_payment', 'delete_payment', 'add_user', 'delete_user'
  'transaction_balance': {
    'Ann': -179.33333333333334, # original data, 'soft-deletion'
    'Tim': 358.66666666666663, # original data, 'soft-deletion'
    'Dan': -179.33333333333334 # original data, 'soft-deletion'
  },
  'total_balance': {
    'Ann': -179.33, # original data, 'soft-deletion'
    'Tim': 200.33, # original data, 'soft-deletion'
    'Dan': -179.33 # original data, 'soft-deletion'
  },
  'who_paid': 'Tim', # original data, 'soft-deletion'
  'who_received': 'all', # original data, 'soft-deletion'
  'amount': 538.0 # original data, 'soft-deletion'
}

add_user_action = {
  # '_id': 0, = creation date, used for sorting
  'creator_id': 178180819,
  'users': ['Tim', 'Dan', 'Ann', 'Mike'],
  'action_type': 'add_user' # all variants: 'create_log', 'delete_log', 'add_payment', 'modify_payment', 'delete_payment', 'add_user', 'delete_user'
}

delete_user_action = { # only users with zero balance can be deleted
  # '_id': 0, = creation date, used for sorting
  'creator_id': 178180819,
  'users': ['Dan', 'Ann', 'Mike'],
  'action_type': 'delete_user' # all variants: 'create_log', 'delete_log', 'add_payment', 'modify_payment', 'delete_payment', 'add_user', 'delete_user'
}
result = testcollection.insert_many([log_info, create_log_action, add_payment_action, modify_payment_action, delete_payment_action, add_user_action, delete_user_action, delete_log_action])
