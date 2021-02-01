from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from hello import UserMixin

mysql = SQLAlchemy()

class User(UserMixin, mysql.Model):
    id = mysql.Column(mysql.Integer, primary_key=True)
    username = mysql.Column(mysql.String(50), nullable=False)
    password = mysql.Column(mysql.String(200), nullable=False)
 
    def save(self):
        mysql.session.add(self)
        mysql.session.commit()

    def set_password(self, password):
        pass_hash = generate_password_hash(password)
        self.password = pass_hash

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Post(mysql.Model):
    id = mysql.Column(mysql.Integer, primary_key = True)
    body = mysql.Column(mysql.String(1000), nullable = False)
    user_id = mysql.Column(mysql.Integer, mysql.ForeignKey('user.id'), nullable = False)

