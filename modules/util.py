from os import system
import math
import sys
import random
import time
import readkeys
from replit import audio

def clear():
  system("clear")

def typeOut(string, sleeptime=0):
  wpm = 70
  for l in string:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(random.uniform(0,0.7)*10.0/wpm)
    source = audio.play_file("workingEh.wav")
  if sleeptime != 0:
    time.sleep(sleeptime)

def createMenu(text, carrotlocation, centerid=0, extraText=[], extraCenter=0):
  selected = 0
  while True:
    clear()
    for sentence in extraText:
      print(sentence.center(centerid))
    
    for sentence in text:
      if (text.index(sentence) == carrotlocation):
        if (centerid == 0):
          print((sentence + " <").center(centerid))
        else:
          print(("> " + sentence).center(centerid-2))
      else:
        print(sentence.center(centerid))
    menuInput = readkeys.getkey()
    if menuInput.lower() == "w" and selected > 0:
      selected -= 1
    elif menuInput.lower() == "s" and selected < len(text) - 1:
      selected += 1
    elif menuInput.lower() == "\r":
      return text[selected]
    carrotlocation = selected

def n(num=1):
  for x in range(num):
    print("")

def typeReplace(text, sleeptime=0):
  text = text

  alph = [f for f in "abcdefghijklmnopqrstuvwxyz .?!',-=+()*&^%$#@![]\{}|/<>"]
  alph.append('"')

  index = 0
  current = ""
  new = ""
  for x in text:
    letter = "a"
    current = ""
    new += letter
    while letter != x.lower():
      letter = random.choice(alph)
      while letter in current:
        letter = random.choice(alph)
      current += letter
      if x.lower() == x:
        new = [t for t in new]
        new[index] = letter
        new = "".join(new)
      else:
        new = [t for t in new]
        new[index] = letter.upper()
        new = "".join(new)
      sys.stdout.write('\x1b[1A')
      sys.stdout.write('\x1b[2K')
      # sys.stdout.write('\b \b')
      print(new)
      time.sleep(0.003)
    else:
      sys.stdout.write('\x1b[1A')
      sys.stdout.write('\x1b[2K')
      
      # sys.stdout.write('\b \b')
      print(new)
      source = audio.play_file("workingEh.wav")
    
    index += 1

  time.sleep(sleeptime)