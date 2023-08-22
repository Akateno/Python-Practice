from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

#the class well use in login route 
class MyForm(FlaskForm):
   email=StringField(label='Email:', validators=[DataRequired()])
   password=PasswordField(label='Password:', validators=[DataRequired()])
   submit=SubmitField(label='Log In')



app = Flask(__name__)
bootstrap=Bootstrap5(app)
app.secret_key = 'some_secret_string_you_cant_guess_WORORORRORORO'


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    login_form=MyForm()
    if login_form.validate_on_submit():
         if login_form.email.data == 'erickkvvargas@gmail.com' and login_form.password.data == "123":
             return render_template('success.html')
         else:
             return render_template('denied.html')
        
    #to get hold of the form data, instead of using request from previous projects 
    #print(login_form.email.data)
    #print(login_form.password.data)

    return render_template('login.html', form=login_form)



if __name__ == '__main__':
    app.run(debug=True)
