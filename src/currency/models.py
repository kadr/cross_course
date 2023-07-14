from datetime import datetime

import sqlalchemy
from sqlalchemy import Column, Integer, String, Boolean, Float

from src.database import Base

metadata = sqlalchemy.MetaData()

currency_table = sqlalchemy.Table(
    "currency",
    metadata,
    sqlalchemy.Column("id", Integer, primary_key=True),
    sqlalchemy.Column("iso", String(40), nullable=False, unique=True),
    sqlalchemy.Column("currency_name", String(100), nullable=False),
    sqlalchemy.Column("is_obsolete", Boolean(), nullable=False),
    sqlalchemy.Column("superseded_by", String(), nullable=True),
    sqlalchemy.Column("currency_symbol", String(), nullable=True),
    sqlalchemy.Column("currency_symbol_on_right", Boolean(), nullable=True),
    sqlalchemy.Column("create_at", Float(), default=datetime.now().timestamp())
)

cross_course_table = sqlalchemy.Table(
    "cross_course",
    metadata,
    sqlalchemy.Column("id", Integer, primary_key=True),
    sqlalchemy.Column("name", String(40), nullable=False, unique=True),
    sqlalchemy.Column("course", Float, nullable=False),
    sqlalchemy.Column("create_at", Float(), default=datetime.now().timestamp())
)


class Currency(Base):
    __tablename__ = "currency"

    id = Column(Integer, primary_key=True, index=True)
    iso = Column(String(40), nullable=False, unique=True)
    currency_name = Column(String(100), nullable=False)
    is_obsolete = Column(Boolean(), nullable=False)
    superseded_by = Column(String(), nullable=True)
    currency_symbol = Column(String(), nullable=True)
    currency_symbol_on_right = Column(Boolean(), nullable=True)
    create_at = Column(Float(), default=datetime.now().timestamp())


class CrossCourse(Base):
    __tablename__ = "cross_course"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(40), nullable=False, unique=True)
    course = Column(Float, nullable=False)
    create_at = Column(Float(), default=datetime.now().timestamp())
