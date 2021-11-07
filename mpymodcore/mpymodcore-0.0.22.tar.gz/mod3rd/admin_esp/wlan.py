import sys
import ubinascii

from modcore.log import logger
from modcore import modc
from moddev.wlan import wlan_ap, WLAN_RESTART
from modext.windup import Router

from mod3rd.simplicity import *
from modext.windup import Namespace

from moddev.network import netw_man
from moddev.network import known_networks


router = Router(root="/admin")

# get request

netw = []


@router.get("/wlan")
def list_wlan(req, args):

    data = netw_data()

    # logger.info(data)
    req.send_response(response=data, fibered=True)


def scan_networks(debug=False):

    global netw
    netw = []

    networks = wlan_ap.scan()

    for nam, mac, channel, dbm, auth, hidden in networks:

        nam = nam.decode()
        mac = ubinascii.hexlify(mac).decode()

        saved = mac in known_networks

        obj = Namespace().update(
            {
                "mac": mac,
                "nam": nam,
                "dbm": dbm,
                "channel": channel,
                "auth": auth,
                "hidden": hidden,
                "known_netw": saved,
            }
        )
        netw.append(obj)

        debug and print(mac, nam)

    sort_name()


def sort_name():
    global netw
    netw = sorted(netw, key=lambda x: x.nam.lower())


def sort_signal():
    global netw
    netw = sorted(netw, key=lambda x: x.dbm)


def netw_data(debug=False):

    scan_networks(debug=debug)

    t = """
            <!DOCTYPE html>
            <html lang="en">
            <html>
            <head>
                <meta charset="utf-8">
                <title>WLAN configuration</title>
            </head>
            <body>

            <h2>WLAN configuration</h2>

            <div> &nbsp; </div>
            <div> Currently connected to: '{ssid}' </div>
            <div> &nbsp; </div>
            <div> IfConfig: '{ifconfig}' </div>
            <div> &nbsp; </div>

            <form action="/admin/wlan" method="POST">
            
                <div> Available Networks nearby </div>
                <div> &nbsp; </div>
                
                <div>
                
                <table>
                <tr>
                    <td></td>
                    <td>Name</td>
                    <td>Mac</td>
                    <td>Signal (dbm)</td>
                    <td>Authmode</td>
                    <td>Hidden</td>
                    <td>Channel</td>
                    <td>Known</td>
                    <td>Remove</td>
                </tr>
                    {*netw}
                    <tr>
                        <td><input type="radio" id="f_{_.mac}" name="fwifi" value="{_.mac}" {checked(_i)}></td>
                        <td><label for="f_{_.mac}">{_.nam}</label></td>
                        <td><span>{_.mac}</span></td>
                        <td><span>{_.dbm}</span></td>
                        <td>{authmode(_.auth)}</td>
                        <td>{hidden(_.hidden)}</td>
                        <td>{_.channel}</td>
                        <td>{_.known_netw}</td>
                        <td>{!_.known_netw}<a href="javascript:forget('{_.mac}')">forget me</a>{}</td>
                    </tr>
                    {}
                </table>
                
                </div>
                <script type="text/javascript">
                function forget(mac)\{
                    rc = confirm( "do you really want to remove network " + mac + " ?" );
                    if(rc)\{
                        window.location.assign( "/admin/wlan/forget/" + mac );
                    \}
                \}
                </script>

                <div> &nbsp; </div>
                <label for="f_passwd">Password:</label><br>
                <input type="text" id="f_passwd" name="fpasswd" value=""><br>

                <input type="submit" value="Connect">
                <div> Make sure to connect via SoftAP for setting up WLAN
                        otherwise Connection might get lost.
                </div>
            </form> 

            </body>
            </html>            
        """

    def authmode(auth):
        if auth == 0:
            return "open"
        if auth == 1:
            return "WEP"
        if auth == 2:
            return "WPA-PSK"
        if auth == 3:
            return "WPA2-PSK"
        if auth == 4:
            return "WPA/WPA2-PSK"

    def hidden(hid):
        if hid:
            return "yes"
        return "no"

    def check_first(index):
        if index == 0:
            return "checked"
        return ""

    wlan_info = wlan_ap.ifconfig()

    smpl = Simplicity(t, esc_func=simple_esc_html)
    ctx = Namespace()
    ctx.update(
        {
            "checked": check_first,
            "ssid": str(wlan_ap.ssid),
            "ifconfig": str(wlan_info),
            "netw": netw,
            "hidden": hidden,
            "authmode": authmode,
        }
    )

    debug and print(netw)
    debug and print(ctx)

    data = smpl.print(ctx)
    return data


# post request


@router.post("/wlan")
def my_form(req, args):

    form = args.form

    try:
        # namespace
        con = list(filter(lambda x: x.mac == form.fwifi, netw))[0]
        ssid = con.nam
        mac = con.mac
        passwd = form.fpasswd

        data = """
                <h1>WLAN configuration saved</h1>
                <div> &nbsp; </div>
                <div> Networkname: '%s' </div>
                <div> Mac: '%s' </div>
                <div> &nbsp; </div>
                <div> Go back to choose <a href="/admin/wlan">WLAN</a> </div>
                """ % (
            ssid,
            mac,
        )

        logger.info("ssid, passwd, mac:", ssid, passwd, mac)

        if len(passwd) == 0 and mac in known_networks:
            netw_man.network_switch(mac)
            logger.info("wlan switch done")

        else:
            wlan_ap.wlan_config(ssid, passwd, mac)
            logger.info("wlan config done")
            # restart in next loop, otherwise connection breaks and response fails
            modc.fire_event(WLAN_RESTART)

    except Exception as ex:

        data = """
                <h1>WLAN configuration failed</h1>
                <div> &nbsp; </div>
                <div> Info: '%s' </div>
                <div> &nbsp; </div>
                <div> Go back to choose <a href="/admin/wlan">WLAN</a> </div>
                """ % (
            ex
        )

    logger.info(data)
    req.send_response(response=data)


@router.xget("/wlan/forget/:mac")
def wlan_forget(req, args):
    rest = args.rest
    mac = rest.mac

    ex = netw_man.network_remove(mac)

    data = """
            <h1>WLAN network removed</h1>
            <div> &nbsp; </div>
            <div> Mac: '%s' </div>
            <div> &nbsp; </div>
            <div> Status: '%s' </div>
            <div> &nbsp; </div>
            <div> Go back to choose <a href="/admin/wlan">WLAN</a> </div>
            """ % (
        mac,
        ex,
    )

    logger.info(data)
    req.send_response(response=data)
