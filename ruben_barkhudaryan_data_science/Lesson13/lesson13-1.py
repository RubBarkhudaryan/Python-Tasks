import pandas as pd

dog_food_orders = pd.read_excel(
    r"..\lessonfiles\dog_food_orders.xlsx", engine="openpyxl"
)

print(dog_food_orders)