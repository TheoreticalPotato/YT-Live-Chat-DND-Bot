import pytchat
from speech import *
from random import randint

chat = pytchat.create(video_id="VIDEO ID")

barbs = []
wizs = []
rogues = []

b = ''
w = ''
r = ''

def choice(choices):
    return choices[randint(0, len(choices) - 1)]

def newBarb():
    global b
    b = choice(barbs)
    print(F'New Barb: {b}')

def newRogue():
    global r
    r = choice(rogues)
    print(F'New Rogue: {r}')

def newWiz():
    global w
    w = choice(wizs)
    print(F'New Wiz: {w}')

def tts():
    print("bot is running")
    while chat.is_alive():
        for c in chat.get().sync_items():
            if c.author.name == b:
                barbSays = open('barbsays.txt', 'w')
                barbSays.write(f"{b}: {c.message}")
                barbSays.close()
                barbSpeak(c.message)
            if c.author.name == w:
                wizSays = open('wizsays.txt', 'w')
                wizSpeak(c.message)
                wizSays.write(f"{w}: {c.message}")
                wizSays.close()
            if c.author.name == r:
                rogueSays = open('roguesays.txt', 'w')
                rogueSpeak(c.message)
                rogueSays.write(f"{r}: {c.message}")
                rogueSays.close()
            if "!barbarian" in c.message and c.author.name not in barbs:
                barbs.append(c.author.name)
                print(f"{c.author.name} has been appended to barbs")
            if "!wizard" in c.message and c.author.name not in barbs and c.author.name not in wizs:
                wizs.append(c.author.name)
                print(f"{c.author.name} has been appended to wizs")
            if "!rogue" in c.message and c.author.name not in wizs and c.author.name not in barbs and c.author.name not in rogues:
                rogues.append(c.author.name)
                print(f"{c.author.name} has been appended to rogues")