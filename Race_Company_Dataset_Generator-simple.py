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

# ---------- Results DF ----------
result_rows = []

for result in range(DATA_SET_SIZE):
    #create a random int from 0 to 10
    rand_event_id = myData.random_int(0, 2)
    result_rows.append({'result_pkey': 'ResK'+str(myData.ean13()),
                        'result_souce_system': SOURCE_SYSTEM_NAME,
                        'result_personid': personDF.iloc[result]['person_pkey'],
                        'result_eventid': str(myData.ean13())+'_e'+str(rand_event_id), 
                        'result_sub_eventid': str(myData.ean13())+'_se'+str(rand_event_id), 
                        'registration_number': str(myData.ean13())+'_reg'+str(rand_event_id),})

resultsDF = pd.DataFrame(result_rows, columns=['result_pkey', 'result_souce_system', 'result_personid', 'result_eventid', 'result_sub_eventid', 'registration_number'])



# ---------- Hierarchy relationship File Builder ----------

# add all hierarchy entities to this list in the order of decreasing precedence
Hierarchy_attribute_list = ["Event", "SubEvent", "Registration", "Result"]

hierarchy_rows = []
for record in range(DATA_SET_SIZE):
    cur_result = resultsDF.iloc[record] 
    #cur_registration = registrationDF.loc[(registrationDF.registration_pkey == cur_result['registration_number'])]
    hierarchy_rows.append({
        'instance_source_pkey': cur_result['result_personid'],
        'instance_description': str(cur_result['result_personid'])+" hierarchy instance",
        'instance_name': str(cur_result['result_personid'])+".hierarchy.instance",
        'instance_rootKey': cur_result['result_personid'],
        'instance_rootSystem': 'ns.vm.hierarchy-import',
        'PersonToResultParent_pkey': cur_result['result_personid'],
        'PersonToResultParent_sourceSystem': SOURCE_SYSTEM_NAME,
        'PersonToResultChild_pkey': cur_result['result_pkey'],
        'PersonToResultChild_sourceSystem': SOURCE_SYSTEM_NAME,
        'PersonToResult_sourcePkey': "Hkey_PtR_"+str(cur_result['result_pkey'])+"_"+str(record),
    })
hierarchyDF = pd.DataFrame(hierarchy_rows, columns=[
    'instance_source_pkey',
    'instance_description',
    'instance_name',
    'instance_rootKey',
    'instance_rootSystem',
    'PersonToResultParent_pkey',
    'PersonToResultParent_sourceSystem',
    'PersonToResultChild_pkey',
    'PersonToResultChild_sourceSystem',
    'PersonToResult_sourcePkey',
])
print(hierarchyDF.head())





# ---------- Creates File Dir ----------

path = './SampleDataFiles'
if not os.path.exists(path):
    os.makedirs(path)

file_path_name_csv = "SampleDataFiles/Ironman_Sample_Relational_Dataset_(SourceSystem-{})(size-{}Rows)-{}.csv".format(SOURCE_SYSTEM_NAME, DATA_SET_SIZE, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")).replace(':', '-')
file_path_name_json = "SampleDataFiles/Ironman_Sample_Relational_Dataset_(SourceSystem-{})(size-{}Rows)-{}.json".format(SOURCE_SYSTEM_NAME, DATA_SET_SIZE, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")).replace(':', '-')



# --------- Export to JSON ---------------

# data = {'person': person_data, 'event': event_data, 'sub_event': sub_event_data, 'registration': registration_data, 'result': result_data}
# data = {'person': personDF, 'event': eventDF, 'sub_event': sub_eventDF, 'registration': registrationDF, 'result': resultsDF}

path = './SampleDataFiles/DL_Ironman-{}'.format(datetime.datetime.now().strftime("%Y-%m-%d %H_%M"))
if not os.path.exists(path):
    os.makedirs(path)



# ------------ Export to CSV ------------

personDF.to_csv("{}/personData.csv".format(path),index=False, quotechar='"', quoting=1)
# eventDF.to_csv("{}/eventData.csv".format(path), index=False, quotechar='"', quoting=1)
# sub_eventDF.to_csv("{}/sub_eventData.csv".format(path), index=False, quotechar='"', quoting=1)
# registrationDF.to_csv("{}/registrationData.csv".format(path), index=False, quotechar='"', quoting=1)
resultsDF.to_csv("{}/resultData.csv".format(path), index=False, quotechar='"', quoting=1)
hierarchyDF.to_csv("{}/hierarchyData.csv".format(path), index=False, quotechar='"', quoting=1)


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

