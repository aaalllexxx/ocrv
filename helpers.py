from register.models import User


def check_login(request):
    ident = request.cookies.get("session_id")
    sid = User.query.filter_by(session_id=ident).first()
    if sid is None:
        return False
    return True


def get_user(request):
    return User.query.filter_by(session_id=request.cookies.get("session_id")).first() or False
