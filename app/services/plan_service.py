from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.plan_repository import PlanRepository
from core.base_classes.base_service import BaseService
from core.database.session import get_async_session


class PlanService(BaseService):

    def __init__(self, session: AsyncSession = Depends(get_async_session)) -> None:
        super().__init__(session)
        self.plan_repository = PlanRepository(session)


    async def find_by_id(self, plan_id):
        return await self.plan_repository.find_by_id(plan_id)

    async def create(self, request):
        return await self.plan_repository.create(request)

    async def update(self, plan_id, request):
        return await self.plan_repository.update(request, plan_id)

