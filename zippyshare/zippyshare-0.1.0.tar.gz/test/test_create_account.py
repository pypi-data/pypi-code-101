# following test code is extracted from https://pypi.org/project/sneaky/


import zippyshare.utils
import os
import sneaky
import sneaky.helper
from undetected_chromedriver.v2 import ChromeOptions


def create_accounts(info, driver: sneaky.Chrome, vpncmd: sneaky.vpncmd):
    zs = zippyshare.ZS(debug=True)

    for _ in info:
        if zs.check_account_created(_[2]):
            print("account '{}' existed".format(_[2]))
            continue
        bot_detected = False

        driver.get("https://www.zippyshare.com/sites/registration.jsp")
        test_div = driver.execute_script('''
        var div = document.createElement("div");
        div.id = "test_move";
        div.style="right:0;bottom:0;top:0;left:0;position:absolute;z-index:99999999999;opacity:0.666;"
        var div2 = document.createElement("div");
        var style = "width:10px;height:10px;position:relative;background:green;border:2px solid blue;";
        div2.style = style;
        div.appendChild(div2);
        document.body.appendChild(div);
        window.addEventListener("mousemove", function(e){
            div2.style = style+"top: "+e.pageY+"px;left: "+e.pageX+"px;";
        });
        return document.querySelector("div#test_move");
        ''')

        driver.execute_script('''arguments[0].style.pointerEvents = "all";''', test_div)
        driver.mimic_move_to_random_xy()
        driver.execute_script('''arguments[0].style.pointerEvents = "none";''', test_div)

        driver.mimic_send_input("//input[@id='firstname']", [
            sneaky.helper.Keys.pause_random(),
            _[0],
            sneaky.helper.Keys.pause_random(),
            sneaky.helper.Keys.TAB,
            sneaky.helper.Keys.pause_random(),
            _[1],
            sneaky.helper.Keys.pause_random(),
            sneaky.helper.Keys.TAB,
            sneaky.helper.Keys.pause_random(),
            _[2],
            sneaky.helper.Keys.pause_random(),
            sneaky.helper.Keys.TAB,
            sneaky.helper.Keys.pause_random(),
            _[3],
            sneaky.helper.Keys.pause_random(),
            sneaky.helper.Keys.TAB,
            sneaky.helper.Keys.pause_random(),
            _[3],
            sneaky.helper.Keys.pause_random(),
            sneaky.helper.Keys.TAB,
            sneaky.helper.Keys.pause_random(),
            _[4],
        ], True)
        driver.mimic_move_to_random_xy()
        driver.mimic_click("//*[@id='terms']")

        recaptcha_iframe1 = driver.xpath("//iframe[@title]")[0]
        recaptcha_iframe1_pos = [recaptcha_iframe1.rect["x"], recaptcha_iframe1.rect["y"]]
        driver.print_element(recaptcha_iframe1)
        print("recaptcha_iframe1", recaptcha_iframe1_pos, recaptcha_iframe1.rect)

        driver.switch_to.frame(recaptcha_iframe1)
        recaptcha_btn = driver.xpath("//*[@id='recaptcha-anchor']")[0]
        recaptcha_btn_pos = [recaptcha_btn.rect["x"], recaptcha_btn.rect["y"]]
        driver.print_element(recaptcha_btn)
        print("recaptcha_btn", recaptcha_btn_pos, recaptcha_btn.rect)

        click_x = recaptcha_iframe1_pos[0]+recaptcha_btn_pos[0]+(recaptcha_btn.rect["width"])/2
        click_y = recaptcha_iframe1_pos[1]+recaptcha_btn_pos[1]+(recaptcha_btn.rect["height"])/2
        print("recaptcha_btn click_x click_y", click_x, click_y)
        driver.switch_to.default_content()
        driver.execute_script('''arguments[0].style.pointerEvents = "all";''', test_div)
        driver.wait(0.3)
        driver.mimic_move_to_random_xy()
        driver.execute_script('''arguments[0].style.pointerEvents = "none";''', test_div)
        driver.wait(0.3)
        while "hidden" in driver.xpath("//iframe[@title]/../..")[1].get_attribute("style"):
            driver.wait(1)
            driver.execute_script('''arguments[0].style.pointerEvents = "all";''', test_div)
            driver.wait(0.3)
            driver.mimic_move_to_xy(click_x, click_y)
            driver.execute_script('''arguments[0].style.pointerEvents = "none";''', test_div)
            driver.wait(0.3)
            driver.mimic_click()
            driver.wait(1)
            print("recaptcha_btn click loop", driver.xpath("//iframe[@title]/../..")[1].get_attribute("style"))
            driver.wait(1)
            driver.execute_script('''arguments[0].style.pointerEvents = "all";''', test_div)
            driver.wait(0.3)
            driver.mimic_move_to_random_xy()
            driver.execute_script('''arguments[0].style.pointerEvents = "none";''', test_div)
            driver.wait(0.3)

        recaptcha_iframe2 = driver.xpath("//iframe[@title]")[1]
        recaptcha_iframe2_pos = [recaptcha_iframe2.rect["x"], recaptcha_iframe2.rect["y"]]
        driver.print_element(recaptcha_iframe2)
        print("recaptcha_iframe2", recaptcha_iframe2_pos, recaptcha_iframe2.rect)

        driver.switch_to.frame(recaptcha_iframe2)
        solver_btn = driver.xpath("//*[contains(@class, 'help-button-holder')]")[0]
        solver_btn_pos = [solver_btn.rect["x"], solver_btn.rect["y"]]
        driver.print_element(solver_btn)
        print("solver_btn", solver_btn_pos, solver_btn.rect)

        click_x = recaptcha_iframe2_pos[0]+solver_btn_pos[0]+solver_btn.rect["width"]/2
        click_y = recaptcha_iframe2_pos[1]+solver_btn_pos[1]+solver_btn.rect["height"]/2
        print("solver_btn click_x click_y", click_x, click_y)
        driver.switch_to.default_content()
        driver.execute_script('''arguments[0].style.pointerEvents = "all";''', test_div)
        driver.wait(0.3)
        driver.mimic_move_to_random_xy()
        driver.execute_script('''arguments[0].style.pointerEvents = "none";''', test_div)
        driver.wait(0.3)
        while True:
            driver.wait(1)
            driver.execute_script('''arguments[0].style.pointerEvents = "all";''', test_div)
            driver.wait(0.3)
            driver.mimic_move_to_xy(click_x, click_y)
            driver.execute_script('''arguments[0].style.pointerEvents = "none";''', test_div)
            driver.wait(0.3)
            driver.mimic_click()
            driver.wait(1)
            print("solver_btn click loop", driver.xpath("//iframe[@title]/../..")[1].get_attribute("style"))
            driver.wait(1)
            driver.execute_script('''arguments[0].style.pointerEvents = "all";''', test_div)
            driver.wait(0.3)
            driver.mimic_move_to_random_xy()
            driver.execute_script('''arguments[0].style.pointerEvents = "none";''', test_div)
            driver.wait(0.3)
            print("solving please wait")
            driver.wait(10)
            if "visible" not in driver.xpath("//iframe[@title]/../..")[1].get_attribute("style"):
                break
            driver.switch_to.frame(driver.xpath("//iframe[@title]")[1])
            try:
                if driver.xpath("//*[contains(text(), 'sending automated queries')]"):
                    print("bot detected")
                    bot_detected = True
                    rotate_vpn(driver, vpncmd)
                    break
                    return False
            except:
                print("solver probably failed")
                bot_detected = True
                rotate_vpn(driver, vpncmd)
                break
                return False
            driver.switch_to.default_content()

        if not bot_detected:
            driver.mimic_move_to_random_xy()
            driver.mimic_click("//*[@id='signupsubmit']")
            driver.wait(5*1)
            if zs.check_account_created(_[2]):
                open("accounts.txt", "ab").write(("\n".join(_)+"\n\n").encode())
                print("created account '{}'".format(_[2]))
            else:
                print("failed to create account '{}'".format(_[2]))
        else:
            print("failed to create account '{}'".format(_[2]))


