from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta,engine

user =Table("users",meta,
    Column('id',Integer, primary_key=True),
    Column("name",String(50)),
    Column('password',String(50))
    )

meta.create_all(engine)