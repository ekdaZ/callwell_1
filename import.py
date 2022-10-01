import phonenumbers
from phonenumbers import carrier

phNumber = open('yang.txt')
print(phNumber)

for ph in phNumber:
    print(carrier.name_for_number(phonenumbers.parse(str(ph),None),'en')) 
