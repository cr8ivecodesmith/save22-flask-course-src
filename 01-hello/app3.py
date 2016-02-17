from hashlib import md5
from flask import Flask, render_template, redirect, session, url_for


app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    session['user'] = 'Foo'
    return redirect(url_for('welcome'))


@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('welcome'))


app.secret_key = md5().hexdigest()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
