from datetime import datetime

from pydantic import BaseModel, ConfigDict


class AdvertsCounterSchema(BaseModel):
    count: int
    time: datetime

    model_config = ConfigDict(from_attributes=True)
