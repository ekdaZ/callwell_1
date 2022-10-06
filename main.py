import pandas as pd
import phonenumbers
from phonenumbers.carrier import name_for_number


def traverse(filename):
    df = pd.read_excel(filename)
    temp_list = []
    for index, row in df.iterrows():
        if len(str(row['Number'])) < 11:
            v = df.iloc[index]
            w = v.loc['Number']
            search_up_data = '44' + str(w)
            df.loc[[index],'Number'] = int(search_up_data)
        z = df.iloc[index]
        x = z.loc['Number']
        search_up_google = '+' + str(x)

        
        phNumber = search_up_google
        new_carrier = name_for_number(phonenumbers.parse(phNumber,None),'en')
        
        temp_list.append(new_carrier)

    df['New Carrier'] = temp_list
    df.to_csv('modified.csv', index = False)