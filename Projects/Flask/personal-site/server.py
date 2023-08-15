from flask import Flask, render_template
import requests

app=Flask(__name__)
@app.route("/")

@app.route('/guess/<name>')
def guess(name):
    gender_url=f'https://api.genderize.io?name={name}'
    age_url=f'https://api.agify.io?name={name}'

    gender_response=requests.get(gender_url)
    gender_data=gender_response.json()
    gender=gender_data['gender']


    age_reseponse=requests.get(age_url)
    age_data=age_reseponse.json()
    age=age_data['age']

    return render_template("guess.html", name=name, gender=gender,age=age)



def home():
    return render_template("index.html")





if __name__ == "__main__":
    app.run(debug=True)