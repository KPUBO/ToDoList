from sqlalchemy import select
from sqlalchemy.orm import query

from core.base_classes.base_repository import BaseRepository
from core.database.models import Plan


class PlanRepository(BaseRepository):

    def __init__(self, session):
        super().__init__(session, Plan)
        self.session = session



