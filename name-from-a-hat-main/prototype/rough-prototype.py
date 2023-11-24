#This algorithm should simulate picking names from a hat.
import pandas as pd
import random as rand
import sys
import time
from tkinter import *
from tkinter import ttk


runtime = True
#pseudocode
# Extract Excel Sheet with Pandas
#   -> Begin runtime
#       -> Take the column with the names OR unique identifiers
#       -> Save column into the list
#       -> From the list, randomly select 1 item
#       -> Remove the item from the list using index()

#userin = input("Enter the name of the excel file: ")

print("*~*~*~*~*\tWelcome to Virtual Pick-A-Name-From-The-Hat\t~*~*~*~*~*")
print("\n")

#import data
userin = input("Enter the name of the Excel File (DO NOT ADD .xlsx): ")
userin = userin + ".xlsx"

try:
    frame = pd.read_excel(userin)
except Exception as e:
    print(e)
    print("Exiting program...Please try again")
    sys.exit()

mainlst = frame.loc[:, "Name"].to_list()
filtered = mainlst

while runtime:

    if len(filtered) == 0:
        print("There are no more names in the hat...")
        print("Thank you for using me!")
        break
    
    #randomly select a name from the list
    pickedname = rand.choice(filtered)
    
    #display the count
    print("From " + str(len(filtered)) + " people, the name pulled out is: ")
    print(".")
    time.sleep(.5)
    print(".")
    time.sleep(.5)
    print(".")
    time.sleep(.5)
    print(pickedname + "!")
    time.sleep(1)

    #display the name
    print("\n")
    print("-------------------------------------------------------------------")
    print("Congratulations to " + pickedname + "! You won the lucky draw!")
    print("-------------------------------------------------------------------")
    print("\n")

    #remove the name from the list completely
    filtered = list(filter((pickedname).__ne__, filtered))
    print("The amount of names still in the hat: " + str(len(filtered)))
    print("\n")

    decisionruntime = True

    while decisionruntime:
        userin2 = input("Pick another name? (y/n): ")
        userin2 = userin2.lower()

        if userin2 == "n":
            print("Goodbye!")
            runtime = False
            decisionruntime = False
        elif userin2 == "y":
            runtime = True
            decisionruntime = False
        else:
            print("Invalid Entry, please type in y or n")
            decisionruntime = True



#print("This program will now select a random value from 6000 pieces of data")

#time.sleep(1)

#frame = pd.read_excel("testsheet.xlsx")

#print(frame.loc[:, "Name"])

#fulllst = frame.loc[:, "Name"].to_list()
#x = rand.choice(fulllst)
#time.sleep(1)
#print(x)
#y = fulllst.index(x)
#time.sleep(1)
#print(len(fulllst))
#time.sleep(1)

#filtered = list(filter((x).__ne__, fulllst))

#print(len(filtered))

#time.sleep(1)
#print("This program will now show an example of removing 1 name from 10 for easier viewing")

#frame2 = pd.read_excel("testsheet2.xlsx")
#print(frame2.loc[:, "Name"])

#newlst = frame2.loc[:, "Name"].to_list()
#x2 = rand.choice(newlst)
#print("Selected name: " + x2)
#y2 = newlst.index(x2)
#print("Original List: ")
#print(newlst)

#filtered2 = list(filter((x2).__ne__, newlst))

#time.sleep(1)
#print("New List: ")
#print(filtered2)