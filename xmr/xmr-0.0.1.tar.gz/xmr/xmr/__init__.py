import discord
from requests import Session
from os import name, system
from sys import exit
from re import search
client = discord.Client()
session = Session()
token = ""
if name == "nt":
    clear = "cls"
else:
    clear = "clear"
@client.event
async def on_connect():
    system(clear)
    print(f"""
                                   _                
                       _________  (_)___  ___  _____
                      / ___/ __ \/ / __ \/ _ \/ ___/
                     (__  ) / / / / /_/ /  __/ /    
                    /____/_/ /_/_/ .___/\___/_/     
                                /_/                 

                        | User: {client.user} |      
                        | Sniping: Slotbot, Nitro Gifts And Giveaways | """)
@client.event
async def on_message(message):
    if "discord.gift/" in message.content:
        gift = search('discord.gift/(.*)', message.content).group(1)
        j = session.post(f"https://discordapp.com/api/v8/entitlements/gift-codes/{gift}/redeem", headers={"Authorization": token}).json()
        print(f"[Nitro]\nGift: {gift}\nMessage: {j['message']}")
    elif "Someone just dropped their wallet in this channel!" in message.content and message.author.id == 346353957029019648:
        try:
            await message.channel.send("~grab")
            print(f"[Slotbot] {message.jump_url}")
        except:
            return
    elif "GIVEAWAY" in message.content and message.author.id == 294882584201003009:
        try:
            await message.add_reaction("🎉")
            print(f"[Giveaway] {message.jump_url}")
        except:
            return

system(clear)
def start():
    global token
    token = input("Token\n>>> ")
    try:
        client.run(token, bot=False)
    except discord.errors.LoginFailure:
        print("Improper token has been passed.\n")
        exit(1)
start()