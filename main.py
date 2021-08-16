from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'adfba2efkajd2fjlir37aerwe'

@app.route('/')
def top():
    return render_template('main.html')

@app.route('/prefecture/<prefName>')
def hello_pref(prefName):
    return render_template('hello_pref.html', prefName=prefName)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
