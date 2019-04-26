from flask import Flask, render_template, abort, redirect, session, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import SignInForm, NewNoteForm, EditNoteForm, DeleteNoteForm
import click
import os

app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY', '23rf2erg4')

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', 'sqlite:///' + os.path.join(app.root_path, 'data.db'))

db = SQLAlchemy(app)


# Models
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)


# global varibles
user = {"name": "jiangyinzuo", "psword": "123456"}


@app.cli.command()
def initdb():
    '''flask initdb'''
    db.create_all()
    click.echo('Initialized database!')


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'logged_in' in session:
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))


@app.route('/home', methods=['GET', 'POST'])
def home():
    form = DeleteNoteForm()
    notes = Note.query.all()
    return render_template('home.html', notes=notes, form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global user
    form = SignInForm()
    if form.validate_on_submit():
        if user['name'] == form.name.data:
            return redirect(url_for('home'))
    return render_template('login.html', form=form)


@app.route('/new_note', methods=['GET', 'POST'])
def new_note():
    form = NewNoteForm()
    if form.validate_on_submit():
        body = form.body.data
        note = Note(body=body)
        db.session.add(note)
        db.session.commit()
        flash('Your note is saved.')
        return redirect(url_for('home'))
    return render_template('new_note.html', form=form)


@app.route('/edit_note/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    form = EditNoteForm()
    note = Note.query.get(note_id)
    if form.validate_on_submit():
        note.body = form.body.data
        db.session.commit()
        flash('Your note is updated.')
        return redirect(url_for('home'))
    form.body.data = note.body  # preset form input's value
    return render_template('edit_note.html', form=form)


@app.route('/delete_note/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    form = DeleteNoteForm()
    if form.validate_on_submit():
        note = Note.query.get(note_id)
        db.session.delete(note)
        db.session.commit()
    else:
        abort(400)
    return redirect(url_for('home'))
