from flask import (
    Flask, request, abort, render_template, redirect, url_for
)
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

from app.models import Base, User, Location, VisitLog
from app.forms import UserForm
from app import sql_play1 as ss


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.sqlite3'

# ORM instance
# To access the session object: db.session
db = SQLAlchemy(app)
db.Model = Base


@app.route('/', methods=['GET', 'POST'])
def home():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(username=form.data.get('username'))
        form.populate_obj(user)
        try:
            ss.add(db.session, user)
        except IntegrityError:
            db.session.rollback()
            form.username.errors.append('Username already exists!')
        else:
            return redirect(url_for('show_users'))
    return render_template('welcome.html', form=form)


@app.route('/add/<username>/')
def add_user(username):
    user = User(username=username)

    try:
        user = ss.add(db.session, user)
    except IntegrityError:
        # Always issue a rollback when a transaction fails
        db.session.rollback()
        return 'Username {} already exists!'.format(username)

    return 'Hello world, {}'.format(user.username)


@app.route('/delete/<int:user_id>/')
def delete_user(user_id):
    user = db.session.query(User).get(user_id)
    try:
        ss.delete(db.session, user)
        return 'Deleted!'
    except:
        abort(404)


@app.route('/show/')
def show_users():
    return '{}'.format([
        {i.id: i.username}
        for i in db.session.query(User).all()
    ])


if __name__ == '__main__':
    app.run()
