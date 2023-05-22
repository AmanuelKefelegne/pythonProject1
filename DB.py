#Install and Import pymongo
import pymongo

#Create a connection String
connection_string="mongodb://localhost:27017"

#create client
try:
    client = pymongo.MongoClient(connection_string)
except Exception:
    print("Error:" + Exception)

#Create a Database
final_project_Db=client["test"]

#Create Collections and Insert a Record
def insert_record(collection_name,record):
    final_project_Db[f"{collection_name}"].insert_one(record)

#Read All Records
def read_all_records(collection_name):
    final_project_Db[f"{collection_name}"].find()

#Read one Record
def read_one_record(collection_name,name):
    final_project_Db[f"{collection_name}"].find_one({"name": name})

