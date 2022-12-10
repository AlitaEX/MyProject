from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileRequired, FileAllowed
from app.models import User


# 但是驗證的任務交给 wtforms,要提一下的是,Email驗證錯誤的话,是pip install wtforms版本過高
# 解決方法有2個
# No.1 : 安裝低版本的,直接Google
# No.2 : 直接 pip install email-validator,也就是另外安裝 email-validator


class RegisterForm(FlaskForm):

    username = StringField('使用者名稱', validators=[DataRequired(), Length(min=6, max=20)])
    email = StringField('電子信箱', validators=[DataRequired(), Email()])
    password = PasswordField('密碼', validators=[DataRequired(), Length(min=7, max=20)])
    confirm = PasswordField('請再次輸入密碼', validators=[DataRequired(), EqualTo('password')])
    # recaptcha = RecaptchaField() # 網路金鑰有問題
    submit = SubmitField('註冊')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('使用者名稱已存在')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('電子信箱已存在')


class LoginForm(FlaskForm):

    username = StringField('使用者名稱', validators=[DataRequired(), Length(min=6, max=20)])
    password = PasswordField('密碼', validators=[DataRequired(), Length(min=7, max=20)])
    remember = BooleanField('記住密碼')
    submit = SubmitField('登入')


class PasswordResetRequestForm(FlaskForm):

    email = StringField('電子信箱', validators=[DataRequired(), Email()])
    submit = SubmitField('送出資料')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError('電子信箱不存在')


class ResetPasswordForm(FlaskForm):

    password = PasswordField('密碼', validators=[DataRequired(), Length(min=7, max=20)])
    confirm = PasswordField('請再次輸入密碼', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('重設密碼')


class UploadPhotoForm(FlaskForm):
    photo = FileField('Image', validators=[FileRequired(), FileAllowed(['png', 'jpg', 'jpeg', 'gif'], 'Images only!')])
    submit = SubmitField('更換頭貼')