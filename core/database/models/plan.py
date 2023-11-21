import datetime

import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.sql.functions import func

from core.base_classes.base_model import Base


class Plan(Base):
    __tablename__ = 'plan'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    done_mark = sa.Column(sa.Boolean, default=False, nullable=True)
    plan_date = sa.Column(sa.DateTime, nullable=True, default=None)
    #expired = sa.Column(sa.Boolean, nullable=True, default=False)
    created_on = sa.Column(sa.DateTime, default=func.now(), nullable=False)

    @orm.validates('plan_date')
    def validate_expiration(self, key, value):
        if value <= datetime.datetime.now():
            raise ValueError(f'Планируемая дата должна быть в будущем')
        return value


