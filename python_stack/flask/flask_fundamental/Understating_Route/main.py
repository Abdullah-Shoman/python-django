from flask import Flask

app = Flask(__name__)

# Task 1
@app.route("/")
def hello():
    return "Hello World"
#  Task 2
@app.route("/dojo")
def hello_dojo():
    return "Dojo!"
#  Task 3
@app.route("/say/<name>")
def say(name):
    return "Hi "+ name +"!"
# Task 4
@app.route("/repeat/<num>/<string>")
def repeat(num,string):
    num = int(num)
    output = ""
    for counter in range(0,num):
        output = output+"<p>"+string+"</p>" 
    return output


if __name__ == '__main__':
    app.run(debug = True)

