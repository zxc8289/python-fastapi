import json

with open('C:\\code\\test1-fastapi\\data\\userList.json', encoding="utf8") as f:
    json_object = json.load(f)

print(json_object)
