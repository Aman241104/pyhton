import json

data = {'name':"Ram", 'lname':"Chandra",'age':29}

with open('data.json','w') as file:
    json.dump(data,file,indent=2)
    file.close()

with open('data.json','r') as file:
    getData=json.load(file)
    print(getData)
    file.close()