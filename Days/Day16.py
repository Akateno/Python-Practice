import AnotherModule 
#print(AnotherModule.another_variable)


#import turtle 
#we can just import turutle like this or another way
#timmy=turtle.Turtle()
#at this point we have created timmy which an object 


# from turtle import Turtle, Screen 

# timmmy2=Turtle()
# timmmy2.shape("turtle")
# timmmy2.color("blue")
# timmmy2.forward(100)

# my_screen=Screen()
#print(my_screen.canvheight)
# my_screen.exitonclick()


#Day17


class User: 
    def __init__(self,user_id,user_name):
        self.id=user_id
        self.user_name=user_name
        self.followers=0
        self.following=0

        print("new user being created....")
        #self is the object being created or initialized, we can follow with as many parameters that get passed down 

    def follow(self,user):
        user.follower +=1
        self.following +=1

#instead of this:
# user1=User()
# user1.id=1
# user1.username="Tony"

#we can write 
user_1=User(1,"Tony")
user_2=User(2,"Kiwi")

user_1.follow(user_2)












