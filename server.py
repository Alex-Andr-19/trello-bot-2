from flask import Flask, request, abort
import json

app = Flask(__name__)

user_token = ''

@app.route('/authorize', methods=['POST'])
def authorize():
    print(json.loads(request.text)['user_token'])
    return 'success', 200

@app.route('/webhook', methods=['POST','HEAD'])
def webhook():
    if request.method == 'POST':
        print(json.dumps(
            request.json,
            sort_keys=True, 
            separators=(",", ": "), 
            ensure_ascii=False)
        )

        if request.json.action.type == 'removeMemberFromCard':
            return 'removeMemberFromCard', 200
        elif request.json.action.type == 'updateCard':
            return 'updateCard', 200
        elif request.json.action.type == 'addMemberToCard':
            return 'addMemberToCard', 200
        elif request.json.action.type == 'commentCard':
            return 'commentCard', 200
        elif request.json.action.type == 'updateCard':
            return 'updateCard', 200




        return 'success', 200
    elif request.method == 'HEAD':
        print('connect')
        return 'success', 200
if __name__ == '__main__':
    app.run()