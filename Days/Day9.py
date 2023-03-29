#dictionaries aka objects 

dictionary={"bug":"an error in code",}
#retrieving items from dictionary
print(dictionary['bug'])

#adding new itoms to dictionary
dictionary["loop"]="Thea action of repeating"
print(dictionary)

#loop through a dictionary 
for key in dictionary:
    print(key)
    print(dictionary[key])


student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
    score = student_scores[student]
    if score > 91:
        student_grades[student]="Outstanding"
    elif score >80:
        student_grades[student]="Exceeds Expectations"
    elif score > 70:
        student_grades[student]="Acceptable"
    else:
        student_grades[student]="Fail"

# 🚨 Don't change the code below 👇
print(student_grades)