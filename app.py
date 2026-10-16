from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)