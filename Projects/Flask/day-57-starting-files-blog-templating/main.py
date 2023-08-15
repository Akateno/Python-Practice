from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url='https://api.npoint.io/c790b4d5cab58020d391'
    response_url=requests.get(blog_url)
    blog_data=response_url.json()
    return render_template("index.html", posts=blog_data)

@app.route('/posts')
def get_blog(posts):

    return render_template("post.html", posts=posts)



if __name__ == "__main__":
    app.run(debug=True)
