
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_people=0
for count in student_heights:
    total_people+=1
    

height_total=0
for heights in student_heights:
    height_total+=heights
    

average=round(height_total/total_people)
print(average)