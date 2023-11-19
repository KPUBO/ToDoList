import sqlalchemy as sa
from sqlalchemy.sql.functions import now

from core.base_classes.base_model import Base


class Plan(Base):
    __tablename__ = 'Plan'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.String, nullable=False)
    plan_date = sa.Column(sa.DateTime, nullable=True)
    done_mark = sa.Column(sa.Boolean, default=False, nullable=True)

    created_on = sa.Column(sa.DateTime, server_default=now(), nullable=True)
    done_datetime = sa.Column(sa.DateTime, nullable=True)
