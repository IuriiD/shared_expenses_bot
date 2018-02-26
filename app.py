# webhook only for TestBot

from flask import Flask, request, make_response, jsonify
import ast # TestBot
import functions_CBB

app = Flask(__name__)

# ###################### Decorators #########################################
@app.route('/')
def index():
    return 'Webhooks for chatbots Plotbot and FoodCompositionChatBot'

@app.route('/webhook', methods=['POST'])
def webhook():
    # Get request parameters
    req = request.get_json(silent=True, force=True)
    action = req.get('result').get('action')
    print(str(req))

    # CommonBalanceBot - add new payment
    if action == "commonbalancebot-add_payment":
        functions_CBB.add_payment(req)
        ourspeech = functions_CBB.balance("all")
        res = functions_CBB.commonbalancebot_speech(ourspeech, action, req['result']['contexts'])

    # CommonBalanceBot - show balance
    elif action == "commonbalancebot-balance":
        user = req.get('result').get('parameters').get('user')
        if user == "":
            user = "all"
        ourspeech = functions_CBB.balance(user)
        res = functions_CBB.commonbalancebot_speech(ourspeech, action, req['result']['contexts'])

    # CommonBalanceBot - show statement
    elif action == "commonbalancebot-statement":
        ourspeech = functions_CBB.statement()
        res = functions_CBB.commonbalancebot_speech(ourspeech, action, req['result']['contexts'])

    # CommonBalanceBot - get json
    elif action == "commonbalancebot-getjson":
        ourspeech = 'hello'
        #print(str(req))
        res = functions_CBB.commonbalancebot_speech(ourspeech, action, req['result']['contexts'])

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