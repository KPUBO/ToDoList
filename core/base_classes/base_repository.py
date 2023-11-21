from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:
    def __init__(self, session: AsyncSession, model):
        self.session = session
        self.model = model

    async def find_by_id(self, item_id: int):
        query = await self.session.execute(
            select(self.model).where(self.model.id == item_id)
        )
        return query.scalar_one()

    async def find_all(self):
        query = await self.session.execute(
            select(self.model).order_by('id')
        )
        return query.scalars().all()

    async def create(self, request):
        stmt = self.model(**request.dict())
        self.session.add(stmt)
        return stmt

    async def update(self, request, item_id):
        stmt = await self.find_by_id(item_id)
        for field, value in request:
            setattr(stmt, field, value)
        await self.session.commit()
        return stmt

    async def delete(self, item_id):
        stmt = await self.session.execute(
            delete(self.model).where(self.model.id == item_id).returning(self.model)
        )
        return stmt.scalar_one()
