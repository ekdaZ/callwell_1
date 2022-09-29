import pandas as pd

df = pd.read_excel('book.xlsx')

# For iteration:
for index, row in df.iterrows():
    if len(str(row['Number'])) < 11:
        v = df.iloc[index]
        
        # print(v)
        w = v.loc['Number']
        w = '44' + str(w)
        df.loc[[index],'Number'] = int(w)
        


# print(df.loc[df['Network'] == 'EE'])

# print(df[['Number', 'Network']])
df.to_excel('modified.xlsx', index = False)