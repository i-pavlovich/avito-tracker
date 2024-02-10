import asyncio

from tracker.models import AdvertsCounter, RequestParams  # noqa
from database import Base, engine


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


asyncio.run(create_tables())
