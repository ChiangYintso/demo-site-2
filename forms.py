from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm


class SignInForm(FlaskForm):
    '''This form is in home.html'''
    name = StringField(
        'Name', validators=[DataRequired(message=u'Pls input your name!')])
    psword = PasswordField('Password',
                           validators=[
                               DataRequired(message=u'Pls input your psword!'),
                               Length(6, 16, message=u'Invalid psword!')
                           ])
    rememberMe = BooleanField('Remember me')
    submit = SubmitField('Sign in')


class NewNoteForm(FlaskForm):
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Save')


class EditNoteForm(FlaskForm):
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Update')


class DeleteNoteForm(FlaskForm):
    submit = SubmitField('Delete')
