# JSON javascript object notation 
import requests 
import json



#loads = when u fetching data form site/api that time u got a responce in string , that string formated data converted into python dictionary format
data = '{"name" : "ErMapsh", "Age": 21}'
parsed = json.loads(data)
print(parsed["name"])


#load
with open("json/json_file.json", 'r') as content:
    print(json.load(content))



#dumps : means python dictionary to javascript
data2 = {
    "ChannelName" : "ErMapsh", 
    "Cars" : ['bmw', 'suzuki', 'tata'],
    "laptop" : ('roti', 460),
    "isbad" : False
 }
jsCompab = json.dumps(data2)
print(jsCompab)


#dump
with open("json/json_file1.txt") as f:
    print(json.dump(data, f.write(data)))