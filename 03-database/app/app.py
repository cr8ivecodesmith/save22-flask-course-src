from flask import Flask, request, abort
from flask.ext.sqlalchemy import SQLAlchemy

from app.models import Base, User, Location, VisitLog


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.sqlite3'
db = SQLAlchemy(app)
db.Model = Base


@app.route('/add/<username>/')
def add_user(username):
    from app import sql_play
    user = User(username=username)
    sql_play.add(db.session, user)
    return 'Hello world, {}'.format(user.username)

@app.route('/delete/<int:user_id>/')
def delete_user(user_id):
    from app import sql_play
    user = db.session.query(User).get(user_id)
    try:
        sql_play.delete(db.session, user)
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
