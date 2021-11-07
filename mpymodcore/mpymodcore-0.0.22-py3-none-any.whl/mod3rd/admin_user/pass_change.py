from modcore.log import logger

from modext.windup import WindUp, Router
from modext.windup_auth import security_store

from mod3rd.simplicity import *
from modext.windup import Namespace


router = Router()


@router.get("/password")
def my_form(req, args):

    session = args.session

    notify = ""
    user = ""

    try:
        user = session.auth_user.name
        notify = session.notify
    except:
        pass
    finally:
        # keep session clean
        try:
            del session.notify
        except:
            pass

    if user == None or len(user) == 0:
        req.send_response(status=401, header=[])
        return

    t = """
        <!DOCTYPE html>
        <html lang="en">
        <html>
        <head>
            <meta charset="utf-8">
            <title>Password</title>
        </head>
        <body>

            <h2>Password</h2>
            <form action="/password" method="POST">
                <div>{notify}</div>
                <label for="f_pass1">New Password:</label><br>
                <input type="password" id="f_pass1" name="pass1" value="" ><br>
                <label for="f_pass2">Repeat Password:</label><br>
                <input type="password" id="f_pass2" name="pass2" value="" ><br>
                <input type="hidden" id="username" name="username" value="{username}" ><br>
                <input type="submit" value="Save">
            </form>
         
        </body>
        </html>
    """

    smpl = Simplicity(t, esc_func=simple_esc_html)
    ctx = Namespace()
    ctx.update(
        {
            "username": user,
            "notify": notify,
        }
    )

    data = smpl.print(ctx)

    logger.info(data)
    req.send_response(response=data)


# post request


@router.post("/password")
def my_form(req, args):

    # get the form data
    username = args.form.username

    password = args.form.pass1
    password2 = args.form.pass2

    session = args.session

    session_user = session.auth_user.name

    if session_user != username:
        # permission denied
        req.send_response(status=401, header=[])
        return

    if password != password2:
        session.notify = "Password do not match"
        req.send_redirect(url="/password")
        return

    session.notify = "Password saved"

    try:
        login_ok = security_store.save_user_password(session_user, password)
    except:
        session.notify = "Password save failed."

    req.send_redirect(url="/password")
