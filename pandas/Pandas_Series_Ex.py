import pandas as pd
import numpy as np
# #  1. Create Series from List

s = pd.Series([10, 20, 30])
# print(s)

# #  Creates a simple Series from a list. Each list element becomes a value in the Series, and Pandas automatically assigns default integer indices starting from 0 to each value.

# #  2. Custom Index

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
# print(s)

# #  You can assign custom labels to Series elements instead of default numeric indices. This helps create more meaningful data representations using string-based or specific identifiers.

# #  3. Access Element by Index

s = pd.Series([100, 200, 300])
print(s[1])

# #  Elements in a Pandas Series can be accessed using numeric indexing similar to  lists. so, index 1 returns the second value of the Series.


# #  4. Slicing Series


s = pd.Series([5, 10, 15, 20, 25])
# print(s[1:4])

# #  like  lists, Series supports slicing. This extracts a subseries from index 1 to index 3 (4 is exclusive), helping in analyzing parts of data.

# #  5. Create Series from Dictionary


d = {'a': 1, 'b': 2, 'c': 3}
s = pd.Series(d)
# print(s)

# #  Creating a Series from a dictionary automatically uses the dictionary keys as indices and values as Series data. It's useful for converting structured key-value pairs into Series.

# #  6. Series with NaN


s = pd.Series([1, np.nan, 3, np.nan])
# print(s)

# #  A Series can include missing or undefined values, represented by NaN (Not a Number). Pandas uses np.nan to denote missing data in numerical Series.

# #  7. Check for NaN

s = pd.Series([1, np.nan, 3])
# print(s.isnull())

# #  The isnull() method returns a boolean Series indicating which values are NaN. It helps identify missing data for further analysis or cleaning.

# #  8. Replace NaN

s = pd.Series([1, np.nan, 3])
# print(s.fillna(0))

# #  Missing values (NaN) can be replaced with specified values using fillna(). This is useful in preprocessing and handling incomplete datasets before applying operations.

# #  9. Mathematical Operation

s = pd.Series([1, 2, 3])
# print(s * 10)

# #  Pandas Series supports vectorized operations. Multiplying a Series by 10 multiplies each element without using loops, which is fast and efficient for large datasets.

# #  10. Series from Scalar

s = pd.Series(100, index=[0, 1, 2, 3])
# print(s)

# #  A single value can be broadcasted across multiple indices using a scalar. It creates a constant Series with repeated values for all given indices.

# #  11. Series Data Type
s = pd.Series([1.5, 2.5, 3.5])
# print(s.dtype)

# #  Use .dtype to check the data type of Series elements. It's useful to confirm if data is integer, float, string, or another type for processing.

# #  12. Series Size
s = pd.Series([10, 20, 30, 40])
# print(s.size)

# #  The size attribute returns the number of elements in the Series. It's helpful for quickly knowing how much data you're working with in a Series.

# #  13. Head of Series
s = pd.Series(range(1, 11))
# print(s)

# print(s.head(3))

# #  head() displays the first few elements of a Series. It’s handy for previewing data, especially in large Series or when loading datasets.


# #  14. Tail of Series
s = pd.Series(range(1, 11))
# print(s.tail(2))

# #  tail() is used to view the last few elements of the Series. Like head(), it helps inspect ending values quickly during data analysis.

# #  15. Series Name
s = pd.Series([10, 20, 30], name="Marks")
# print(s)

# #  Assigning a name to the Series gives it an identity, which is useful for labeling during visualization, exporting, or combining Series into a DataFrame.

# #  16. Series to List
# s = pd.Series([10, 20, 30])
# # print(s.tolist())

# #  Converts Series to a  list using tolist(). It helps when Pandas features are not needed, or when interacting with non-Pandas-based functions.

# #  17. Apply Function

s = pd.Series([1, 2, 3])
# print(s.apply(lambda x: x))

# #  apply() lets you apply custom functions to each element of the Series. It is powerful for transforming or computing new values from existing data.

# #  18. Boolean Indexing
s = pd.Series([10, 25, 30, 5])
# print(s[s > 20])

# #  Boolean indexing filters data based on conditions. Here, it selects only values greater than 20, useful for quick filtering or conditional analysis.

# #  19. Sort Series

s = pd.Series([30, 10, 20])
# print(s.sort_values())

# #  sort_values() arranges Series elements in ascending order. It’s useful for ordering data to identify minimum, maximum, or prepare for visualization.

# #  20. Unique Values
s = pd.Series([1, 2, 2, 3, 3, 3])
# print(s.unique())

# #  unique() returns distinct values from a Series, removing duplicates. It's useful for identifying the range of values, checking categories, or data validation.


# # 21. Check Series Index


