# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Demonstrate how to use Pickling and Error Handling
# ChangeLog (Who,When,What):
#   Tyler Tidd,02/22/21, Created code
# ---------------------------------------------------------------------------- #

import pickle

#Initiatlize variables
lstTable =[]
choice = ""

# Load current pickled data
print("Try loading existing pickled data:")
try:
    objFile = open("Pickle.dat", "rb")
    objFileData = pickle.load(objFile)
    for i in objFileData:
        print(i["Task"] + " | " + i["Priority"])
    objFile.close()
    print("Successfully loaded file")
except FileNotFoundError as e:
    print("Custom message: 'File not found'")

while choice != 'exit':
    task = str(input('What is the new task name?: '))
    priority = str(input('What is the new task priority? (high/med/low): '))
    dicRow = {"Task": task, "Priority": priority}
    lstTable.append(dicRow)
    try:
        choice = input("Type 'exit' to exit or 'next' to input another task ").lower()
        if choice not in ['exit', 'next']:
            raise Exception("Please use 'exit' or 'next' keywords\n")
    except Exception as e:
        print("Python message: ", e, e.__doc__)
        print("Python type: ", type(e))

print("Here are your tasks pre-pickled:")
for i in lstTable:
    print(i["Task"] + " | " + i["Priority"])

print("Pickling tasks...")
objFile = open("Pickle.dat", "wb")
pickle.dump(lstTable, objFile)
objFile.close()

print("Here are your tasked unpickled: ")
objFile = open("Pickle.dat", "rb")
objFileData = pickle.load(objFile)
for i in objFileData:
    print(i["Task"] + " | " + i["Priority"])
objFile.close()
