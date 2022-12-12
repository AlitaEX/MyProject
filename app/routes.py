import os
from app import app, bcrypt, db
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, login_required, current_user, logout_user
from werkzeug.utils import secure_filename

from app.forms import *
from app.models import User

from app.email import send_reset_password_mail
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# 推薦
@app.route('/recommend')
def recommend():
    return render_template('recommend.html')


@app.route("/")
@login_required
def index():
    # count_collection = len(current_user.collection), count_collection=count_collection
    return render_template('index.html')


@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    form = UploadPhotoForm()
    if form.validate_on_submit():
        f = form.photo.data
        if f.filename == '':
            flash('沒有選擇檔案', category='danger')
            return render_template('edit_profile.html', form=form)
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join('app', 'static', 'assets', filename))
            current_user.avatar_img = '/static/assets/' + filename
            db.session.commit()
            return redirect(url_for('index', username=current_user.username))
    return render_template('edit_profile.html', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = bcrypt.generate_password_hash(form.password.data)    # password加密
        email = form.email.data
        user = User(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        flash('註冊成功', category='success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        # 檢查是否匹配
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            # 用戶存在、密碼匹配
            login_user(user, remember=remember)
            flash('登入成功', category='Info')
            if request.args.get('next'):
                next_page = request.args.get('next')
                return redirect(next_page)
            return redirect(url_for('index'))
        flash('用戶不存在或密碼錯誤', category='danger')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/reset_password_request', methods=['GET', 'POST'])
def send_password_reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = PasswordResetRequestForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        token = user.generate_reset_password_token()
        send_reset_password_mail(user, token)
        flash('寄送成功, 請至您的信箱收取信件', category='Info')
    return render_template('reset_password_request.html', form=form)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user = User.check_reset_password_token(token)
        if user:
            user.password = bcrypt.generate_password_hash(form.password.data)
            db.session.commit()
            flash('密碼已重設, 請用新密碼登入', category='Info')
            return redirect(url_for('login'))
        else:
            flash('用戶不存在', category='Info')
            return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)


@app.route('/collection')
@login_required
def collection():
    list = ['fuck','you']
    return render_template('collection.html', content=list)


# 飲料html
@app.route('/a_nice_holiday')
def a_nice_holiday():
    return render_template('a_nice_holiday.html')


@app.route('/oolong_tea_project')
def oolong_tea_project():
    return render_template('oolong_tea_project.html')


@app.route('/do_it_myself')
def do_it_myself():
    return render_template('do_it_myself.html')


@app.route('/health_future_tea')
def health_future_tea():
    return render_template('health_future_tea.html')


@app.route('/mateas')
def mateas():
    return render_template('mateas.html')


@app.route('/see_joy')
def see_joy():
    return render_template('see_joy.html')


@app.route('/eight_yo')
def eight_yo():
    return render_template('eight_yo.html')


@app.route('/richa')
def richa():
    return render_template('richa.html')


@app.route('/wu_win')
def wu_win():
    return render_template('wu_win.html')


@app.route('/insir')
def insir():
    return render_template('insir.html')


@app.route('/blike')
def blike():
    return render_template('blike.html')


@app.route('/chos_drinks')
def chos_drinks():
    return render_template('chos_drinks.html')


@app.route('/yogurt_master')
def yogurt_master():
    return render_template('yogurt_master.html')


@app.route('/the_little_things')
def the_little_things():
    return render_template('the_little_things.html')


@app.route('/true_boss')
def true_boss():
    return render_template('true_boss.html')