def rotate_vpn(driver: sneaky.Chrome, vpncmd: sneaky.vpncmd):
    driver.get("about:blank")
    vpncmd.disconnect_vpn()
    driver.wait(1)
    vpncmd.connect_known_vpn(_NICNAME="VPN2")
    while not vpncmd.is_connected_to_vpn():
        driver.wait(0.5)


def setup_profile(driver: sneaky.Chrome, vpncmd: sneaky.vpncmd):
    driver.get("https://chrome.google.com/webstore/detail/buster-captcha-solver-for/mpbjkejclgfgadiemmefgebjfooflfhl")
    input("setup done? ")
    input("sure? ")


def main():
    info = zippyshare.utils.generate_account_info()
    info = zippyshare.utils.read_account_info(open("zippy.txt", "rb").read().decode())
    print("~ SNEAKY sneaky ~")
    print()
    print("Mode: ")
    print("1. setup default profile")
    print("2. create zippy accounts")
    print("3. exit")
    print()
    mode = input("Enter mode: ")
    if mode == "1":
        job = setup_profile
    elif mode == "2":
        job = lambda *args: create_accounts(info, *args)
    else:
        exit(0)

    capabilities = sneaky.helper.DesiredCapabilities.CHROME
    options = ChromeOptions()
    profile_fp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ChromeProfile")
    os.makedirs(profile_fp, exist_ok=True)
    options.add_argument("--user-data-dir={}".format(profile_fp))
    options.add_argument("--profile-directory=Default")
    sneaky.test(init=dict(
        executable_path=r"C:\chromedriver.exe",
        options=options,
        # capabilities=capabilities,
        # capabilities=options.to_capabilities(),
        open_developer_tools=True,
        # browsermobproxy_enable=False,
        browsermobproxy_server_init={
            "path": r"C:\browsermob-proxy\bin\browsermob-proxy.bat"
        },
        browsermobproxy_create_proxy_kwargs={
            "params": {
                "trustAllServers": "true",
                "port": 8009
            }
        },
        browsermobproxy_new_har_kwargs={
            "options": {
                "captureHeaders": True,
                "captureContent": True
            }
        },
        # vpncmd_enable=False,
        vpncmd_init={
            "vpncmd_fp": r"C:\Program Files\SoftEther VPN Client\vpncmd_x64.exe",
            "debug": True
        },
        vpncmd_setup_cmd_args=[
            "/client",
            "localhost",
        ],
        vpncmd_connect_known_vpn_kwargs={
            "_NICNAME": "VPN2"
        },
        debug=True
    ), job=job)


if __name__ == "__main__":
    main()




