from app import db
import sqlalchemy as sa
import sqlalchemy.orm as so
from datetime import datetime, timezone
import app.models as models

class Post(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    body: so.Mapped[str] = so.mapped_column(sa.String(140))
    data: so.Mapped[datetime] = so.mapped_column(index=True, default=sa.func.now())
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(models.Usuario.id), index=True)
    author: so.Mapped[models.Usuario] = so.relationship(back_populates='posts')