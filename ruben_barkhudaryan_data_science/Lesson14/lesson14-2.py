print("Working with datatypes.")
print("Text format - html")

import pandas as pd

data_url = pd.read_html(
    r"https://en.wikipedia.org/w/index.php?" + "title=Solar_power&oldid=1022764141"
)

solar_PV_data = data_url[1]

print(solar_PV_data)
