from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#shows the login route, with the get and post methods 
#using request not to be confused with "requests" we can access the user input BUT the form input must have a name/filepath that matches rquest.form['name']
#meanwhile the form must have an action and a method at the
@app.route('/login', methods=['POST', 'GET'])
def receive_data():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        return f"Hi your name is {username} and your password is {password}"
        
        



if __name__ == '__main__':
    app.run(debug=True)


