from flask import Flask

from sql_chars import sql_chars_api

DEBUG = True
HOST = 'localhost'
PORT = 8000

app = Flask(__name__)
app.register_blueprint(sql_chars_api)


@app.route('/')
def hello_world():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)
