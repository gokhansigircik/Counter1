# pair programmed with Joana

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key ='CountingNumbers'

@app.route('/')
def index():
    if not session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return render_template('index.html', counter = session['counter'])

@app.route('/counter', methods=['POST'])
def counter():
    print(request.form)
    session['counter'] = request.form['counter']
    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

@app.route('/countup')
def count_up():
    session['counter'] += 2
    return render_template('index.html', counter = session['counter'])


if __name__ == "__main__":
    app.run(debug=True)

