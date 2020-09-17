import pandas as pd
import sqlite3

def read_database(path):
    connection = sqlite3.connect(path)
    return pd.read_sql("SELECT * FROM weather",connection)
    




