import utility
import requests
from os import getenv
from flask import Flask
from flask import request
from flask import jsonify


app = Flask(__name__)


STDY_TOKEN = getenv('STDY_TOKEN')
URL = 'https://api.telegram.org/bot{}/'.format(STDY_TOKEN)


@app.route('/')
def start_page():
    return '<h1> STDY Bot is online</h1>'


@app.route('/{}'.format(STDY_TOKEN), methods=['POST', 'GET'])
def webhook():
    if request.method == 'POST':
        r = request.get_json()
        utility.write_json(r)
        return jsonify(r)
    return '<h1>Bot start page</h1>'


def send_message(chat_id, text):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()


if __name__ == '__main__':
    app.run()
