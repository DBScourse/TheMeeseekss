# A log of the logged in users
logged_in = {}


def user_login(username):
    logged_in[username] = True


def user_check(username):
    return username in logged_in


def user_logout(username):
    logged_in.pop(username, 0)
