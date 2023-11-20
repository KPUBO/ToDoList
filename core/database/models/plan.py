import sqlalchemy as sa
from sqlalchemy.sql.functions import func

from core.base_classes.base_model import Base


class Plan(Base):
    __tablename__ = 'plan'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    done_mark = sa.Column(sa.Boolean, default=False, nullable=True)
    created_on = sa.Column(sa.DateTime, default=func.now(), nullable=False)
