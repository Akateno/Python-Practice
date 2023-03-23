#similar to arrays we can print the first character 
#this is called subscripting 

#using underscores for integers will be ignored by the computer 
#floats or floating point numbers are numbers with decimals 
print("Hello"[0])

#we can find what kind of class were working with
print(type(6))

#we can also convert from one data type to another 
#str takes object and converts to a string 
new_num = str(6)
print(new_num)

print(70 + float("100.5"))
print(str(70)+str(100))

#very easy to convert datatypes in python 
#we can round to two decimals places

print(8/2,2)

#fstring 
#similar to javascripts `${}`
score =0
height = 1.8
isWinning = True 

print(f"your score is {score}, your height is {height}, you are {isWinning}")

#use f strings to cut down in a lot of time so you dont have to convert data types if need be 

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
best_score=0; 
for score in student_scores:
    if score > best_score:
        best_score=score
        
print(f"The highest score in the class is: {best_score}")   
    