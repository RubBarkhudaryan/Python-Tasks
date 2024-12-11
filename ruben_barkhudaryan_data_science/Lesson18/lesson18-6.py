print("Pandas: How to read write files")
print("Working with xml files")

import pandas as pd

df = pd.read_xml("s3://pmc-oa-opendata/oa_comm/xml/all/PMC1236943.xml",xpath=".//journal-meta")
print(df)
