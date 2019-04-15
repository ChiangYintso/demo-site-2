from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class SignInForm(Form):
    name = StringField(
        'Name', validators=[DataRequired(message=u'Pls input your name!')])
    psword = PasswordField('Password',
                           validators=[
                               DataRequired(message=u'Pls input your psword!'),
                               Length(6, 16, message=u'Invalid psword!')
                           ])
    rememberMe = BooleanField('Remember me')
    submit = SubmitField('Sign in')
