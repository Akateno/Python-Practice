#Conditional operators 
print("Whelcome to rollercoaster")
height = int(input("What is your height in cm? "))

if height >= 120: 
    print("You can ride the roller coaster")
    age = int(input("What is your age?"))
    if age < 12:
        bill =5
        print("Please pay $5")
    elif age<=18:
        bill= 7
        print("that will be $7")
    elif age >= 45 and age <= 55:
        print("everything is ok, free ride for you!!!")
    else: 
        bill = 12
        print("that will be 12")
else:
    print("sorry you have to be taller")

wants_photo = input("Do you want a photo? Y or N. ")

if wants_photo == "Y":
    bill +=3

print(f"Your final bill is {bill}")

#elif statement 
#you can use as many between the if and else part of the statement 

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_string = name1 + name2 
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love = l + o + v + e

love_score = int(str(true) + str(love))




if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50: 
    print(f"Your score is {love_score}, you are alright together.")
else: 
    print(f"Your score is {love_score}")


    

#modulo
number = int(input("Which number do you choose?"))
if number % 2 ==0:
    print("This is an even number")
else:
    print("This is an odd number")

#multiple if statements in succession 


#Logical Operators
#just like javascript 
