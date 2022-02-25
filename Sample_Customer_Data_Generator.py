from faker import Faker
import pandas as pd
import os
import datetime

myData = Faker()

DATA_SET_SIZE = 50
SOURCE_SYSTEM_NAME = "Python_Generation_script"

personRows = []

for person in range(DATA_SET_SIZE):
    pkey = 'Python_GS'+str(myData.ean13())
    personRows.append(
        {
            'pkey': pkey, 
            'souce_system': SOURCE_SYSTEM_NAME, 
            'first_name' : myData.first_name(), 
            'middle_name': None, 
            'last_name' : myData.last_name(), 
            'full_name': None,  
            'prefix': None, 
            'suffix': None, 
            'email': myData.email(), 
            'phone_number': myData.phone_number(), 
            'street_address': myData.street_address(), 
            'city': myData.city(), 
            'state': myData.state(), 
            'zip_code': myData.zipcode()
        }
    )
    
    if myData.boolean():
        personRows[person]['prefix'] = myData.prefix()
    
    if myData.boolean():
        personRows[person]['suffix'] = myData.suffix()
    
    if myData.boolean():
        personRows[person]['middle_name'] = myData.first_name()
        personRows[person]['full_name'] = str(personRows[person]['first_name']) + ' ' + str(personRows[person]['middle_name']) + ' ' + str(personRows[person]['last_name'])
    else:
        personRows[person]['full_name'] = personRows[person]['first_name'] + ' ' + personRows[person]['last_name']

personDF = pd.DataFrame(personRows, columns=['pkey', 'souce_system', 'first_name', 'middle_name', 'last_name', 'full_name', 'prefix', 'suffix', 'email', 'phone_number', 'street_address', 'city', 'state', 'zip_code'])
print(personDF.head())


path = './SampleDataFiles'
if not os.path.exists(path):
    os.makedirs(path)

file_path_name = "SampleDataFiles/Sample_Customer_Data_(SourceSystem-{})(size-{}Rows)-{}.csv".format(SOURCE_SYSTEM_NAME, DATA_SET_SIZE, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")).replace(':', '-')
personDF.to_csv(str(file_path_name), index=False, quotechar='"', quoting=1)

# --- Faker Library Functions ---
# print(myData.name())
# print(myData.address())
# print(myData.street_address())
# print(myData.city())
# print(myData.state())
# print(myData.zipcode())
# print(myData.phone_number())
# print(myData.email())
# print(myData.company())
# print(myData.job())
# print(myData.text())
# print(myData.paragraph())
# print(myData.sentence())
# print(myData.word())
# print(myData.boolean())
# print(myData.date())
# print(myData.time())
# print(myData.iso8601())
# print(myData.date_time())
# print(myData.date_time_ad())
# print(myData.credit_card_expire())
# print(myData.credit_card_full())
# print(myData.credit_card_number())
# print(myData.credit_card_provider())
# print(myData.credit_card_security_code())
# print(myData.currency_code())
# print(myData.currency_name())
# print(myData.currency_symbol())
#print(myData.ean13())
# print(myData.ean8())

