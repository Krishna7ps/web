# datetime to compare dates, json to work with json input
import datetime as dt 
import json

# loading json files
with open("new_image.json","r") as rf:
    data=json.load(rf)

# count files to retain or delete
Obj_delete=0
Obj_retain=0

# User input for retention period
retention_days=int(input("Please enter retention days: "))

# d2 holds date and time at execution, while d1 hold object creation date
d2=dt.datetime.now()

print("Count, total file objects:",len(data))

# Iterate through each object of the json-input-file and extrating object creation time
# d1-d2 give age of the object
# AgeOfObj should be less than retention_days to file be retained. Otherwise, it should be
# deleted

for i in data:
    d1=dt.datetime.strptime(str.split(i["creationTimestamp"],'.')[0],"%Y-%m-%dT%H:%M:%S")
    AgeOfObj= d2-d1
    if AgeOfObj.days>retention_days:
        Obj_delete+=1
    else:
        Obj_retain+=1

print("Count, files to be deleted:", Obj_delete)
print("Count, files to be retained:", Obj_retain)
     
