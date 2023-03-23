#random module 
import random 
#random_integer = random.randint(100,200)
#print(random_integer)

#random_float = random.random()
#print(random_float)

#basically learning about arrays
#.append(), .extend([1,2,3,4]), .split("") strings to list

# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print(names)
# 🚨 Don't change the code above 👆
names=names_string.split(", ")
#Write your code below this line 👇
num = (len(names))
choice = random.randint(0,num-1)
person_who_will_pay = names[choice]

print(f" {person_who_will_pay} is going to buy the meal today!")

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)
# print(dirty_dozen[0])
# print(dirty_dozen[1][2])
# print(dirty_dozen[1][3])