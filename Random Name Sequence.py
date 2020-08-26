# importing random module
import random

#Making a list of candidates 
list1= ['Aakriti','Antara','Romil']

#Initializing value of State 
State = True

#Using While loop to generate mutliple sequence 
while State:
    #Generating random Values for the sequence
    for i in random.sample(range(0,3), 3):
        #printing the list 
        print(list1[i],end = "   ")
    print()
    #Updating value of state to prevent infinte loop
    State = int(input("Enter 1 or 0  "))
print("EOP")
