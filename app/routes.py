from flask import render_template
from app import app

@app.route('/index')
@app.route('/')
def index():
    username = "matya kotos"
    return render_template('index.html',
                           username = username)

@app.route('/albums/<int:album_number>')
def albums(album_number):
    return (f"This is {album_number} album")