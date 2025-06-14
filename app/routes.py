from flask import render_template
from app import app

@app.route('/index')
@app.route('/')
def index():
    username = "Екатерина Мотос"
    news=[
        "Дельфины перестали удовлетворять своих самок. Теперь они перешли на ваших детей...",
        "Павел Техник скончался сегодня в своей квартире в Дубае",
        "СТРАНА УЖАСНУЛАСЬ, УВИДЕВ ЧТО СТАЛО С АЛИШЕРОМ МОРГЕНШТЕРНОМ ПОСЛЕ ГОДА В РЕХАБЕ",
        "УЧЁНЫЕ ТВЕРДЯТ: СТАЛИН НЕ ЕЛ ДЕТЕЙ НА ЗАВТРАК! ОН ЕЛ ИХ НА УЖИН..."
    ]
    return render_template('index.html',
                           username=username,
                           news=news)

@app.route('/albums/<int:album_number>')
def albums(album_number):
    return (f"This is {album_number} album")