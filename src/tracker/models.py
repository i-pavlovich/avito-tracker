from database import Base
from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class AdvertsCounter(Base):
    __tablename__ = "adverts_counters"

    id: Mapped[int] = mapped_column(primary_key=True)
    query_params_id: Mapped[int] = mapped_column(
        ForeignKey("requests_params.id", ondelete="CASCADE")
    )
    count: Mapped[int]
    date: Mapped[datetime]


class RequestParams(Base):
    __tablename__ = "requests_params"

    id: Mapped[int] = mapped_column(primary_key=True)
    query: Mapped[str]
    region: Mapped[str]
