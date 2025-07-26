
import pandas as pd
a = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(a)
# print()
# c:\Krishna\Python\Examples\More Practice\PYTHON\PYTHON\Pandas\Movieratingdata3.csv


a = pd.DataFrame({10: [1, 2, 3], 11: [4, 5, 6], 12: [7, 8, 9]})
# print(a)

b = pd.DataFrame([{'Maths': 90, 'Sci': 80, 'Phy': 78},
                  {'Maths': 56, 'Sci': 67, 'Phy': 88}], index=[11, 22])
# print(b)


x = pd.Series([1, 2, 3, 4, 5, 6, 7])
y = pd.Series([8, 7, 6, 5, 4, 3, 2])

df = pd.DataFrame({"One": x, "Two": y})
# print() 
# print(df)


l1 = ['One', 'Two', 'Three', 'Four'] 
ab = pd.Series([1, 2, 3, 4], index= ['Five', 'Six', 'Seven', 'Eight'])
# print(ab)


ab = pd.Series([1, 2, 3, 4], index=[11, 12, 13, 14])

cd = pd.Series([5, 6, 7, 8], index=[11,12,13,14])
df1 = pd.DataFrame({'Maths': ab, 'Science': cd})
# print()
print(df1)
