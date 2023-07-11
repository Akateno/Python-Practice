#list comprehension:works with strings, list, and dictionaries   
#ex: new_list = [New_item for item in list]
#ex: numbe4s = [1,2,3]
    #  new_list=[]
    #  for n in list:
    #     add_1 = n+1
    # new_list.append(add_1)
    #now instead we do
    #new_list=[new_item for item in list]
    #new_list = [n+1 for n in numbers]

numbers = [1,2,3]
new_numbers=[n+1 for n in numbers]
print(new_numbers)

name="angela"
letters_list=[letter for letter in name]
print(letters_list)


#list, range, string supple 

new_numbs=range(1,5)
new_nums=[nums*2 for nums in new_numbs]
print(new_nums)

#conditional list comprehension 
#new_list = [new_item for item in list if test]

names=["alex","beth", "caroline", "dave", "eleanor", "freddie"]
# short_names=[name for name in names if len(name)<5]
# print(short_names)

uppercase_names=[name.upper() for name in names if len(name)>5]
print(uppercase_names)



#open fuiles with with open as, data overlap exercise 
# with open ("file1.txt") as file1:
#     data1=file1.readlines()
    
# with open ("file2.txt") as file2:
#     data2=file2.readlines()


# result=[int(item) for item in data1 if item in data2]

# # Write your code above 👆

# print(result)


#dictionary comprehension 
# new_dic = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
import random 
names=["alex","beth", "caroline", "dave", "eleanor", "freddie"]
student_scores = {student:random.ranint(1,100) for student in names}
passed_students={student:score for (student,score) in student_scores.items() if score>=60}


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
sentence2=sentence.split()
result= {word:len(word) for word in sentence2 }
# Write your code below:
print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

# Write your code 👇 below:
weather_f={day:(temp * 9/5) + 32 for (day,temp) in weather_c.items()}


print(weather_f)
