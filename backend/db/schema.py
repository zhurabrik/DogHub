from sqlalchemy import Column, MetaData, Table, Integer
from sqlalchemy.dialects.postgresql import JSONB

metadata = MetaData()

templates_table = Table(
    "templates",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("meta", JSONB, nullable=False),
)
