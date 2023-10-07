from kivy.core.audio import SoundLoader
from kivy.clock import Clock
import sys, requests, urllib

username = None
done = SoundLoader.load("sounds/gamescreen.mp3")
back = SoundLoader.load("sounds/back.mp3")
click = SoundLoader.load("sounds/click.mp3")
ex1 = SoundLoader.load("sounds/ex1.mp3")
ex2 = SoundLoader.load("sounds/ex2.mp3")
ex3 = SoundLoader.load("sounds/ex3.mp3")
finish = SoundLoader.load("sounds/done.mp3")
wrongsound = SoundLoader.load('sounds/wrong.mp3')
correctsound = SoundLoader.load('sounds/right.mp3')
main = SoundLoader.load("sounds/main.mp3")

sounds = {
    "done": done,
    "back": back,
    "click": click,
    "wrongsound": wrongsound,
    "correctsound": correctsound,
    "ex3": ex3,
    "finish": finish
}

musics = {
    "ex1": ex1,
    "ex2": ex2,
    "main": main
}

def bgmusic():
    main.play()
    main.loop = True

def ex_music():
    ex1.play()
    ex1.loop = True
def extwo_music():
    ex2.play()
    ex2.loop = True

def exthree_music():
    ex3.play()
    ex3.loop = True

def stop_music():
    if main.state == 'play':
        main.stop()

def stop_ex():
    if ex1.state == 'play':
        ex1.stop()

def stop_extwo():
    if ex2.state == 'play':
        ex2.stop()

def stop_exthree():
    if ex3.state == 'play':
        ex3.stop()


def save_score():
    path = 'scores/progress2.txt'
    with open(path, 'r') as f:
        i = f.read()
    i = int(i)

    i += 1

    i = str(i)
    with open(path, 'w') as f:
        f.write(i)


def save_error():
    path = 'scores/errors2.txt'
    with open(path, 'r') as f:
        x = f.read()
    x = int(x)

    x += 1

    x = str(x)
    with open(path, 'w') as f:
        f.write(x)

def attempts():
    path = 'scores/attempts.txt'
    with open(path, 'r') as f:
        i = f.read()
    i = int(i)

    i += 1

    i = str(i)
    with open(path, 'w') as f:
        f.write(i)

def angry():
    path = 'scores/angry.txt'
    with open(path, 'r') as f:
        i = f.read()
    i = int(i)

    i += 1

    i = str(i)
    with open(path, 'w') as f:
        f.write(i)

def happy():
    path = 'scores/happy.txt'
    with open(path, 'r') as f:
        i = f.read()
    i = int(i)

    i += 1

    i = str(i)
    with open(path, 'w') as f:
        f.write(i)

def disgust():
    path = 'scores/happy.txt'
    with open(path, 'r') as f:
        i = f.read()
    i = int(i)

    i += 1

    i = str(i)
    with open(path, 'w') as f:
        f.write(i)

def fear():
    path = 'scores/fear.txt'
    with open(path, 'r') as f:
        i = f.read()
    i = int(i)

    i += 1

    i = str(i)
    with open(path, 'w') as f:
        f.write(i)

def surprise():
    path = 'scores/surprise.txt'
    with open(path, 'r') as f:
        i = f.read()
    i = int(i)

    i += 1

    i = str(i)
    with open(path, 'w') as f:
        f.write(i)

def sad():
    path = 'scores/sad.txt'
    with open(path, 'r') as f:
        i = f.read()
    i = int(i)

    i += 1

    i = str(i)
    with open(path, 'w') as f:
        f.write(i)

def send_message():
	print ('Sending Message...')
	path = 'https://sms.teamssprogram.com/api/send?key=3261474a2cfc3766cf7b7216abcdd851b27b5e5b&phone=+639751727061&message=MESSAGEHERE&device=497&sim=0&priority=1'
	requests.post(path)
	print ('Message Sent!')