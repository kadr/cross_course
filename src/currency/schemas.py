from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel


class Currency(BaseModel):
    iso: str
    currency_name: str
    is_obsolete: bool
    create_at: float = datetime.now().timestamp()
    superseded_by: str | None = None
    currency_symbol: str | None = None
    currency_symbol_on_right: bool | None = None

    class Config:
        orm_mode = True


class CreateCurrency(Currency): ...


class GetCurrency(Currency):
    id: int


class CrossCourse(BaseModel):
    name: str
    course: float
    create_at: float = datetime.now().timestamp()

    class Config:
        orm_mode = True


class CreateCrossCourse(CrossCourse): ...


class GetCrossCourse(CrossCourse):
    id: int
