from fastapi import APIRouter, Depends
from starlette import status

from app.schemas.plan_schemas import PlanResponseSchema, PlanRequestSchema, PlanUpdateSchema
from app.services.plan_service import PlanService

plan_router = APIRouter(
    prefix='/plan_router',
    tags=["Plan"]
)


@plan_router.get(
    '/plans',
    response_model=list[PlanResponseSchema],
    status_code=status.HTTP_200_OK
)
async def get_all_plans(
        service: PlanService = Depends()
):
    return await service.find_all()


@plan_router.get(
    '/plans/{plan_id}',
    response_model=PlanResponseSchema,
    status_code=status.HTTP_200_OK
)
async def get_plan_by_id(
        plan_id: int,
        service: PlanService = Depends()
):
    return await service.find_by_id(plan_id)


@plan_router.post(
    '/plans',
    # response_model=PlanResponseSchema,
    status_code=status.HTTP_201_CREATED
)
async def insert_plan(
        request: PlanRequestSchema,
        service: PlanService = Depends()
):
    return await service.create(request)


@plan_router.put(
    '/plans/{plan_id}',
    response_model=PlanResponseSchema,
    status_code=status.HTTP_200_OK
)
async def update_plan_by_id(
        plan_id: int,
        request: PlanUpdateSchema,
        service: PlanService = Depends()
):
    return await service.update(plan_id, request=request)


@plan_router.delete(
    '/plans/{plan_id}',
    response_model=PlanResponseSchema,
    status_code=status.HTTP_200_OK
)
async def delete_plan_by_id(
        plan_id: int,
        service: PlanService = Depends()
):
    return await service.delete(plan_id)
