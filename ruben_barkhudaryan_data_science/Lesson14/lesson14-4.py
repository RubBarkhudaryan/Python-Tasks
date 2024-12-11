print("Working with datatypes.")
print("Binary format - sql")

import sqlite3 as sql
import pandas as pd

conn = sql.connect("DataSets/bike_share.db")

c = conn.cursor()

data = pd.read_csv(
    "DataSets/bike_share_UCS_2_LE_BOM.tsv", encoding="utf_16_le", sep="\t"
)


c.execute("CREATE TABLE IF NOT EXISTS RENTALS(Date, Hour, Qty)")

conn.commit()

data.to_sql("RENTALS", conn, if_exists="replace")


# conn.close()
