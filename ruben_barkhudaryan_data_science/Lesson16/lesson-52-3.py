print("Working with Datatypes")
print("binary format-sql")
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite://", echo=False)
