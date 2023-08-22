
from flask import Flask, render_template, request
import requests 
import smtplib 

app = Flask(__name__)

posts_data = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

personal_email= "erickkvvargas@gmail.com"
personal_password=''

@app.route('/')
def home():

    return render_template("index.html", all_posts=posts_data)


@app.route('/about')
def about():
   return render_template("about.html")

@app.route('/contact', methods=["GET", "POST"])
def contact():
   if request.method == "POST":
        data=request.form
        print(data['name'])
        print(data['email'])
        print(data['phone'])
        print(data['message'])
        return render_template("contact.html", msg_sent=True)
   return render_template('contact.html', msg_sent=False)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts_data:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


#this was in day/lesson 32
def send_email(name,email,phone,message):
     email_message=f"subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
     with smtplib.SMTP('smtp.gmail.com') as connection:
         connection.starttls()
         connection.login(personal_email,personal_password)
         connection.sendmail(personal_email,personal_email, email_message)

if __name__ == "__main__":
    app.run(debug=True)


