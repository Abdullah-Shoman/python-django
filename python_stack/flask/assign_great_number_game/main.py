from flask import Flask, render_template, request, session,redirect 
import random

app = Flask(__name__)
app.secret_key = '9k9k9k9k'
random_num = random.randint(1,100)

@app.route('/')
def main():
    # print(random_num)
    number_from_form = 0
    try_num = 0
    return render_template('index.html',number_from_form = number_from_form , random_num = random_num,try_num = try_num)

@app.route('/', methods=['POST'])
def main2():
    try_num = 0
    session['number'] = request.form['num']
    number_from_form =int(session["number"])
    print("number is ",random_num)
    print(number_from_form)
    return render_template('index.html',number_from_form = number_from_form,random_num=random_num, try_num = try_num)



if __name__ == '__main__':
    app.run(debug = True)