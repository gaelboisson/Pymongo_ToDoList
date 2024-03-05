from pymongo import MongoClient
from pandas import DataFrame
# Get the database using the method we defined in pymongo_test_insert file
from pymongo_get_database import get_database
dbname = get_database()
collection_name = dbname["ToDoList"]

tasks = []


# Get the database using the method we defined in pymongo_test_insert file
from pymongo_get_database import get_database
dbname = get_database()
collection_name = dbname["ToDoList"]


def newTask(task):
    tasks.append(task)
    from dateutil import parser
    task_index = {
    "Tache" : task,
    "id" : id
    }
    collection_name.insert_one(task_index)
    print("Nouvelle tache ajoutée")

def toDo():
    # Retrieve a collection named "user_1_items" from database
    collection_name = dbname["ToDoList"]
 
    item_details = collection_name.find()
    for item in item_details:
        # convert the dictionary objects to dataframe
        items_df = DataFrame(item_details)

    # see the magic
    print(items_df)

def finishedTask(id):
    dbname.ToDoList.delete_one( { "id" : id } )


print("To-Do list")

while True:
    print("Menu")
    print("1 : Liste des taches")
    print("2 : Ajouter une tache")
    print("3 : Taches terminées")
            
    choice = input()

    if choice =="1":
        toDo()
    elif choice =="2":
        task = input("Nouvelle taches ? ")
        id = input("Numéro de la tache ? ")
        newTask(task)
    elif choice =="3":
        task_index = str(input("Numéro de la tache finie ? "))
        finishedTask(task_index)
    else:
        print("Non mais lis les choix stp")

    