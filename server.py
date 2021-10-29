from flask import Flask, request, abort
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST','HEAD'])
def webhook():
    if request.method == 'POST':
        print(json.dumps(
            request.json,
            sort_keys=True, 
            indent=4, 
            separators=(",", ": "), 
            ensure_ascii=False)
        )
        return 'success', 200
    elif request.method == 'HEAD':
        print('connect')
        return 'success', 200
if __name__ == '__main__':
    app.run()