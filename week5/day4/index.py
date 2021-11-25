import json
family_dict = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}
with open("json_file.json", "w") as f:
    json.dump(family_dict, f, indent = 4)
with open("json_file.json", "r") as f:
    family = json.load(f)
colors = ["yellow", "green"]
i = 0
for child in family["children"]:
    child["favorite_color"] = colors[i]
    i+= 1
with open("json_file.json", "w") as f:
    json.dump(family, f, indent = 4)