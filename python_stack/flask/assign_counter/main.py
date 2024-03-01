from flask import Flask, render_template, session,redirect,request

app = Flask(__name__)
app.secret_key = '121212321'


# main route session for counter 
@app.route('/')
def main():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1 
    # if 'counter' in session:
    #     print('Session is Created')
    # else:
    #     print('there is not session')

    return render_template('index.html')

# create route/desotry_session to clear the session and redirect to the min route 
@app.route('/destroy_session')
def destroy_session():
    print("hello Destroy")
    session.pop()
    return redirect('/')

# add 2 visitor button 
@app.route('/add', methods=['POST'])
def add_visitor():
    print("add two visitor")
    session['counter']+=1
    return redirect('/')

# rest button 
@app.route('/rest_session', methods=['POST'])
def rest_session():
    print("Rest Visitor")
    session.clear()
    return redirect('/')


# add visitor by client
@app.route('/add_visitor', methods=['POST'])
def add_by_client():
    session['counter'] += (int(request.form['num'])-1)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)