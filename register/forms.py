from wtforms import StringField, PasswordField, EmailField, Form, validators


class RegisterForm(Form):
    username = StringField('Имя пользователя', [validators.Length(min=4, max=25)])
    email = EmailField("Email", [validators.DataRequired()])
    password = PasswordField('Пароль', [validators.DataRequired()])
    confirm = PasswordField('Repeat Password', [
        validators.DataRequired(),
        validators.EqualTo('password', message='Passwords must match')
    ])
