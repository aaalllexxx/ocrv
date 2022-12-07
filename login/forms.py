from wtforms import StringField, PasswordField, Form, validators


class LoginForm(Form):
    username = StringField('Имя пользователя', [validators.Length(min=4, max=25)])
    password = PasswordField('Пароль', [validators.DataRequired()])
