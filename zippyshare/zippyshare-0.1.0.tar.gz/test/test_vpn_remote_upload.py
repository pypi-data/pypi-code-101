import zippyshare
import zippyshare.utils
import traceback


credentials = zippyshare.utils.read_account_info(open("accounts.txt", "rb").read().decode())


zs = zippyshare.ZS(
    vpncmd_option={
        "vpncmd_fp": r"C:\Program Files\SoftEther VPN Client\vpncmd_x64.exe"
    },
    vpncmd_setup_cmd_option=[
        "/client",
        "localhost",
    ],
    debug=True
)


f = "/path/to/zip.zip"
try:
    for i, _ in enumerate(credentials):
        zs.login(
            credentials=_[2:4],
            use_vpn=True,
            _NICNAME="VPN2",
        )
        # since zippyshare limits 500MB per file
        # you need to implement a custom bytes serving file server
        # learn more at https://github.com/foxe6/pythoncgi/blob/master/pythoncgi/example/zippyshare_remote_upload.py
        url = "http://mydomain/?part={}&filepath={}".format(i+1, f)
        print(url, zs.remote_upload(url))
        zs.logout()
except:
    traceback.print_exc()


zs.logout()

