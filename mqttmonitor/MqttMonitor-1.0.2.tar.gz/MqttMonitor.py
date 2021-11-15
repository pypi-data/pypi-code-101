#
# Copyright (c) 2021 Fw-Box (https://fw-box.com)
# Author: Hartman Hsieh
#
# Description :
#   The function is based on MQTT.
#   When the original serial of ESP8266/ESP32 cannot be used,
#   it can replace serial print.
#
# Libraries :
#    pip install paho.mqtt
#

from tkinter import *
from tkinter import ttk
import tkinter.font as Font
import threading
import time
import paho.mqtt.client as mqtt
import json
from io import StringIO
import random, string


__version__ = "1.0.2"


mainWin = Tk()


WIN_BG = "white"
WIDGET_BG = "white"
WIDGET_FG = "black"
PAD_X = 10
PAD_Y = 10
IPAD_X = 0
IPAD_Y = 0

TextInfo = None
gLabelStatus = None
gVarCheckAutoscroll = None
gButtonRun = None
gClient = None
gSubTopic = ""
gMqttRunning = False
gAppConfig = None

def main():
    global gAppConfig
    global TextInfo

    gAppConfig = loadAppConfig()

    TextInfo = initGUI(mainWin)

    mainWin.mainloop()


def initGUI(win):
    global gAppConfig
    global TextInfo
    global gLabelStatus
    global gVarCheckAutoscroll
    global gButtonRun

    wg_font = Font.Font(family='微軟正黑體', size=12, weight='bold')
    wg_font_small = Font.Font(family='微軟正黑體', size=10, weight='bold')
    
    frame2 = Frame(win, bg=WIN_BG)
    frame2["bg"] = WIDGET_BG

    frame3 = Frame(win, bg=WIN_BG)
    frame3["bg"] = WIDGET_BG

    frame1 = Frame(win, bg=WIN_BG)
    frame1["bg"] = WIDGET_BG

    str_title = "MqttMonitor %s - https://fw-box.com" % (__version__)
    win.title(str_title)
    win.geometry('670x400')
    win.configure(background=WIN_BG)

    #
    # Frame 2
    #

    textInfoScrollbar = Scrollbar(frame2)
    textInfoScrollbar.pack(side=RIGHT, fill=Y)

    textInfo = Text(frame2, width=180, height=80, yscrollcommand=textInfoScrollbar.set)
    textInfo.pack()
    textInfo.configure(state='disabled')

    textInfoScrollbar.config(command=textInfo.yview)

    #
    # Frame 1
    #

    col_index = 0

    gLabelStatus = Label(frame1, text="X", background='red')
    gLabelStatus.grid(row=0, column=col_index, sticky=E, padx=0, pady=0, ipadx=0, ipady=0)
    col_index = col_index + 1

    lbSpace0 = Label(frame1, text=" ")
    lbSpace0["bg"] = WIDGET_BG
    lbSpace0.grid(row=0, column=col_index, sticky=E, padx=0, pady=0, ipadx=0, ipady=0)
    col_index = col_index + 1

    lbBroker = Label(frame1, text="Broker")
    lbBroker["bg"] = WIDGET_BG
    lbBroker.grid(row=0, column=col_index, sticky=E, padx=0, pady=0, ipadx=0, ipady=0)
    col_index = col_index + 1

    textBroker = Text(frame1, width=15, height=1)
    textBroker["bg"] = WIDGET_BG
    textBroker.grid(row=0, column=col_index, sticky=W, padx=0, pady=0, ipadx=0, ipady=0)
    col_index = col_index + 1
    textBroker.delete(1.0,"end")
    textBroker.insert(1.0, gAppConfig['MqttBroker'])

    lbSpace1 = Label(frame1, text=" ")
    lbSpace1["bg"] = WIDGET_BG
    lbSpace1.grid(row=0, column=col_index, sticky=E, padx=0, pady=0, ipadx=0, ipady=0)
    col_index = col_index + 1

    lbPort = Label(frame1, text="Port")
    lbPort["bg"] = WIDGET_BG
    lbPort.grid(row=0, column=col_index, sticky=E, padx=0, pady=0, ipadx=0, ipady=0)
    col_index = col_index + 1

    textPort = Text(frame1, width=6, height=1)
    textPort["bg"] = WIDGET_BG
    textPort.grid(row=0, column=col_index, sticky=W, padx=0, pady=0, ipadx=0, ipady=0)
    col_index = col_index + 1
    textPort.delete(1.0,"end")
    textPort.insert(1.0, gAppConfig['MqttBrokerPort'])

    lbSpace2 = Label(frame1, text=" ")
    lbSpace2["bg"] = WIDGET_BG
    lbSpace2.grid(row=0, column=col_index, sticky=E, padx=0, pady=0, ipadx=0, ipady=0)
    col_index = col_index + 1

    lbSubTopic = Label(frame1, text="Sub Topic")
    lbSubTopic["bg"] = WIDGET_BG
    lbSubTopic.grid(row=0, column=col_index, sticky=E, padx=0, pady=0, ipadx=0, ipady=0)
    col_index = col_index + 1

    textSubTopic = Text(frame1, width=28, height=1)
    textSubTopic["bg"] = WIDGET_BG
    textSubTopic.grid(row=0, column=col_index, sticky=W, padx=0, pady=0, ipadx=0, ipady=0)
    col_index = col_index + 1
    textSubTopic.delete(1.0,"end")
    textSubTopic.insert(1.0, gAppConfig['SubTopic'])

    lbSpace3 = Label(frame1, text=" ")
    lbSpace3["bg"] = WIDGET_BG
    lbSpace3.grid(row=0, column=col_index, sticky=E, padx=0, pady=0, ipadx=0, ipady=0)
    col_index = col_index + 1

    gButtonRun = Button(frame1)
    gButtonRun["bg"] = WIDGET_BG
    gButtonRun["text"] = "Connect"
    gButtonRun["command"] = lambda: onClick(textBroker.get("1.0","end"), textPort.get("1.0","end"), textSubTopic.get("1.0","end"))
    gButtonRun.grid(row=0, column=col_index, sticky=W, padx=0, pady=0, ipadx=0, ipady=0)
    col_index = col_index + 1

    lbSpace5 = Label(frame1, text=" ")
    lbSpace5["bg"] = WIDGET_BG
    lbSpace5.grid(row=0, column=col_index, sticky=E, padx=0, pady=0, ipadx=0, ipady=0)
    col_index = col_index + 1

    #gButtonSetting = Button(frame1)
    #gButtonSetting["bg"] = WIDGET_BG
    #gButtonSetting["text"] = "*"
    #gButtonSetting["command"] = lambda: onClickButtonSetting()
    #gButtonSetting.grid(row=0, column=col_index, sticky=W, padx=0, pady=0, ipadx=0, ipady=0)
    #col_index = col_index + 1

    #
    # Frame 3
    #

    col_index = 0

    gVarCheckAutoscroll = BooleanVar()
    gCheckAutoscroll = Checkbutton(frame3, var=gVarCheckAutoscroll)
    gCheckAutoscroll["bg"] = WIDGET_BG
    gCheckAutoscroll["text"] = "Autoscroll"
    gCheckAutoscroll["command"] = lambda: onClickAutoscroll()
    gCheckAutoscroll.grid(row=0, column=col_index, sticky=W, padx=0, pady=0, ipadx=0, ipady=0)
    gVarCheckAutoscroll.set(True)
    col_index = col_index + 1

    gButtonClearOutput = Button(frame3)
    gButtonClearOutput["bg"] = WIDGET_BG
    gButtonClearOutput["text"] = "Clear output"
    gButtonClearOutput["command"] = lambda: onClickClearOutput(textInfo)
    gButtonClearOutput.grid(row=0, column=col_index, sticky=W, padx=0, pady=0, ipadx=0, ipady=0)
    col_index = col_index + 1

    frame1.pack(padx=2,pady=2)
    frame3.pack(padx=2,pady=2)
    frame2.pack(padx=2,pady=2)

    return  textInfo


