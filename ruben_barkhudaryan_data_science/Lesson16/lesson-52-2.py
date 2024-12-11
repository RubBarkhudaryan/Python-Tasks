print("Working with Datatypes")
print("binary format-sql")
import pandas as pd
from sqlalchemy import create_engine

dataset = pd.DataFrame(
    {
        "Names": ["Davit", "Armen", "Karen", "Suren"],
        "DOB": ["10/01/2009", "08/16/2008", "9/22/2007", "6/10/2008"],
    }
)
# print(dataset)
engine = create_engine("sqlite://", echo=False)
dataset.to_sql("Employee_Data", con=engine)
with engine.connect() as con:
    con.execute("SELECT * FROM Employee_Data").fetchall()
