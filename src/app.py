from os import getenv
from flask import Flask

app = Flask(__name__)


URL = 'https://api.telegram.org/bot{}/'.format(getenv('STDY_TOKEN'))


@app.route('/')
def hello_world():
    return URL


if __name__ == '__main__':
    app.run()
