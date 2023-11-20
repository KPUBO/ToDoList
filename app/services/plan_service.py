from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.plan_repository import PlanRepository
from core.base_classes.base_service import BaseService
from core.database.session import get_async_session


class PlanService(BaseService):

    def __init__(self, session: AsyncSession = Depends(get_async_session)) -> None:
        super().__init__(session)
        self.plan_repository = PlanRepository(session)

    async def find_all(self):
        return await self.plan_repository.find_all()

    async def find_by_id(self, plan_id):
        return await self.plan_repository.find_by_id(plan_id)

    async def create(self, request):
        plan = await self.plan_repository.create(request)
        await self.session.commit()
        return plan

    async def update(self, plan_id, request):
        return await self.plan_repository.update(request, plan_id)

    async def delete(self, plan_id):
        plan = await self.plan_repository.delete(plan_id)
        await self.session.commit()
        return plan

