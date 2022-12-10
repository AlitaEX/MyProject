from flask import current_app
from flask_login import UserMixin
import jwt

from app import db, login


@login.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


# 收藏品10/27
# collection = db.Table('collection',
#                       db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
#                       db.Column('followed_id', db.Integer, db.ForeignKey('user.id')),
# )


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False) # len=20
    email = db.Column(db.String(120), unique=True, nullable=False)
    avatar_img = db.Column(db.String(120), default='/static/assets/default-avatar.jpg', nullable=False)
    # 10/27
    # followed = db.relationship(
    #     'User', secondary=collection,
    #     primaryjoin=(collection.c.follower_id == id),
    #     secondaryjoin=(collection.c.followed_id == id),
    #     backref=db.backref('followers', lazy=True), lazy=True
    # )

    def __repr__(self):
        return '<User %r>' % self.username

    def generate_reset_password_token(self):
        return jwt.encode({'id': self.id}, current_app.config['SECRET_KEY'], algorithm='HS256')

    # 解碼token,檢測id
    @staticmethod
    def check_reset_password_token(token):
        try:
            decode = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            return User.query.filter_by(id=decode['id']).first()
        except:
            return None