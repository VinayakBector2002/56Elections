print("Programme to count the zoom votes!")
list1 = list((map(str,input("Enter the names in upper case, seperated by ',' i.e commas").split(","))))
print(list1)
d1 = {"name":"votes"}
for i in list1:
    d1[i] = 0
print(d1)
print("Refer to the dictionary above for confirming the names")
l2 = []
fin = open("zoomchats.txt", "r")
for line in fin.readlines():
    for word in line.split():
        if word.isupper() in list1:
            d1[word.isupper()] +=1
        else:
            l2.append(word)
            

print("These are redundant entries ", l2)

print("Final result ")
print(d1)



fin.close()


print("EOP")