def addLine(str):
    global TextInfo
    global gVarCheckAutoscroll
    #print(str)
    TextInfo.configure(state='normal')
    TextInfo.insert(END, str)
    #TextInfo.insert(END, "\n")
    if gVarCheckAutoscroll.get():
        TextInfo.yview(END)
    TextInfo.configure(state='disabled')


def onClickAutoscroll():
    global gVarCheckAutoscroll
    print("onClickAutoscroll")
    print("gVarCheckAutoscroll=%d" % (gVarCheckAutoscroll.get()))

def onClickClearOutput(textOutput):
    print("onClickClearOutput")
    textOutput.config(state=NORMAL)
    textOutput.delete('1.0', END)
    textOutput.config(state='disabled')

def onClickButtonSetting():
    print("onClickButtonSetting")
    sub_win = Tk()

    wg_font = Font.Font(family='微軟正黑體', size=12, weight='bold')
    wg_font_small = Font.Font(family='微軟正黑體', size=10, weight='bold')

    frame1 = Frame(sub_win, bg=WIN_BG)
    frame1["bg"] = WIDGET_BG

    sub_win.title('MqttMessage 1.0.0 - https://fw-box.com')
    sub_win.geometry('200x100')
    sub_win.configure(background=WIN_BG)

    lbSpace1 = Label(frame1, text="123")
    lbSpace1["bg"] = WIDGET_BG
    lbSpace1.grid(row=0, column=0, sticky=E, padx=0, pady=0, ipadx=0, ipady=0)

    frame1.pack(padx=PAD_X,pady=PAD_Y)

