from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world!' + 5  # Triggers a type error


if __name__ == '__main__':
    # Our app would've run on 127.0.0.1:5000 by default.
    app.run(host='0.0.0.0', port=8001, debug=True)
