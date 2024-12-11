print("Working with Datatypes")
print("binary format-sql")
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///DataSets/bike_share.db"
)
with engine.connect() as conn, conn.begin():
    data = pd.read_sql_table("RENTALS", conn)
print(data)
