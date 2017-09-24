from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

# import Configuration fro config file
from config import Configuration

app = Flask(__name__)

# use the values from Configuration class
app.config.from_object(Configuration)

# init database
db = SQLAlchemy(app)

# init flask-script
migrate = Migrate(app, db)
# imit flask-migrate
manager = Manager(app)
# add flask-migrate into flask-script
manager.add_command('db', MigrateCommand)
