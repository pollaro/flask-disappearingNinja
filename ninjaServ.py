from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/ninja')
def allNinjas():
    return render_template('ninjas.html')
@app.route('/ninja/<color>')
def showColor(color):
    if color == 'blue':
        return render_template('blue.html')
    elif color == 'red':
        return render_template('red.html')
    elif color == 'orange':
        return render_template('orange.html')
    elif color == 'purple' or color == 'violet':
        return render_template('purple.html')
    else:
        return render_template('not.html')
app.run(debug=True)
