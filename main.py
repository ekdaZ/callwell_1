import pandas as pd

df = pd.read_excel('book.xlsx')

# For iteration:
# for index, row in df.iterrows():
#     print(row['Number'])

print(df.loc[df['Network'] == 'EE'])

# print(df[['Number', 'Network']])