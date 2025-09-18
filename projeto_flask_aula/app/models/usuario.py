from app import db
import sqlalchemy as sa
import sqlalchemy.orm as so
from typing import Optional

class Usuario(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    telefone: so.Mapped[str] = so.mapped_column(sa.String(20))
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    posts: so.Mapped['Post']=so.relationship(back_populates='author')