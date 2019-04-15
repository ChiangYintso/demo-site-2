from flask import Flask, render_template

app = Flask(__name__)

app.secret_key = "123456"

# global varibles
user = {
    "name": 'JYZ',
}


@app.route('/')
def index():
    return render_template('index.html', user=user)
