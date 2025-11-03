#Using the if else statements to make decisions

#ask user for their age
age = input("Enter your age: ")

#remove the words like 'years old' or 'I'm'
age = age.lower().replace("years old" , "").replace("i'm" , "" ).replace("i am" ,"").strip()

age = int(age)

#Determine the age group
if age < 18:
    group = "Minor"
elif age < 60:
    group = "Adult"
else:
    group = "Senior"

#Ask for user name
name = input("What is your name ?")

#remove words like i'm or i am
name = name.lower().replace("i'm", "").replace("i am", "").strip()
name = name.capitalize()

#Output or Print the results
print(f"Hello {name}, based on your age ({age}), you are {group}.")