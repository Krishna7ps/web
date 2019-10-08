import json
# import datetime
from datetime import date, datetime, timedelta
import datetime as dt 

with open("new_image.json","r") as rf:
    data=json.load(rf)
File_count=0
retention_days=input("Please enter retention days: ")
# d1 = datetime.now()-timedelta(days=int(retention_days))
# print("type of d1", type(d1))
# d1=datetime.strptime(d1, "%Y-%m-%d")

for i in data:
    d2=datetime.strptime(str.split(i["creationTimestamp"],'T')[0], "%Y-%m-%d")

    print("type of d2", type(d2))
    if (d1-d2).days <retention_days:
        File_count+=1

print("Condition Met files count:",File_count)



