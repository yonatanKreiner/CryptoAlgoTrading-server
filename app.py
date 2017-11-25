from flask import Flask, request
from pbClient import PushbulletClient
app = Flask(__name__)

pushbullet = PushbulletClient()

def __transact(agent, activity, coin, amount):
    event = activity + '- coin: ' + coin + ', amount: ' + amount
    pushbullet.push(agent, event)
    return agent + ': ' + event
 
@app.route('/sell/<agent>')
def sell(agent):
    coin = request.args.get('coin', '')
    amount = request.args.get('amount', '')
    return __transact(agent, 'sell', coin, amount)

@app.route('/buy/<agent>')
def buy(agent):
    coin = request.args.get('coin', '')
    amount = request.args.get('amount', '')
    return __transact(agent, 'buy', coin, amount)

@app.route('/keep-alive/<agent>')
def keep_alive(agent):
    print(agent + ' is alive')
    return agent + ' is alive'

@app.route('/')
def main():
    return 'Server is running'
