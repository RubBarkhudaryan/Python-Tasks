print("Working with datatypes.")

import pandas as pd

data_url = pd.read_html(
    r"https://en.wikipedia.org/w/index.php?" + "title=Solar_power&oldid=1022764141"
)

print(data_url)