def onClick(broker, port, subTopic):
    global gAppConfig
    global gClient
    global gSubTopic
    global gMqttRunning
    new_broker = broker.strip()
    new_port = int(port.strip())
    new_sub_topic = subTopic.strip()
    print(new_broker)
    print(new_port)
    print(new_sub_topic)

    str_status = gLabelStatus.cget("text")
    if str_status == "O":
        print("Try to disconnect")
        gMqttRunning = False
    elif str_status == "X":
        gSubTopic = new_sub_topic

        gAppConfig['MqttBroker'] = new_broker
        gAppConfig['MqttBrokerPort'] = new_port
        gAppConfig['SubTopic'] = new_sub_topic
        saveAppConfig(gAppConfig)

        #if client != None:
        #    client.close()

        gClient = mqtt.Client()

        gClient.on_connect = on_connect

        gClient.on_disconnect = on_disconnect

        # 設定接收訊息的動作
        gClient.on_message = on_message

        # 設定登入帳號密碼
        #gClient.username_pw_set("try","xxxx")

        # 設定連線資訊(IP, Port, 連線時間)
        gClient.connect(new_broker, new_port, 60)

        gMqttRunning = True
        # 建立一個子執行緒
        th = threading.Thread(target = runMqttLoop, args = (gClient, ))
        th.setDaemon(True)#守護執行緒
        # 執行該子執行緒
        th.start()

def loadAppConfig():
    j_data = None
    try:
        with open('MqttMonitor.json', 'r') as read_file:
            j_data = json.load(read_file)
    except:
        print("The file 'MqttMonitor.json' doesn't exist.")
    if j_data == None:
        str_topic = random.choice(string.ascii_lowercase)
        str_topic = str_topic + (''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(15)))
        str_topic = "message/" + str_topic
        print("str_topic=" + str_topic)
        j_data = {"MqttBroker":"broker.emqx.io","MqttBrokerPort":1883,"SubTopic":str_topic}
    return j_data

def saveAppConfig(jData):
    ret = json.dumps(jData)
    with open('MqttMonitor.json', 'w') as fp:
        fp.write(ret)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    global gSubTopic
    global gButtonRun
    print("MQTT : Connected with result code " + str(rc))
    client.subscribe(gSubTopic)
    gLabelStatus.configure(background='green')
    gLabelStatus.config(text="O")
    gButtonRun.config(text="Disconnect")
    #print(gLabelStatus.cget("text"))   

def on_disconnect(client, userdata, rc):
    global gMqttRunning
    global gButtonRun
    print("MQTT : Disconnected")
    gLabelStatus.configure(background='red')
    gLabelStatus.config(text="X")
    gButtonRun.config(text="Connect")
    gMqttRunning = False

#
# The callback for when a PUBLISH message is received from the server.
#
def on_message(client, userdata, msg):
    payload = str(msg.payload, "utf-8")
    #print("MQTT : Message received\n" + payload + "\ntopic : " + msg.topic + "\nretained = " + str(msg.retain))
    addLine(payload)

def runMqttLoop(ObjMqttClient):
    global gMqttRunning
    while gMqttRunning:
        ObjMqttClient.loop() # runs one iteration of the network loop
    ObjMqttClient.disconnect() # disconnect gracefully



if __name__ == "__main__":
    main()
