from pymongo import MongoClient
import pymongo
client = MongoClient('3.221.17.194', 9999)
db = client.Modelsdb
customcollection=db.Models
print('hai')
'''for i in customcollection.find({'Custommodelid': 'ad9fe98-c5a0-48aa-af03-e702673c7374'},{"Uploadedfiles3location": 1, "Modelservicetype": 1, "Modeltype": 1,"max_seq_length": 1, "batch_size": 1, "Lableldata": 1, "Lables": 1}):
    print(type(i))
    print(len(i))'''

#db.Models.update_many({"Originofmodel": "Nativemodel",}, {"$rename":{"Model-cognitiveservicetype":"Model_cognitiveservicetype"}})
'''myquery = {"Originofmodel": "Nativemodel",'Modelid': '7b616791-a166-4543-b791-3b31ed6461c2'}
newvalues = {"$set": {"Model-cognitiveservicetype": "text"}}
#newvalues={"$rename":{"Model-apiurl":"Model_apiurl"}}
updation = customcollection.update_many(myquery, newvalues)
#q={}
#r={$rename:{"Model-apiurl":"Model_apiurl"}}
#up=customcollection.update(q, r, false, true)'''