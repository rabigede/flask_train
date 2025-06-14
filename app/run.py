from flask import Flask, render_template
from app.templates import *

app = Flask(__name__)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)


