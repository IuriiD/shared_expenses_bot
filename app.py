# webhook only for TestBot

from flask import Flask, request, make_response, jsonify
import ast # TestBot

app = Flask(__name__)

# ###################### CommonBalanceBot Functions #########################
def add_payment(req):
    '''
        Function gets 1) info about transaction from JSON from webhook (user1=payer, user2(optinally)=receiver of
        direct payment, otherwise user1 pays for all (including him/herself), payment sum (in basic currency or other
        currency that has to be converted into basic currency) and 2) retrieves transaction log from txt file and
        updates it with a new transaction. Returns dictionary with transactions (log) which is saved in txt file
    '''
    # Get our log (txt file will be substituted with Mongo DB)
    with open("log.txt", "r+") as logfromtxt:
        log = ast.literal_eval(logfromtxt.read())

    BASIC_CURRENCY = 'UAH'

    # Exchange rates to be substituted with calls to some API
    usd_uah = 26.9
    eur_uah = 33.1

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
# ###################### CommonBalanceBot Functions END #####################

# ###################### Decorators #########################################
@app.route('/')
def index():
    return 'Webhooks for chatbots Plotbot and FoodCompositionChatBot'

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get request parameters
    req = request.get_json(silent=True, force=True)
    action = req.get('result').get('action')

    # CommonBalanceBot - add new payment
    if action == "commonbalancebot-add_payment":
        add_payment(req)
        ourspeech = balance("all")
        res = commonbalancebot_speech(ourspeech, action, req['result']['contexts'])

    # CommonBalanceBot - show balance
    elif action == "commonbalancebot-balance":
        user = req.get('result').get('parameters').get('user')
        if user == "":
            user = "all"
        ourspeech = balance(user)
        res = commonbalancebot_speech(ourspeech, action, req['result']['contexts'])

    else:
        # If the request is not of our actions throw an error
        res = {
            'speech': 'Something wrong happened',
            'displayText': 'Something wrong happened'
        }

    return make_response(jsonify(res))
# ###################### Decorators END ##############################

if __name__ == '__main__':
    #port = int(os.getenv('PORT', 5000))
    app.run(debug=False, host='0.0.0.0')#, port=port)