import os
import sneaky
import sneaky.driver
from undetected_chromedriver.v2 import ChromeOptions


def test_recaptcha(web: sneaky.SNEAKY, driver: sneaky.Chrome, vpncmd: sneaky.vpncmd):
    driver.get("https://www.google.com/recaptcha/api2/demo")

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
                return False
        except:
            print("solver probably failed")
            return False
        driver.switch_to.default_content()

    driver.mimic_move_to_random_xy()
    driver.mimic_click("//*[@id='recaptcha-demo-submit']")
    driver.wait(5 * 1)
    print("done")


def setup_profile(web: sneaky.SNEAKY, driver: sneaky.Chrome, vpncmd: sneaky.vpncmd):
    driver.get("https://chrome.google.com/webstore/detail/buster-captcha-solver-for/mpbjkejclgfgadiemmefgebjfooflfhl")
    input("setup done? ")
    input("sure? ")


def test_traffic_monitor(web: sneaky.SNEAKY, driver: sneaky.Chrome, vpncmd: sneaky.vpncmd):
    web.capture_request_traffic()
    driver.get("https://duckduckgo.com")
    driver.wait(3)
    import json
    print(json.dumps(web.request_traffic, indent=1))
    web.stop_capture_traffic()
    web.clear_traffic()


def main():
    print("~ SNEAKY sneaky ~")
    print()
    print("Mode: ")
    print("1. setup default profile")
    print("2. test solving recaptcha")
    print("3. test traffic monitor")
    print("4. exit")
    print()
    mode = input("Enter mode: ")
    if mode == "1":
        job = setup_profile
    elif mode == "2":
        job = test_recaptcha
    elif mode == "3":
        job = test_traffic_monitor
    else:
        exit(0)


    capabilities = sneaky.driver.DesiredCapabilities.CHROME
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
        vpncmd_enable=False,
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


