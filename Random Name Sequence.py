# importing random module
import random

#Making a list of candidates 
list1= ['Candidate1','Candidate2','Candidate3']

#Initializing value of State 
State = True

#Using While loop to generate mutliple sequence 
while State:
    #Generating random Values for the sequence
    print(random.sample(list1, 3))
    #Updating value of state to prevent infinte loop
    try :
        State = int(input("Enter 1 or 0  "))
    except ValueError:
        continue 
print("EOP")
