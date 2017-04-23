import uuid as ud


def uuid():
    u = str(ud.uuid4())
    return u.replace('-', '')
