from datetime import datetime

from pydantic import BaseModel


class PlanResponseSchema(BaseModel):
    id: int
    name: str
    done_mark: bool | None
    created_on: datetime | None

    class Config:
        orm_mode: True


class PlanRequestSchema(BaseModel):
    name: str

    class Config:
        orm_mode: True


class PlanUpdateSchema(BaseModel):
    name: str
    done_mark: bool | None
