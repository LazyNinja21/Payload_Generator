import json
from supp import *
infile = 'payload.json'
filename = 'person.txt'

#To clear the file before use
open(filename, 'w').close()

#Method to write the dictionary as json to a file
def payload_write(person_dict):
    with open(filename, 'a') as json_file:
        json_file.write("****************************\n")
        json.dump(person_dict, json_file,indent = 2)
        json_file.write("\n")

#Default payload
#person = '{"name": "", "age": 0}'

#Opening the json file to dump data as dictionary
with open(infile) as f:
  person_dict = json.load(f)

#User input for number of payload generation
num = input("Enter the number of payloads you need: ")
num = int(num)
i = 0

#Loop to generate the number of payloads defined by user
while (i<num):
    person_dict['name'] = fake.name()
    person_dict['age'] = random.randint(10, 80)
    payload_write(person_dict)
    #print(i,person_dict)
    i=i+1

print(num,"Payloads written to the file",filename)