from datetime import timedelta
from typing import Sequence

from fastapi import APIRouter

from tracker.schemas import AdvertsCounterSchema


router = APIRouter(
    prefix="/tracker",
    tags=["avito tracker"],
)


@router.post("/add")
async def create_request_for_adverts(
    query: str,
    region: str,
) -> int:
    pass


@router.get("/stat")
async def get_statistics_adverts(
    id: int,
    period: timedelta,
) -> Sequence[AdvertsCounterSchema]:
    pass
