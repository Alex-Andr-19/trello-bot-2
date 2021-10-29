from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/webhook', methods=['POST','GET'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return 'success', 200
    elif request.method == 'GET':
        print('connect')
        return 'success', 200
if __name__ == '__main__':
    app.run()