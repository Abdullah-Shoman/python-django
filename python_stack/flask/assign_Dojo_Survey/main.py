from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result_form():
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    comment_from_form = request.form['comment']
    gender_from_form = request.form['gender']
    checkbox_from_form = request.form['check']
    print(checkbox_from_form)
    return render_template("result.html",name_from_form=name_from_form, location_from_form = location_from_form,
                        language_from_form = language_from_form,comment_from_form = comment_from_form,
                        gender_from_form = gender_from_form , checkbox_from_form = checkbox_from_form)


if __name__ == '__main__':
    app.run(debug = True)