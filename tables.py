from sqlalchemy import Table, Column, Integer, String, Boolean
from database import metadata_obj

tasks_table = Table(
    'tasks',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('title', String(length=32), nullable=False),
    Column('description', String(length=255), nullable=True),
    Column('completed', Boolean, nullable=False, default=False)
)
