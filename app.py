
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('register.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm = request.form.get('confirm', '')

        if not name or not email or not password or not confirm:
            return render_template(
                'register.html',
                error='Please fill in all fields.',
                name=name,
                email=email
            )

        if password != confirm:
            return render_template(
                'register.html',
                error='Passwords do not match.',
                name=name,
                email=email
            )

        return render_template('success.html', name=name)

    return render_template('register.html')


@app.route('/welcome/<name>')
def welcome(name):
    return render_template('welcome.html', name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
