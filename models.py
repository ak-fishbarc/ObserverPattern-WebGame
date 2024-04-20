from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from time import time
import jwt


def create_user_model(db):

    class User(UserMixin, db.Model):
        id: Mapped[int] = mapped_column(primary_key=True)
        username: Mapped[str] = mapped_column(String(16), index=True, unique=True)
        email: Mapped[str] = mapped_column(String(120), index=True)
        password_hashed = mapped_column(String(256))
        verified = mapped_column(Boolean(False))

        def set_password(self, password):
            self.password_hashed = generate_password_hash(password)

        def check_password(self, password):
            return check_password_hash(self.password_hashed, password)

        def verify(self):
            self.verified = True

        def get_reset_password_token(self, app, expires_in=600):
            return jwt.encode(
                {'reset_password': self.id, 'exp': time() + expires_in},
                app.config['SECRET_KEY'], algorithm='HS256'
            )

        @staticmethod
        def verify_reset_password_token(app, db, token):
            try:
                id = jwt.decode(token, app.config['SECRET_KEY'],
                                algorithms=['HS256'])['reset_password']
            except:
                return
            return db.session.get(User, id)

        def __repr__(self):
            return "<Username: %r>" % self.username

    return User


