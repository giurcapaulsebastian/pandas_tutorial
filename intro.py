from os import sep
import pandas as pd

#df = pd.read_csv("pokemon_data.csv")
#print(df.tail(3))

#df_xlsx = pd.read_excel("pokemon_data.xlsx")
#print(df_xlsx.head(3))

df = pd.read_csv('pokemon_data.txt', delimiter='\t')

#print(df.head(5))

### Read Headers
#print(df.columns)

### Read each column
#print(df['Name'].head(5))
#print(df[['Name','Type 1']].head(5))

### Read Each Row
#print(df.head(4))
#print(df.iloc[0:4])
# for index,row in df.iterrows():
#     print(index, row['Name'])
#print(df.loc[df['Type 1'] == "Fire"])

### Read a specific locatin (R,C)
print(df.iloc[2,1])

print(df.describe())