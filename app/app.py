from flask import Flask

# import Configuration fro config file
from config import Configuration

app = Flask(__name__)

# use the values from Configuration class
app.config.from_object(Configuration)
