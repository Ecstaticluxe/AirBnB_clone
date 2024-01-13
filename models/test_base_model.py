#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print("Original state:")
print(my_model)
my_model.save()
print("\nState after saving:")
print(my_model)
my_model_json = my_model.to_dict()
print("\nDictionary representation:")
for key, value in my_model_json.items():
    print("\t{}: ({}) - {}".format(
        key, type(value), value
    ))

print("\nJSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(
        key, type(my_model_json[key]), my_model_json[key]
    ))
