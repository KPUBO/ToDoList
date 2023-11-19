from fastapi import APIRouter, Depends
from starlette import status

from app.services.plan_service import PlanService

plan_router = APIRouter(
    prefix='/plan_router',
    tags=["Plan"]
)

@plan_router.get(
    '/plans',
    status_code= status.HTTP_200_OK
)
async def get_plan_by_id(
        plan_id: int,
        service: PlanService = Depends()
):
    return await service.find_by_id(plan_id)