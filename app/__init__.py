from flask import Flask

app = Flask(__name__)
from app import routes
from config import Config
app.config.from_object(Config)
