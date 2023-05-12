import turtle
import pandas


#import the data that has the coordinates for each state
data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()

# print(state_data[state_data.state == "Alaska"])
# print(state_data['state'])

screen = turtle.Screen()
screen.title("U.S. States Game")

#we can add the states image as a turtle graphic by adding to screen and addshape and turtle.shape(image)
image='blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

#getting the coordiates from the map to make labeling easier 
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

guessed_states=[]

while len(guessed_states)<50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Whats another states name?").title()

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item())


screen.exitonclick()
