from modcore.log import logger
from modcore import modc

from modext.windup_auth import AuthRouter

from mod3rd.simplicity import *
from modext.windup import Namespace

from modext.windup_auth import security_store


router = AuthRouter(root="/admin")


@router.get("/secsys", groups=["root", "sudo", "admin"])
def get_secsys(req, args):

    t = """
            <!DOCTYPE html>
            <html lang="en">
            <html>
            <head>
                <meta charset="utf-8">
                <title>Security setup</title>
            </head>
            <body>

                <h2>Security setup</h2>
                <form action="/admin/secsys" method="POST">
                    <label for="f_enabled">Security Enabled:</label><br>
                    <input type="text" id="f_enabled" name="enabled" value="{enabled}" ><br>
                    <input type="submit" value="Save">
                </form>
             
            </body>
            </html>
    """

    smpl = Simplicity(t, esc_func=simple_esc_html)
    ctx = Namespace()
    ctx.update(
        {
            "enabled": str(security_store.__enabled).upper(),
        }
    )

    data = smpl.print(ctx)

    req.send_response(response=data, fibered=True)


@router.post("/secsys", groups=["root", "sudo", "admin"])
def post_secsys(req, args):

    form = args.form

    disabled = form.enabled.strip().upper() == "FALSE"

    logger.info("disabled", disabled)

    security_store._remove_all_settings()

    security_store.set_temp_enabled(not disabled)

    if disabled == True:
        security_store._save_settings()

    data = """
            <!DOCTYPE html>
            <html lang="en">
            <html>
            <head>
                <meta charset="utf-8">
                <title>Security setup</title>
            </head>
            <body>

                <h2>Security setup</h2>
                <div>
                    Data saved.
                </div>
             
            </body>
            </html>
    """

    req.send_response(response=data, fibered=True)
