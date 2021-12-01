import csv 
import random
from faker import Faker

myData = Faker()

DATA_SET_SIZE = 100
df = {'First Name', 'Last Name', 'Email', 'Phone Number', 'Street Address', 'City', 'State', 'Zip Code'}

# parser to get city state and zip code from address
def parse_address(address):
    address_list = address.split(', ')
    address_ln1 = address_list[0].split('\n')[0]
    city = address_list[0].split('\n')[1]
    state = address_list[1].split(' ')[0]
    zip_code = address_list[1].split(' ')[1]
    return [address_ln1, city, state, zip_code]

addy = myData.address()
parse_address(addy)
print("parser: ", parse_address(addy))
print("Full Address: ", addy)
print("City: ", parse_address(addy)[1])
print("State: ", parse_address(addy)[2])
print("Zip Code: ", parse_address(addy)[3])




# --- Faker Functions ---
# print(myData.name())
# print(myData.address())
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

