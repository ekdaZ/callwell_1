import pandas as pd
import phonenumbers
from phonenumbers.carrier import name_for_number
import os


def traverse(filename):
    df = pd.read_excel('upload/' + filename + '.xlsx')
    temp_list = []
    print('MAIN CHECK')
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
    # # df.reset_index(drop =True, inplace=True)
    # # df.to_csv(r'BASIC_PATH + /modified_files\modified.csv'  ,index = False)
    df.to_csv(os.path.join('modified_files','improved_' + filename + '.csv'))