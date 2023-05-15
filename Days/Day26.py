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
