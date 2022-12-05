from faker import Faker
import pandas as pd
import os
import datetime
import random
from nltk.corpus import names
import nltk
import gender_identifier

from lookups import *

myData = Faker()

DATA_SET_SIZE = 500
SOURCE_SYSTEM_NAME = "Python_Generation_script"

personRows = []

def rand_mariatal_status():
    return random.choice(marital_statuses)


for person in range(DATA_SET_SIZE):
    pkey = 'Python_GS'+str(myData.ean13())
    personRows.append(
        {
        'id': pkey, 
        'souce_system': SOURCE_SYSTEM_NAME, 
        'first_name' : myData.first_name(), 
        'middle_name': None, 
        'last_name' : myData.last_name(), 
        'full_name': None,  
        'prefix': None, 
        'suffix': None, 
        'gender': None,
        'email': myData.email(), 
        'phone_number': myData.phone_number(), 
        'address_line_1': myData.street_address(),
        'address_line_2': None,
        'city': myData.city(), 
        'state': myData.state(), 
        'zip_code': myData.zipcode(),
        'marital_status': rand_mariatal_status(),
        'birth_date': myData.date_of_birth(),
        }
    )

    gender = gender_identifier.name_gender(personRows[person]['first_name'])
    # print(gender,personRows[person]['first_name'])
    if gender == 'male':
        personRows[person]['gender'] = random.choice(gender_data) 
    else:
        personRows[person]['gender'] = random.choice(gender_data) 
    if myData.boolean():
        if gender == 'male':
            personRows[person]['prefix'] = random.choice(male_prefix_data)
        else:
            personRows[person]['prefix'] = random.choice(female_prefix_data)
    
    if myData.boolean():
        personRows[person]['suffix'] = myData.suffix()
    
    if myData.boolean():
        name_gender = False
        name = None
        while not name_gender:
            name = myData.first_name()
            name_gender = True if gender_identifier.name_gender(name) == gender else False    
        personRows[person]['middle_name'] = name
        personRows[person]['full_name'] = str(personRows[person]['first_name']) + ' ' + str(random.choice([name, name[0], str(name[0]+'.')])) + ' ' + str(personRows[person]['last_name'])
    else:
        personRows[person]['full_name'] = personRows[person]['first_name'] + ' ' + personRows[person]['last_name']

personDF = pd.DataFrame(personRows, columns=['id', 'souce_system', 'first_name', 'middle_name', 'last_name', 'full_name', 'prefix', 'suffix', 'gender', 'email', 'phone_number', 'address_line_1', 'address_line_2', 'city', 'state', 'zip_code', 'marital_status', 'birth_date'])
print(personDF.head())

name_genderDF = pd.DataFrame(personRows, columns=['first_name', 'gender'])


path = './SampleDataFiles'
if not os.path.exists(path):
    os.makedirs(path)

file_path_name = 'SampleDataFiles/SAMPLE(SourceSystem-{})(size-{}Rows)-{}.csv'.format(SOURCE_SYSTEM_NAME, DATA_SET_SIZE, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')).replace(':', '-')
personDF.to_csv(str(file_path_name), index=False, quotechar='"', quoting=1)
#name_genderDF.to_csv(str('sampleDataFiles/name_gender.csv'), index=False, quotechar='"', quoting=1)

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

