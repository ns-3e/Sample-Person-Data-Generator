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
    personRows.append({'person_pkey': pkey,
                       'person_souce_system': SOURCE_SYSTEM_NAME, 
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

personDF = pd.DataFrame(personRows, columns=['person_pkey', 'person_souce_system', 'first_name', 'middle_name', 'last_name', 'full_name', 'prefix', 'suffix', 'email', 'phone_number', 'street_address', 'city', 'state', 'zip_code'])
print("Preson Rows: \n", personRows)
print("Person DF: \n",personDF.head())


# ---------- Event DF ----------
event_rows = []

for event in range(10):
    event_rows.append({'event_pkey': 'EveK'+str(myData.ean13()), 'event_souce_system': SOURCE_SYSTEM_NAME, 'event_name': 'IRONMAN 70.3', 'event_description': myData.text()})

eventDF = pd.DataFrame(event_rows, columns=['event_pkey', 'event_souce_system', 'event_name', 'event_description'])

# ---------- Sub Event DF ----------
sub_event_rows = []

for sub_event in range(10):
    sub_event_rows.append({'sub_event_pkey': 'SbeK'+str(myData.ean13()), 
                           'sub_event_souce_system': SOURCE_SYSTEM_NAME,
                           'sub_event_parent_eventid': eventDF.iloc[sub_event]['event_pkey'],
                           'sub_event_name': "SubEvent IRONMAN 70.3", 
                           'venue': myData.city(),})

sub_eventDF = pd.DataFrame(sub_event_rows, columns=['sub_event_pkey', 'sub_event_souce_system', 'parent_eventid', 'sub_event_name', 'venue'])

# ---------- Registration DF ----------
registration_rows = []

for registration in range(DATA_SET_SIZE):
    #create a random int from 0 to 10
    rand_event_id = myData.random_int(0, 9)
    registration_rows.append({'registration_pkey': 'RegK'+str(myData.ean13()),
                              'registration_souce_system': SOURCE_SYSTEM_NAME,
                              'registration_personid': personDF.iloc[registration]['person_pkey'],
                              'registration_eventid': eventDF.iloc[rand_event_id]['event_pkey'], 
                              'registration_sub_eventid': sub_eventDF.iloc[rand_event_id]['sub_event_pkey'], 
                              'registration_date': myData.date(pattern="%Y-%m-%d"), 
                              'registration_status': 'Registered',})

registrationDF = pd.DataFrame(registration_rows, columns=['registration_pkey', 'registration_souce_system', 'registration_personid', 'registration_eventid', 'registration_sub_eventid', 'registration_date', 'registration_status'])

# ---------- Results DF ----------
result_rows = []

for result in range(DATA_SET_SIZE):
    #create a random int from 0 to 10
    rand_event_id = myData.random_int(0, 9)
    result_rows.append({'result_pkey': 'ResK'+str(myData.ean13()),
                        'result_souce_system': SOURCE_SYSTEM_NAME,
                        'result_personid': personDF.iloc[result]['person_pkey'],
                        'result_eventid': eventDF.iloc[rand_event_id]['event_pkey'], 
                        'result_sub_eventid': sub_eventDF.iloc[rand_event_id]['sub_event_pkey'], 
                        'registration_number': myData.ean13(),})

resultsDF = pd.DataFrame(result_rows, columns=['result_pkey', 'result_souce_system', 'result_personid', 'result_eventid', 'result_sub_eventid', 'registration_number'])







# personDF.set_index('pkey', inplace=True)
# eventDF.set_index('pkey', inplace=True)
# sub_eventDF.set_index('pkey', inplace=True)
# registrationDF.set_index('pkey', inplace=True)
# resultsDF.set_index('pkey', inplace=True)

# ---------- Creates File Dir ----------

path = './SampleDataFiles'
if not os.path.exists(path):
    os.makedirs(path)

file_path_name_csv = "SampleDataFiles/Ironman_Sample_Relational_Dataset_(SourceSystem-{})(size-{}Rows)-{}.csv".format(SOURCE_SYSTEM_NAME, DATA_SET_SIZE, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")).replace(':', '-')
file_path_name_json = "SampleDataFiles/Ironman_Sample_Relational_Dataset_(SourceSystem-{})(size-{}Rows)-{}.json".format(SOURCE_SYSTEM_NAME, DATA_SET_SIZE, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")).replace(':', '-')


#------------ Export to CSV ------------

# personDF.to_csv(str(file_path_name), index=False, quotechar='"', quoting=1)


# --------- Export to JSON ---------------

# data = {'person': person_data, 'event': event_data, 'sub_event': sub_event_data, 'registration': registration_data, 'result': result_data}
data = {'person': personDF, 'event': eventDF, 'sub_event': sub_eventDF, 'registration': registrationDF, 'result': resultsDF}

path = './SampleDataFiles/DL_Ironman-{}'.format(datetime.datetime.now().strftime("%Y-%m-%d %H_%M"))
if not os.path.exists(path):
    os.makedirs(path)

# create a data frame from the data
# df = pd.DataFrame(data)

# ------------ Export to JSON ------------

# personDF.to_json("{}/personData.json".format(path), orient='records')
# eventDF.to_json("{}/eventData.json".format(path), orient='records')
# sub_eventDF.to_json("{}/sub_eventData.json".format(path), orient='records')
# registrationDF.to_json("{}/registrationData.json".format(path), orient='records')
# resultsDF.to_json("{}/resultData.json".format(path), orient='records')


# ------------ Export to CSV ------------

personDF.to_csv("{}/personData.csv".format(path),index=False, quotechar='"', quoting=1)
eventDF.to_csv("{}/eventData.csv".format(path), index=False, quotechar='"', quoting=1)
sub_eventDF.to_csv("{}/sub_eventData.csv".format(path), index=False, quotechar='"', quoting=1)
registrationDF.to_csv("{}/registrationData.csv".format(path), index=False, quotechar='"', quoting=1)
resultsDF.to_csv("{}/resultData.csv".format(path), index=False, quotechar='"', quoting=1)



# file_path_name = "SampleDataFiles/Ironman_Sample_Relational_Dataset_(SourceSystem-{})(size-{}Rows)-{}.csv".format(SOURCE_SYSTEM_NAME, DATA_SET_SIZE, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")).replace(':', '-')
# personDF.to_csv(str(file_path_name), index=False, quotechar='"', quoting=1)


# file_path_name = "SampleDataFiles/Ironman_Sample_Relational_Dataset_(SourceSystem-{})(size-{}Rows)-{}.json".format(SOURCE_SYSTEM_NAME, DATA_SET_SIZE, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")).replace(':', '-')
# with open(file_path_name, 'w') as outfile:
#     json.dump(json_result, outfile)

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

