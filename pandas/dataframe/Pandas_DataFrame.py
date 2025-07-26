import pandas as pd
import numpy as np

# # 1. Create a DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)
# print(data)
# print(f'DataFrame:\n{df}')

# # 2. Read a CSV file
# df = pd.read_csv('C:\Krishna\Python\Examples\Movieratingdata3.csv')
df = pd.read_csv('C:/Krishna/Python/Examples/Movieratingdata3.csv')
print(df)


# # 3. Write a DataFrame to a CSV file
# df.to_csv('output.csv', index=False)
# print(x)

# # 4. Display first 2 rows
# print(f'First 2 rows:\n{df.head(2)}')

# # 5. Display last 2 rows
# print(f'Last 2 rows:\n{df.tail(2)}')

# # 6. Get DataFrame summary
# print(f'Description:\n{df.describe()}')

# # 7. Get DataFrame info
# df.info()

# # 8. Select a column
# print(f'Column A:\n{df["MOVIE_ID"]}')

# # 9. Select multiple columns
# print(f'Selected Columns:\n{df[["MOVIE_ID", "MOVIE_TITLE"]]}')

# # 10. Select a row by index
# print(f'Row 1:\n{df.iloc[1]}')

# 11. Select a row by label
# print(f'Row 1 (Label):\n{df.loc[1]}')

# # 12. Filter rows
# filtered_df = df[df['RATING'] > 8]
# print(f'Filtered DataFrame:\n{filtered_df}')

# # 13. Add a new column
# df['MOVIE_INFO'] = df['MOVIE_TITLE'] + df['GENRES']
# print(f'Updated DataFrame:\n{df}')

# # 14. Drop a column
# df = df.drop(columns=['MOVIE_INFO'])
# print(f'DataFrame after dropping column:\n{df}')

# # 15. Sort by column
sorted_df = df.sort_values(by='RATING', ascending=False)
print(f'Sorted DataFrame:\n{sorted_df}')

# # 16. Group by a column and sum
# df_grouped = df.groupby('USER_ID').sum()
# print(f'Grouped DataFrame:\n{df_grouped}')

# # 17. Find unique values
# unique_values = df['PRODUCTION_YEAR'].unique()
# print(f'Unique values in A: {unique_values}')

# # 18. Replace values
# df['RATING'] = df['RATING'].replace(111, 5)
# print(f'DataFrame with replaced values:\n{df}')

# # 19. Fill missing values
# df.fillna(0, inplace=True)

# # 20. Drop missing values
# df.dropna(inplace=True)

# # 21. Merge two DataFrames
# df2 = pd.DataFrame({'USER_ID': [10, 2], 'E': [100, 200]})
# merged_df = pd.merge(df, df2, on='USER_ID', how='inner')
# print(f'Merged DataFrame:\n{merged_df}')

# # 22. Pivot table
# pivot = df.pivot_table(values='USER_ID', index='RATING', aggfunc=np.sum)
# print(f'Pivot Table:\n{pivot}')

# # 23. Apply function to column
# df['R'] = df['A'].apply(lambda x: x*2)
# print(f'DataFrame after applying function:\n{df}')

# # 24. Reset index
# df_reset = df.reset_index(drop=True)
# print(f'Reset Index:\n{df_reset}')

# # 25. Set a new index
# df.set_index('RATING', inplace=True)
# print(f'DataFrame with new index:\n{df}')


# fname laname course 
# abc    nnn    cpp 
# bbb    iiii   pppp
# bb     hhhhh  ooooo