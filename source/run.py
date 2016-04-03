# -*- coding: utf-8 -*-

from flask.ext.script import Manager, Server
from mysite import app

manager = Manager(app)
manager.add_command("runserver",Server(host="127.0.0.1", port=5000))

@manager.command
def install():
    '''Installs all required packages.'''
    #os.system('pip install -U -r requirements.txt')


@manager.command
def build():
    """Builds the static files."""
    print("Freezing it up! Brr...")
    #freezer.freeze()  # Freezes the project to build/
    print('Copying CNAME...')
    #cname = os.path.join(HERE, 'CNAME')
    #shutil.copyfile(cname, os.path.join(build_dir, 'CNAME'))
    print('...done')

if __name__ == '__main__':
    #manager = Manager(app)
    #manager.add_command("runserver",Server(host="127.0.0.1", port=5000))
    manager.run()