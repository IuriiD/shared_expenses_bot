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

    # CommonBalanceBot - welcome
    if action == "commonbalancebot-welcome":
        req_for_uid = functions_CBB.check_for_logs(req)["payload"]
        ourspeech = functions_CBB.welcome_response(req_for_uid)["payload"]
        res = functions_CBB.commonbalancebot_speech(ourspeech, action, req['result']['contexts'])

    # CommonBalanceBot - create log
    elif action == "commonbalancebot-create_log":
        ourspeech = functions_CBB.create_log(req)["payload"]
        res = functions_CBB.commonbalancebot_speech(ourspeech, action, req['result']['contexts'])

    # CommonBalanceBot - delete log
    elif action == "commonbalancebot-delete_log":
        req_for_uid = functions_CBB.check_for_logs(req)["payload"]
        ourspeech = functions_CBB.delete_log_response(req_for_uid, req['result']['contexts'])
        res = functions_CBB.commonbalancebot_speech(ourspeech["payload"], action, ourspeech["contexts"])

    # CommonBalanceBot - delete log - deletion confirmed
    elif action == "commonbalancebot-delete_log-do_it":
        ourspeech = functions_CBB.delete_log(req)["payload"]
        res = functions_CBB.commonbalancebot_speech(ourspeech, action, req['result']['contexts'])

    # CommonBalanceBot - add new user
    elif action == "commonbalancebot-add_user":
        ourspeech = functions_CBB.add_user(req)["payload"]
        res = functions_CBB.commonbalancebot_speech(ourspeech, action, req['result']['contexts'])

    # CommonBalanceBot - remove user
    elif action == "commonbalancebot-delete_user":
        ourspeech = functions_CBB.delete_user(req)["payload"]
        res = functions_CBB.commonbalancebot_speech(ourspeech, action, req['result']['contexts'])

    # CommonBalanceBot - add new payment
    elif action == "commonbalancebot-add_payment":
        result = functions_CBB.add_payment(req)
        if result["status"] != "error":
            functions_CBB.update_balance(req)
            ourspeech = functions_CBB.balance(req)["payload"]
        else:
            ourspeech = result["payload"]
        res = functions_CBB.commonbalancebot_speech(ourspeech, action, req['result']['contexts'])

    # CommonBalanceBot - delete payment
    elif action == "commonbalancebot-delete_payment":
        ourspeech = functions_CBB.delete_payment(req)["payload"]
        functions_CBB.update_balance(req)
        res = functions_CBB.commonbalancebot_speech(ourspeech, action, req['result']['contexts'])

    # CommonBalanceBot - show balance
    elif action == "commonbalancebot-balance":
        functions_CBB.update_balance(req)
        user = req.get('result').get('parameters').get('user')
        if user == "":
            user = "all"
        ourspeech = functions_CBB.balance(req, user)["payload"]
        res = functions_CBB.commonbalancebot_speech(ourspeech, action, req['result']['contexts'])

    # CommonBalanceBot - show statement
    elif action == "commonbalancebot-statement":
        ourspeech = functions_CBB.statement(req)["payload"]
        res = functions_CBB.commonbalancebot_speech(ourspeech, action, req['result']['contexts'])

    # CommonBalanceBot - get json
    elif action == "commonbalancebot-getjson":
        ourspeech = 'hello'
        #print(str(req))
        res = functions_CBB.commonbalancebot_speech2(ourspeech, action, req['result']['contexts'])

    # CommonBalanceBot - taking user back to conversation
    elif action == "commonbalancebot-besidethepoint":
        ourspeech = functions_CBB.besidethepoint()["payload"]
        res = functions_CBB.commonbalancebot_speech(ourspeech, action, req['result']['contexts'])

    # CommonBalanceBot - display FAQ
    elif action == "commonbalancebot-faq":
        ourspeech = functions_CBB.faq()["payload"]
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