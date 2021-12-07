from faker import Faker
import pandas as pd
import os
import datetime
import json

myData = Faker()

DATA_SET_SIZE = 20
SOURCE_SYSTEM_NAME = "Desktop_Test_Flatfile"


# ---------- Person DF ----------
personRows = []

for person in range(DATA_SET_SIZE):
    pkey = 'PerK'+str(myData.ean13())
    personRows.append({'pkey': pkey,
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
                       'zip_code': myData.zipcode(),})
    
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


# ---------- Event DF ----------
event_rows = []

for event in range(10):
    event_rows.append({'pkey': 'EveK'+str(myData.ean13()), 'souce_system': SOURCE_SYSTEM_NAME, 'event_name': 'IRONMAN 70.3', 'event_description': myData.text()})

eventDF = pd.DataFrame(event_rows, columns=['pkey', 'souce_system', 'event_name', 'event_description'])


# ---------- Sub Event DF ----------
sub_event_rows = []

for sub_event in range(10):
    sub_event_rows.append({'pkey': 'SbeK'+str(myData.ean13()), 
                           'souce_system': SOURCE_SYSTEM_NAME,
                           'parent_eventid': eventDF.iloc[sub_event]['pkey'],
                           'sub_event_name': "SubEvent IRONMAN 70.3", 
                           'venue': myData.city(),})

sub_eventDF = pd.DataFrame(sub_event_rows, columns=['pkey', 'souce_system', 'parent_eventid', 'sub_event_name', 'venue'])


# ---------- Registration DF ----------
registration_rows = []

for registration in range(DATA_SET_SIZE):
    #create a random int from 0 to 10
    rand_event_id = myData.random_int(0, 9)
    registration_rows.append({'pkey': 'RegK'+str(myData.ean13()),
                              'souce_system': SOURCE_SYSTEM_NAME,
                              'personid': personDF.iloc[registration]['pkey'],
                              'eventid': eventDF.iloc[rand_event_id]['pkey'], 
                              'sub_eventid': sub_eventDF.iloc[rand_event_id]['pkey'], 
                              'registration_date': myData.date(pattern="%Y-%m-%d"), 
                              'registration_status': 'Registered',})

registrationDF = pd.DataFrame(registration_rows, columns=['pkey', 'souce_system', 'personid', 'eventid', 'sub_eventid', 'registration_date', 'registration_status'])

# ---------- Results DF ----------
result_rows = []

for result in range(DATA_SET_SIZE):
    #create a random int from 0 to 10
    rand_event_id = myData.random_int(0, 9)
    result_rows.append({'pkey': 'ResK'+str(myData.ean13()),
                        'souce_system': SOURCE_SYSTEM_NAME,
                        'personid': personDF.iloc[result]['pkey'],
                        'eventid': eventDF.iloc[rand_event_id]['pkey'], 
                        'sub_eventid': sub_eventDF.iloc[rand_event_id]['pkey'], 
                        'registration_number': myData.ean13(),})

resultsDF = pd.DataFrame(result_rows, columns=['pkey', 'souce_system', 'personid', 'eventid', 'sub_eventid', 'registration_number'])


# ---------- Creates File Dir ----------

path = './SampleDataFiles'
if not os.path.exists(path):
    os.makedirs(path)

#------------ Export to CSV ------------

# file_path_name = "SampleDataFiles/Ironman_Sample_Relational_Dataset_(SourceSystem-{})(size-{}Rows)-{}.csv".format(SOURCE_SYSTEM_NAME, DATA_SET_SIZE, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")).replace(':', '-')
# personDF.to_csv(str(file_path_name), index=False, quotechar='"', quoting=1)


# --------- Export to JSON ---------------
with open('file.json', 'w') as file:
    json.dump({ "buy": L1, "sell": L2}, file)


# -------- Faker Library Functions --------

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

