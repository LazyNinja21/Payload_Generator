import json
from supp import *  
infile = 'payload.json'
filename = 'person.txt'

class Error(Exception):
    """Base class for other exceptions"""
    pass

class LargeValueError(Error):
    """Raised when the input value is too large"""
    pass

#To clear the file before use
open(filename, 'w').close()

#"a_dictionary = " + str_dictionary + "\n"

#Method to write the dictionary as json to a file
def payload_write(person_dict, val):
    val=val+1
    val = str(val)
    with open(filename, 'a') as json_file:
        #json_file.write("****************************\n")
        #json_file.write(str(val))
        json_file.write("\n************** "+ val +" **************\n")
        json.dump(person_dict, json_file,indent = 2)
        json_file.write("\n")

#Default payload
#person = '{"name": "", "age": 0}'

#Opening the json file to dump data as dictionary
with open(infile) as f:
  person_dict = json.load(f)

#User input for number of payload generation
while True:
    try:
        num = int(input("Enter the number of payloads you need: "))
        if (num>500):
            raise LargeValueError
        break
    except (TypeError,ValueError):
        print("Enter a valid value. The input should be an integer number")
    except LargeValueError:
        print("Please enter a value less than 100.")

#Functions to generate the number of payloads defined by user
def generate_us():
    i = 0 #Initializing value for the loop
    while (i<num):
        person_dict['Name'] = fake_us.name()
        person_dict['Age'] = random.randint(10, 80)
        person_dict['Address']['Address_L1'] = fake_us.street_address()
        person_dict['Address']['City'] = fake_us.city()
        person_dict['Address']['State'] = fake_us.state()
        person_dict['Address']['Country'] = 'US' #fake.country(), country_code
        person_dict['Address']['Postal'] = fake_us.postalcode_in_state()
        payload_write(person_dict,i)
        #print(i,person_dict)
        i=i+1

def generate_all():
    i = 0 #Initializing value for the loop
    while (i<num):
        person_dict['Name'] = fake.name()
        person_dict['Age'] = random.randint(10, 80)
        person_dict['Address']['Address_L1'] = fake.street_address()
        person_dict['Address']['City'] = fake.city()
        person_dict['Address']['State'] = fake.state()
        person_dict['Address']['Country'] = fake.country() #country_code
        person_dict['Address']['Postal'] = fake.postalcode()
        payload_write(person_dict,i)
        #print(i,person_dict)
        i=i+1

while True:
    try:
        choice = int(input("Select\n1. US\n2. All Countries :\n"))
        #break
    except (TypeError,ValueError):
        print("Enter a valid value. The input should be an integer number.")
    else:
        if choice == 1:
            generate_us()
            print(num,"Payload(s) written to the file",filename)
            break
        elif choice == 2:
            generate_all()
            print(num,"Payload(s) written to the file",filename)
            break
        else:
            print("Please choose from the given options.")
 

