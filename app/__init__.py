from flask import Flask
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)   # (template_folder='./')設定 templates 資料夾位置就是當前執行檔
app.config.from_object(Config)  # 重要 一定要在SQLALCHEMY實例化對像前面

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
mail = Mail(app)

login = LoginManager(app)
login.login_view = 'login'
login.login_message = '請先登入'
login.login_message_category = 'Info'

from app.routes import *
from app import run