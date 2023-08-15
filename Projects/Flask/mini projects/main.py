from flask import Flask
app = Flask(__name__)



@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
            '<p>This is a paragraph</p> '\
            '<img src="https://butwhytho.net/wp-content/uploads/2023/07/Gear-5-But-Why-Tho.jpg" >'\
            '<img src="https://i.gifer.com/origin/e2/e2ffc3e709d4d3c376f6d4155bd0777b.gif" width=200 >'

@app.route('/bye')
def bye():
    return "Bye User"

@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello person named: {name}! you are {number} years old!"


#turn on auto refresh (debug=True)
if __name__== "__main__":
    app.run(debug=True)

#make CSS decorators 
def make_bold(function): 
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper 

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper 


#make advanced decorators 

class User: 
    def __init__(self,name):
        self.name=name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args,**kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper 

@is_authenticated_decorator
def create_blog_post(user):
    print(f"thiis is {user.name}s new blog post")

new_user=User("Erick")
new_user.is_logged_in=True 
create_blog_post(new_user)


# Create the logging_decorator() function 👇

def logging_decorator(fn):
    def wrapper(*args,**kwargs):
        print(f"you called {fn.__name__}{args} ")
        result=fn(args[0],args[1], args[2])
        print(f"the answer for this is {result}")
    return wrapper

    
# Use the decorator 👇
@logging_decorator
def test_func(a,b,c):
    return a*b*c

test_func(1,2,3)