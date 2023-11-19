from fastapi import APIRouter

from app.routes.plan_router import plan_router

routes = APIRouter()

routes.include_router(plan_router)