from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from flask_marshmallow import Marshmallow

login_manager=LoginManager()
db=SQLAlchemy()
migrate=Migrate()
ma=Marshmallow()