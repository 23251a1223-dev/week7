
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return register()
    return render_template('register.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        password = request.form.get('password', '')
        confirm = request.form.get('confirm', '')

        if password != confirm:
            return render_template(
                'register.html',
                error='Passwords do not match.',
                name=name,
                email=email
            )

        return render_template('success.html', name=name)

    return render_template('register.html')


@app.route('/welcome/<name>', methods=['GET'])
def welcome(name):
    return render_template('welcome.html', name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
