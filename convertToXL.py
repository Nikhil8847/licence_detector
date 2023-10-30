# pip install openpyxl

import pandas as pd
import sqlite3

connection = sqlite3.connect("mydatabase.db")


query = "SELECT * from cars Where number_plate != 'None'"

df = pd.read_sql(query, connection)

df.to_excel("data.xlsx")