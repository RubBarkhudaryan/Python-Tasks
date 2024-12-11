import pandas as pd

data_url = pd.read_html(r"https://en.wikipedia.org/wiki/Wind_power")

print(data_url)