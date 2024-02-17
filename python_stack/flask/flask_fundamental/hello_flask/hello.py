from flask import Flask
# here we create an instance of flask (python file argument __name__)
app = Flask(__name__);

# called the route method using @ (decorator)  
@app.route('/')
def hello_world():
    return 'hello world!'

# import statements, maybe some other routes    
# @app.route('/success')
# def success():
#     return "success"
    
@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name


if __name__=='__main__':
    app.run(debug=True)