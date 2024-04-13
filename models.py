from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import generate_password_hash, check_password_hash


def create_user_model(db):

    class User(db.Model):
        id: Mapped[int] = mapped_column(primary_key=True)
        username: Mapped[str] = mapped_column(String(16), index=True, unique=True)
        email: Mapped[str] = mapped_column(String(120), index=True)
        password_hashed = mapped_column(String(256))

        def set_password(self, password):
            self.password_hashed = generate_password_hash(password)

        def check_password(self, password):
            return check_password_hash(self.password_hashed, password)

        def __repr__(self):
            return "<Username: %r>" % self.username

    return User


