"""
    Base terminal command manager.

    Define terminal commands here to run actions
"""
from flask.ext.script import Manager, Server
from flask.ext.sqlalchemy import SQLAlchemy
from system.init import initialize_app

app = initialize_app()

app.config.update(
    FACEBOOK_CONSUMER_KEY='259154491127882',
    FACEBOOK_CONSUMER_SECRET='c5b9a2e1e25bfa25abc75a9cd2af450a',
    SECRET_KEY='9as8d18g3jksaf791odoshdakjsdag19u',
    DEBUG=True
)

manager = Manager(app)

manager.add_command('runserver', Server(host='127.0.0.1'))

if __name__ == "__main__":
    manager.run()
