import json

car_data = {"name": "tesla", "engine": "electric"}

# print(type(car_data))

# json.dumps()
# json.dump()

# car_data_json_string = json.dumps(car_data)   # converts to a json string
#
# print(car_data_json_string)
# print(type(car_data_json_string))


# with open("new_json_file.json", "w") as jsonfile:   # writing a json file
#     json.dump(car_data, jsonfile)

with open("new_json_file.json") as jsonfile:
    car = json.load(jsonfile)
    print(type(car))
    print(car["name"])