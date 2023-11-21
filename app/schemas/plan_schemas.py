from datetime import datetime

from pydantic import BaseModel
from pydantic.v1 import validator

from core.helpers.datetime_helper import DateTimeHelper


class PlanResponseSchema(BaseModel):
    id: int
    name: str
    done_mark: bool | None
    plan_date: datetime | None
    created_on: datetime | None

    @validator('plan_date')
    def parse_timestamp(cls, value):
        return DateTimeHelper.to_datetime(value)

    @validator('created_on')
    def parse_created_on(cls, value):
        return DateTimeHelper.to_datetime(value)

    class Config:
        json_encoders = {
            datetime: DateTimeHelper.to_datetime_minutes
        }


class PlanRequestSchema(BaseModel):
    name: str
    plan_date: datetime

    # plan_date: Optional[datetime] = Field(None)

    @validator('plan_date')
    def parse_timestamp(cls, value):
        return DateTimeHelper.to_str(value)

    class Config:
        json_encoders = {
            datetime: DateTimeHelper.to_datetime_minutes
        }


class PlanUpdateSchema(BaseModel):
    name: str
    done_mark: bool | None
