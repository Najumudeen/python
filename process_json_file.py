# import json

# mydict = {
#     "people": [
#         {
#             "name": "Bob",
#             "age": 28,
#             "weight": 80
#         },
#         {
#             "name": "Anna",
#             "age": 34,
#             "weight": 67
#         },
#         {
#             "name": "Charles",
#             "age": 45,
#             "weight": 78
#         },
#         {
#             "name": "Daniel",
#             "age": 21,
#             "weight": 110
#         }
#     ]
# }

# # Dumps takes actuall objects 
# json_string = json.dumps(mydict, indent=2)

# with open('mydata.json', 'w') as f:
#     f.write(json_string)
# #print(json_string)

# Read Json Files
################################

# import json

# with open('mydata.json', 'r') as f:
#     json_object = json.loads(f.read())

# print(json_object['people'][0]['name'])

################################
# Read Json file with object Oriented
# 

import json

class Person:

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def print_info(self):
        print(self.name, self.age, self.weight)


    def get_older(self, years):
        self.age += years

# save to json

    def save_to_json(self, filename):
        person_dict = {'name': self.name, 'age': self.age, 'weight': self.weight}
        with open(filename, 'w') as f:
            f.write(json.dumps(person_dict, indent=2))

    
    def load_from_json(self, filename):
        with open(filename, "r") as f:
            data = json.loads(f.read())

        self.name = data['name']
        self.age = data['age']
        self.weight = data['weight']



# p1 = Person("Mike", 27, 90)
# p1.print_info()
# p1.get_older(3)
# p1.save_to_json("mike.json")

# Load data

p2 = Person(None, None, None)
p2.load_from_json("mike.json")
p2.print_info()