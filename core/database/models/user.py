import sqlalchemy as sa
from core.base_classes.base_model import Base


class User(Base):
    __tablename__ = 'User'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(50),  nullable=False)
    surname = sa.Column(sa.String(50), nullable=False)
    sex = sa.Column(sa.String, nullable=False)
    age = sa.Column(sa.Integer,  nullable=False)

