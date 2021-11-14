#!/usr/bin/env python3

import socketio,pyperclip,time,argparse

__version__ = "v0.0.15"
# standard Python
sio = socketio.Client()
@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error(data):
    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")


@sio.on('sync')
def on_message(data):
    pyperclip.copy(data["data"])

def main():
    parser = argparse.ArgumentParser(description='client for sync clipboard')
    parser.add_argument('-s','--server',help='server address to connect to',default="http://localhost:8080")
    parser.add_argument('-i','--id',help='the id to specify users',default="123123")
    parser.add_argument('-t','--access_token',help='token to access the server, must be same to the token of server',default="123123")
    args = parser.parse_args()
    server = args.server
    room = args.id
    access_token=args.access_token
    sio.connect(url=server,auth={"room":room,"access_token":access_token})

    curr_clip = pyperclip.paste()

    while pyperclip.waitForNewPaste():
        new_clip = pyperclip.paste()
        print("New clip: " + new_clip)

        if new_clip != curr_clip:
            if not new_clip.startswith("file:///"):
                sio.emit('sync',{"data":new_clip, "room":room})
            curr_clip = new_clip
def cli() -> None:
    try:
        main()
    except KeyboardInterrupt:
        print("\nExited on keyboard interrupt.")

if __name__ == '__main__':
    cli()