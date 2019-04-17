from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm


class SignInForm(FlaskForm):
    '''
    This form is in index.html
    '''
    name = StringField(
        'Name', validators=[DataRequired(message=u'Pls input your name!')])
    psword = PasswordField('Password',
                           validators=[
                               DataRequired(message=u'Pls input your psword!'),
                               Length(6, 16, message=u'Invalid psword!')
                           ])
    rememberMe = BooleanField('Remember me')
    submit = SubmitField('Sign in')
