from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Import routes di bawah agar tidak terjadi circular import
from app import routes