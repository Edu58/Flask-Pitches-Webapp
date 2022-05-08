from app import create_app, db
from flask_script import Manager, Server
from app.models import Users, Pitches, Categories, Comments, Reactions

app = create_app('development')
manager = Manager(app)
manager.add_command('server', Server)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, users=Users, pitches=Pitches, categories=Categories, comments=Comments,
                reactions=Reactions)


if __name__ == '__main__':
    manager.run()
