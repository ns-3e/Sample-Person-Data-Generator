import csv 
from faker import Faker

myData = Faker()

DATA_SET_SIZE = 100
df = {'first_name', 'last_name', 'full_name', 'prefix', 'suffix','email', 'phone_number', 'street_address', 'city', 'state', 'zip_code'}

# parser to get city state and zip code from address
# def parse_address(address):
#     address_list = address.split(', ')
#     print(address_list)
#     address_ln1 = address_list[0].split('\n')[0]
#     print(address_ln1)
#     city = address_list[0].split('\n')[1]
#     state = address_list[1].split(' ')[0]
#     zip_code = address_list[1].split(' ')[1]
#     return [address_ln1, city, state, zip_code]



for person in range(DATA_SET_SIZE):
    person = {'first_name' : myData.first_name(), 'middle_name': None, 'last_name' : myData.last_name(), 'prefix': None, 'suffix': None, 'email': myData.email(), 'phone_number': myData.phone_number(), 'street_address': myData.street_address(), 'city': myData.city(), 'state': myData.state(), 'zip_code': myData.zipcode()}
    
    if myData.boolean():
        person['prefix'] = myData.prefix()
    
    if myData.boolean():
        person['suffix'] = myData.suffix()
    
    if myData.boolean():
        person['middel_name'] = myData.first_name()
    
    print(person)



# --- Faker Functions ---
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
# print(myData.ean13())
# print(myData.ean8())

