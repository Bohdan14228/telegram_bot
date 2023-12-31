from datetime import datetime

from sqlalchemy import *

metadate1 = MetaData()

roles = Table(
    'roles',
    metadate1,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('permission', JSON),
)

users = Table(
    'users',
    metadate1,
    Column('id', Integer, primary_key=True),
    Column('email', String, nullable=False),
    Column('username', String, nullable=False),
    Column('password', String, nullable=False),
    Column('registered_at', TIMESTAMP, default=datetime.utcnow),
    Column('role_id', Integer, ForeignKey('roles.id')),
)
