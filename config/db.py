from sqlalchemy import create_engine,MetaData

engine = create_engine("mysql+pymysql://JzHRx4IPZw:mpr7skAcJl@remotemysql.com:3306/JzHRx4IPZw")

meta = MetaData()

conn = engine.connect()