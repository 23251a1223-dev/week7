"""from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world!!'
if __name__=='__main__':
    app.run(debug=True)
"""
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    # Normally you’d save to DB here
    return render_template('success.html', username=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
