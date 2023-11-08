import pymongo

mongo_uri = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.0.2"

client = pymongo.MongoClient(mongo_uri)

db = client.get_database('db')

collection = db.get_collection("student_1")

def insert():
    name1 = input("Enter name: ")
    roll1 = int(input("Enter roll: "))
    marks1 = int(input("Enter marks: "))
    data_to_insert = {"roll": roll1, "name": name1, "marks": marks1}
    inserted_id = collection.insert_one(data_to_insert).inserted_id
    print("Record inserted successfully")

def remove():
    roll = int(input("Enter roll no to delete: "))
    query = {"roll": roll}
    projection = {"_id": 0}
    temp = collection.find_one(query, projection=projection)
    if temp is None:
        print("Record does not exist")
    else:
        print(temp)
        collection.delete_one(query)
        print("Record deleted successfully")

def update():
    roll = int(input("Enter roll no to update: "))
    marks = int(input("Enter new marks: "))
    query = {"roll": roll}
    query1 = {"$set": {"marks": marks}}
    projection = {"_id": 0}
    temp = collection.find_one(query, projection=projection)
    if temp is None:
        print("Record does not exist")
    else:
        print("Before Update:")
        print(temp)
        collection.update_one(query, query1)
        temp = collection.find_one(query, projection=projection)
        print("After Update:")
        print(temp)
        print("Record updated successfully")

def display_all():
    cursor = collection.find({}, projection={"_id": 0})
    print("All Records:")
    for document in cursor:
        print(document)
    
   

def search_records():
    roll = int(input("Enter roll no to search: "))
    query = {"roll": roll}
    projection = {"_id": 0}
    cursor = collection.find(query, projection=projection)
    print("Matching Records:")
    for document in cursor:
        print(document)
    
    

def main():
    while True:
        print("-----------------------------------------------------")
        print("\t1.Insert")
        print("\t2.Update")
        print("\t3.Delete")
        print("\t4.Display All Records")
        print("\t5.Search Records")
        print("\t6.Exit")
        ch = int(input("Enter your choice here: "))
        if ch == 1:
            insert()
        elif ch == 2:
            update()
        elif ch == 3:
            remove()
        elif ch == 4:
            display_all()
        elif ch == 5:
            search_records()
        else:
            client.close()
            break

main()
