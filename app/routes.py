from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/albums/<int:album_number>')
def albums(album_number):
    return (f"This is {album_number} album")