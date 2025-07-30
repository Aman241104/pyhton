from os import path
from typing import assert_type
import pandas as pd
path = "Movieratingdata3.csv"
df = pd.read_csv(path)
# print(df)
# print('\n', df['PRODUCTION_YEAR'] > 2015)
# print('\n', df['MOVIE_TITLE'] == 'Ironman')
# df1 = df[df['PRODUCTION_YEAR'] > 2015 | (df['MOVIE_TITLE'] == 'Ironman')]
# print('\n', df1)
