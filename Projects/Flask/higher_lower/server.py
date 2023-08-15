from flask import Flask 
import random

app=Flask(__name__)
guessed_number=random.randint(0,9)
print(guessed_number)

@app.route('/')
def test():
    
    return "<h1 style='text-align: center'>Guess a number between 0 and 9</h1>"\
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'  >"\


@app.route("/<int:guess>")
def guess_indicator(guess): 
    if guess > guessed_number:
        return "<h1> A little lower :D </h1>"\
                "<img src='https://media2.giphy.com/media/SEaKNxJgOfU76/giphy.gif?cid=ecf05e47qho4n36a31nnohqe4b0hzxj2pjd7a65spf81xydw&ep=v1_gifs_search&rid=giphy.gif&ct=g' >"
    elif guess < guessed_number:
        return  "<h1> A little higher!!! :D </h1>"\
                "<img src='https://media1.giphy.com/media/ek2J5jkQthPVu/giphy.gif?cid=ecf05e47padrhf1iw4xaqvry8q4ni2dqvvogwakt2b8chnou&ep=v1_gifs_search&rid=giphy.gif&ct=g' >"  
    elif guess == guessed_number:
        return "<h1> RIGHT ON THE MONEY!!! :D </h1>" \
                "<img src='https://media1.giphy.com/media/jG186kNLKs6TS/giphy.gif?cid=ecf05e47kneoks8fqor21p4re45d634g26khgdq7yuqosgr7&ep=v1_gifs_search&rid=giphy.gif&ct=g' >"
                     

            
    


if __name__== "__main__":
    app.run(debug=True)
