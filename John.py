#Create an empty list outside of your loop
incrt_names = []

while True: #While loop will break when input is John/john/JOHN
    name = input("Please enter a name ")#Asks for user input while loop isn't broken
    if name.upper() == "JOHN": #Checks if name is john
        break #Breaks out of loop when John
    else:
        incrt_names.append(name) #Appends other given string at index [-1] 

print(incrt_names) #Prints name after loop has been broken

#Printing the list after the loop will work because python goes line by line and won't runt the print() method before the loop has been broken.
#This giving you a list of incorrect strings.