from app import create_app
from flask_script import Manager

# from app.models import Users, Pitches, Categories, Comments, Reactions

app = create_app('production')
manager = Manager(app)
# manager.add_command('server', Server)

# @manager.shell
# def make_shell_context():
#     return dict(app=app, db=db, users=Users, pitches=Pitches, categories=Categories, comments=Comments,
#                 reactions=Reactions)
#
#
# @manager.command
# def test():
#     import unittest
#     tests = unittest.TestLoader().discover('test')
#     unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
