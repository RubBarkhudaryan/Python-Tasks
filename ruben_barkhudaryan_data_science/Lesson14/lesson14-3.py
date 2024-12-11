print("Working with datatypes.")
print("Text format - html")

import pandas as pd

data_url = pd.read_csv(r"DataSets\thyroid.tsv", encoding="utf_16_le", sep="\t")

print(data_url.head(10))
