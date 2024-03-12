from flask import Flask,session,redirect,render_template,request
import random

app = Flask(__name__)
app.secret_key = '121234312123'

# the main route 
@app.route('/')
def main():
    # check if the browser have the session or need to create a new session
    if 'gold' in session:
        print(session['gold'])
    else:
        # create a new session with defualt value
        session['gold'] = 0
        session['counter'] = 0
    
    # check if the browser have the session of avtivity or need to create a new one 
    if 'activites' in session:
        print(session['activites'])
    else:
        # create session for the activity and be list to save multi avtivity 
        session['activites'] = []

    # returne value be the render for the templates file (index.html)
    return render_template("index.html")

# Process money route
@app.route('/process_money', methods=['POST'])
def process_money():
    # get the value of the submit button (farm,cave,house and casino)
    building = request.form['building']
    if building == 'farm':
        # counter of the activity
        session['counter'] +=1
        # random value for the gold
        random_gold = random.randint(10,20)
        # add the new erne gold 
        session['gold']+= random_gold
        # save the activity 
        session['activites'].append('<p class = "win"> '+str(session['counter'])+': Earn '+ str(random_gold) +' gold from the farm! </p>')

    elif building == 'cave':
        session['counter'] +=1
        random_gold = random.randint(5,10)
        session['gold']+= random_gold
        session['activites'].append('<p class = "win"> '+str(session['counter'])+': Earn '+ str(random_gold) +' gold from the cave! </p>')

    elif building == 'house':
        session['counter'] +=1
        random_gold = random.randint(2,5)
        session['gold']+= random_gold
        session['activites'].append('<p class = "win"> '+str(session['counter'])+': Earn '+ str(random_gold) +' gold from the house! </p>')

    elif building == 'casino':
        session['counter'] +=1
        random_gold = random.randint(-50,50)
        session['gold']+= random_gold
        if random_gold > 0:
            session['activites'].append('<p class = "win"> '+str(session['counter'])+': Earn '+ str(random_gold) +' gold from the casino! </p>')
        else:
            session['activites'].append('<p class = "lose"> '+str(session['counter'])+': Earn '+ str(random_gold) +' gold from the farm! </p>')
    
    # return to the main route
    return redirect('/')

# rest the session and redirect to the main route
@app.route('/rest', methods = ['POST'])
def rest_game():
    # clear the session 
    session.clear()
    # retrun to the main route 
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)