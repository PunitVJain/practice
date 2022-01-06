# pandas
import pandas as pd

data = {"first_name": ["Punit", "Ram"], "last_name": ["Jain", "Charan"], "mobile_no": ["9876543298", "8967452389"]}

df = pd.DataFrame(data)
#print(tuple(df.columns))


lst = [1, 2,3 ,4, 5]

df1 = pd.DataFrame(lst)
#print(type(df1))