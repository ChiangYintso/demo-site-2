from flask import Flask, render_template
from forms import SignInForm

app = Flask(__name__)

app.secret_key = "123456"

# global varibles
user = {
    "name": "jiangyinzuo",
    "psword": "123456"
}


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SignInForm()
    global user
    if form.validate_on_submit():
        if user["name"] == form.name.data and user["psword"] == form.psword.data:
            return render_template('index.html', user=user)
        else:
            return render_template('signin.html', form=form, tag=True)
    return render_template('signin.html', form=form, tag=False)
