# Loops let us repeat actions multiple times without writing the same code again
#This loop will count from 1 to 10 using FOR loop
print("Counting from 1 to 10 using FOR loop : ")

for i in range(1, 11) : #range (1, 11) gives numbers 1 to 10
    print(i) #Print the current number
    

#WHILE loop
#This loop will count from 1 to 10 using the while loop
print("\nCounting from 1 to 10 using WHILE loop : ")

count = 1  #start with 1
while count <= 10: #repeat as long as count is 10 or less
    print(count) #print the current number
    count+= 1 #Increase count by 1 each time