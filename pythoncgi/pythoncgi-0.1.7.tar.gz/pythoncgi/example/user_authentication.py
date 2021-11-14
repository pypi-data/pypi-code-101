#!/usr/bin/python3
from pythoncgi import (
    _SERVER, _GET, _POST, _SESSION, _COOKIE, _HEADERS,
    set_status, set_header, generate_range_headers,
    execute, print, print_file, flush, main,
    log, log_construct,
    should_return_304,
    basic_authorization, parse_authorization,
)


# try GET http://127.0.0.1/user_authentication.py


def get_validater():
    # using some key store backend like keyring
    def backend(username, password):
        store = {
            "admin": "admin"
        }
        if username not in store:
            return False
        if password != store[username]:
            return False
        return True
    return backend


def validate():
    return get_validater()(*parse_authorization())


@execute(
    method="get",
    authentication=lambda: True,
)
def get():
    print("<p>Try username <b>admin</b> with password <b>admin</b>.</p>")
    print("<p>Logged in credentials: {}</p>".format(parse_authorization()))
    print("<p>")
    print("<input type='button' onclick='window.location=window.location.href.replace(window.location.hostname, \"admin:admin@\"+window.location.hostname)' value='Login'/>")
    print("<input type='button' onclick='window.location=window.location.href.replace(window.location.hostname, \"log:out@\"+window.location.hostname)' value='Logout'/>")
    print("</p>")
    print("<form method='post'><input type='submit' value='Try authentication in POST page'/></form>")


@execute(
    method="post",
    authentication=validate,
)
def post():
    print("<p>If you see this, it means you are authenticated.</p>")
    print("<p>Try logout and visit this page again.</p>")


if __name__ == '__main__':
    main()

