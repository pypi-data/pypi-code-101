from credsafe.utils import Manager
from omnitools import getpw, parse_credentials_argv


# the manager is used to perform quick saves from console inputs and quick loads for apps without configuring RSA keys and other underlying values
# see example at https://github.com/foxe6/zippyshare/blob/master/zippyshare/core.py#L33
csm = Manager("my_app_name")


def my_app(credentials=None):
    if not credentials:
        credentials = parse_credentials_argv(True)
        if credentials:
            csm.export_credentials(credentials, overwrite=True)
        else:
            credentials = csm.import_credentials()
            if not credentials:
                credentials = [
                    input("Enter username: "),
                    getpw("Enter password: "),
                ]
                print()
                csm.export_credentials(credentials)
    print("credentials", credentials)


# enter user pass from prompt
# will be exported
my_app()
# enter user pass within program
# will not be exported
my_app(["user", "pass"])
# enter user pass from command line
# will be exported
# test_manager.py -U user --password pass
# test_manager.py --username user -P pass
# delete credentials
csm.delete_credentials()

