from flask import Flask, request
app = Flask(__name__)

@app.route('/sell/<agent>')
def sell(agent):
    coin = request.args.get('coin', '')
    amount = request.args.get('amount', '')
    return 'sell- agent: ' + agent + ',coin: ' + coin + ', amount: ' + amount

@app.route('/buy/<agent>')
def buy(agent):
    coin = request.args.get('coin', '')
    amount = request.args.get('amount', '')
    return 'buy- agent: ' + agent + ',coin: ' + coin + ', amount: ' + amount

@app.route('/')
def main():
    return 'Server is running'
