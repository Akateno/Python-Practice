# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
# from turtle import Turtle, Screen

# my_screen=Screen()
# print(my_screen.canvheight)


#initialize: to set vaiables, counter, switches, to their staring values at the eginnning of a program or subprogram, CONSTRUCTOR 


class User: 
    def __init__(self,user_id,username):
        self.id = user_id
        self.username=username
        self.followers=0
        self.follwoing=0



    def follow(self, user):
        user.follower +=1
        self.following +=1
        






user_1 = User("001", 'angela')
user_2 = User("002", "Jack")





