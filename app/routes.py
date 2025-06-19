from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import userLoginForm


@app.route('/index')
@app.route('/')
def index():
    username = ""
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


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = userLoginForm()
    if form.validate_on_submit():
        flash(f"{form.login.data}, {form.password.data} успешно отправлено в военкомат")
        return redirect(url_for('index'))
    return render_template('login.html', form=form)