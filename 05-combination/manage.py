from flask.ext.script import Manager
from app.app import app, db  # get the `app` and `db` objects


manager = Manager(app)
app.config['DEBUG'] = True


if __name__ == '__main__':
    # Create the database (normally placed in a seperate module)
    from app import sql_play1 as ss
    db.session = ss.create_session(
        app.config['SQLALCHEMY_DATABASE_URI']
    )

    # Run the web app
    manager.run()
