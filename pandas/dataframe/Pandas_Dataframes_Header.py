from os import path
from typing import assert_type
import pandas as pd
path = "Movieratingdata1.csv"
df = pd.read_csv('Movieratingdata1.csv')
# print(df)

# df = pd.read_csv(path, names=["a", "b", "c", "d",
#                  "e", "f", "g", "h", "i", "j"])
# print(df)

# print(df.head(3))
# print(df.tail(4))
# print(df.info(4))
# print(df.describe())
# print(df.shape[0])
# print(df.shape[1])
# print(df.size)
# print(df.sample())
# print(df.loc[1:5, ['PRODUCTION_YEAR', 'MOVIE_TITLE']])
# print(df.iloc[0])
# df.fillna(method='bfill', limit=2)
# print(df)
# print("\n", df.replace({'MOVIE_ID': '[0-9]'}, 'm', regex=True))
