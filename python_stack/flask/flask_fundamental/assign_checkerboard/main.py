from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def main():
    num = 8
    num2 = 8
    color1 = 'gold'
    color2 = 'goldenrod'
    return render_template('index.html',num=num,num2=num2,color1=color1,color2=color2)


@app.route('/<num>')
def main2(num):
    num2 = 8
    num = int(num)
    color1 = 'gold'
    color2 = 'goldenrod'
    return render_template('index.html',num=num,num2=num2,color1=color1,color2=color2)

@app.route('/<num>/<num2>')
def main3(num,num2):
    num = int(num)
    num2 = int(num2)
    color1 = 'gold'
    color2 = 'goldenrod'
    return render_template('index.html',num=num,num2=num2,color1=color1,color2=color2)



@app.route('/<num>/<num2>/<color1>/<color2>')
def main4(num,num2,color1,color2):
    color1 = color1
    color2 = color2
    num = int(num)
    num2 = int(num2)
    return render_template('index.html',color1=color1,color2=color2,num=num,num2=num2)


if __name__ == '__main__':
    app.run(debug = True)