s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
# print(s.index)


# #  Explanation: The index attribute returns the labels (indexes) of the Series. Useful when you want to inspect or modify index values during data manipulation.



# # 22. Rename Index


s = pd.Series([1, 2, 3], index=['x', 'y', 'z'])
s.index = ['a', 'b', 'c']
# print(s)


# #  Explanation: You can directly assign a new list to the index property to rename existing indices, which helps in organizing or re-labeling your data.



# # 23. Drop Value by Index


s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
# print(s.drop('b'))


# #  Explanation: The drop() method removes an element by its label, allowing you to filter out specific values when cleaning or reshaping the Series.



# # 24. Check Value Existence


s = pd.Series([1, 2, 3])
# print(21 in s.values)


# #  Explanation: You can check whether a value exists in a Series using the in keyword with .values, which returns a boolean result (True or False).



# # 25. Check Index Existence


s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
# print('b' in s)


# #  Explanation: You can check whether an index label exists in the Series using the in keyword directly. It’s useful for safe access or conditional checks.



# # 26. Count Non-NaN Values


s = pd.Series([1, 2, np.nan])
# print(s.count())


# #  Explanation: The count() method counts only non-null values in the Series. It's different from size, and is useful for checking data completeness.



# # 27. Value Counts


s = pd.Series([1, 2, 2, 3,1, 3, 3,2,2])
# print(s.value_counts())
# print(s.count())



# #  Explanation: Returns frequency counts of unique values in the Series. It's useful in analyzing categorical or repeated data patterns for statistics or visualizations.



# # 28. Series Mean


s = pd.Series([10, 20, 30])
# print(s.mean())


# #  Explanation: Calculates the arithmetic average of all numeric values in the Series. Commonly used in statistical analysis, especially for performance or trend evaluations.



# # 29. Series Median


s = pd.Series([10, 20, 30])
# print(s.median())


# #  Explanation: Returns the middle value of the Series after sorting. Useful for understanding central tendency when data may contain outliers affecting the mean.



# # 30. Series Standard Deviation


s = pd.Series([10, 20, 30])
# print(s.std())


# #  Explanation: Measures how much data deviates from the mean. Useful for detecting data variability and assessing stability in numeric Series.



# # 31. Series Describe


s = pd.Series([10, 20, 30])
# print(s.describe())


# #  Explanation: Summarizes key statistics (count, mean, std, min, max, quartiles) for the Series. Ideal for quick numeric overview and data exploration.



# # 32. Replace Value


s = pd.Series([10, 20, 30])
# print(s.replace(20, 200))


# #  Explanation: Replaces a specific value with a new one using replace(). Very useful in data cleaning and normalization.



# # 33. Clip Series


s = pd.Series([5, 15, 25])
print(s.clip(lower=10, upper=20))


# #  Explanation: Restricts values within given bounds. Values below lower are set to lower; above upper are set to upper. Used in data normalization and error handling.



# # 34. Map with Dictionary


s = pd.Series(['cat', 'dog'])
# print(s.map({'cat': 'meow', 'dog': 'bark'}))


# #  Explanation: map() replaces or transforms values using a dictionary or function. It's very useful in categorical value transformation or labeling.



# # 35. Convert to Numpy Array


s = pd.Series([1, 2, 3])
# print(s.to_numpy())


# #  Explanation: Converts Series to a NumPy array. Helps when using NumPy operations or integrating with libraries that require NumPy inputs.



# # 36. Add Two Series


s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])
# print(s1 + s2)


# #  Explanation: Series support element-wise arithmetic operations. Adding two Series of the same length adds their respective values, aligning by index.



# # 37. Align Series with Different Index


s1 = pd.Series([1, 2], index=['a', 'b'])
s2 = pd.Series([3, 4], index=['b', 'c'])
# print(s1 + s2)


# #  Explanation: Series align automatically by index during arithmetic. If an index doesn't match, the result is NaN for that index. Helps merge overlapping data correctly.



# # 38. String Methods


s = pd.Series(['apple', 'banana', 'cherry'])
# print(s.str.upper())


# #  Explanation: Use .str accessor to apply string methods to each element. Enables string transformation like upper(), lower(), replace(), etc., similar to Python strings.



# # 39. Filter Using Condition


s = pd.Series([5, 10, 15, 20])
# print(s[s % 2 == 0])


# #  Explanation: Boolean indexing with custom conditions helps filter data based on logic. Here, it extracts only even numbers using modulo operator.



# # 40. Reset Series Index


s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
s_reset = s.reset_index(drop=True)
print(s_reset)


# #  Explanation: reset_index() resets the index to default integers. Useful when reindexing after filtering or sorting and you want to remove custom labels.


