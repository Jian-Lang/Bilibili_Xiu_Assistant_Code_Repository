# encoding:utf-8
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from apps.models.user_model import *
from apps.models.following_up import *
from apps.models.friends import *
from apps import create_app
from exits import db

app = create_app()
manager = Manager(app = app)
migrate = Migrate(app = app, db = db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.run(host='0.0.0.0',ssl_context=("6794555_www.zhangwenning.top.pem","6794555_www.zhangwenning.top.key"))
