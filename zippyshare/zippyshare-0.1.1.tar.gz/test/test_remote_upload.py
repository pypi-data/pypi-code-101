import zippyshare
import traceback


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


try:
    zs.login(
        use_vpn=False,
        _NICNAME="VPN2",
    )
    print(zs.remote_upload("https://pastebin.com/raw/sViuU9AN"))
except:
    traceback.print_exc()


zs.logout()

