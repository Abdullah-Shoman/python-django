from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def Hello():
    return " Assignment playground, Please use route '/play' " 


@app.route('/play')
def level1():
    return render_template("index.html")


@app.route('/play/<num>')
def level2(num):
    times = int(num)
    return render_template("index.html",times = times)

@app.route('/play/<num>/<color>')
def level3(num,color):
    times = int(num)
    set_color = color
    return render_template("index.html",times = times , color = set_color)




if __name__ == '__main__':
    app.run(debug = True)