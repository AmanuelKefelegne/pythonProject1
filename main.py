#from bs4 import BeautifulSoup

#with open('html_xhtml.html' , 'r') as h:
#    con=h.read()

#    s=BeautifulSoup(con,'lxml')
#    p=s.find_all('script')
#    print(p)
#Install and import pymongo
import pymongo

#create connection string
conn_str="mongodb://localhost:27017"

#create client
try:
    client = pymongo.MongoClient(conn_str)
except Exception:
    print("Error:"+ Exception)

#create db
myDb=client["test"]

#create collection
myCollectin=myDb["account"]

#create record
myRecord={
    "name":"manaman",
    "age":"22"
}

#insert document
insert=myCollectin.insert_one(myRecord)
print(insert.inserted_id)
print(client.list_database_names())


#read record
readrecord= myCollectin.find_one()

#update record
query_upd={
    "age":"22"
}
new={
    "$set":{"age":"2"}
}
updaterecord=myCollectin.update_one(query_upd,new)

#Delete
'''
query_del={
    "name":"aman"
}
del_Record=myCollectin.delete_one(query_del);
print(myCollectin.find_one())'''