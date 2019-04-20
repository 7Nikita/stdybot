import re
import worker
import pymongo
import utility
import requests
from os import getenv
from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from multiprocessing import Process
from command_system import command_list


app = Flask(__name__)
utility.load_modules()

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['stdybot']


update_process = Process(target=worker.update_information)
update_process.start()


STDY_TOKEN = getenv('STDY_TOKEN')
URL = 'https://api.telegram.org/bot{}/'.format(STDY_TOKEN)


@app.route('/')
def start_page():
    return render_template('landing.html')


@app.route('/{}'.format(STDY_TOKEN), methods=['POST', 'GET'])
def webhook():
    if request.method == 'POST':
        r = request.get_json()
        for command in command_list:
            for regular in command.keys:
                if re.match(regular, r['message']['text']) is not None:
                    send_message(r['message']['chat']['id'], command.process(r))
                    return jsonify(r)
        send_message(r['message']['chat']['id'], 'unknown command')
        utility.write_json(r)
        return jsonify(r)
    return render_template('landing.html')


def send_message(chat_id, text):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()


if __name__ == '__main__':
    app.run()
