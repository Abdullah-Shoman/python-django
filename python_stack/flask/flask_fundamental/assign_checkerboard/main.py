from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def map1():
    row = 8
    col = 8
    return render_template('index.html',col = col ,row = row)

@app.route('/<num>')
def map2(num):
    row = 8
    col = int(num)
    return render_template('index.html',col = col ,row = row)

@app.route('/<num>/<num2>')
def map3(num,num2):
    row = int(num2)
    col = int(num)
    return render_template('index.html',col = col ,row = row)


if __name__ == '__main__':
    app.run(debug = True)


