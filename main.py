from flask import Flask
from urls import setup_routing

app = Flask(__name__)
setup_routing(app)
