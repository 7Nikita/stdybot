import utility
from os import getenv
from flask import Flask
from flask import request
from flask import jsonify

from flask_sslify import SSLify


app = Flask(__name__)
sslify = SSLify(app)


STDY_TOKEN = getenv('STDY_TOKEN')
URL = 'https://api.telegram.org/bot{}/'.format(STDY_TOKEN)


@app.route('/{}'.format(STDY_TOKEN), methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        utility.write_json(r)
        return jsonify(r)
    return '<h1>Bot start page</h1>'


if __name__ == '__main__':
    app.run()
