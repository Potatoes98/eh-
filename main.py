import os
import math
import sys
import random
import time
import readkeys
from modules.util import *

typeReplace("Nobody will ever know why this exists...", 1)
clear()



typeOut("Eh? EH?! Why are you here? Eh, I'm sure it'll be fine...\n", 1)
print("Option 1: Eh?\nOption 2: Eh...\n")
selection = readkeys.getkey()
if not selection.isnumeric():
  clear()
  typeReplace("You made a grave mistake there, eh?", 1)
  typeReplace("I guess I have to give you a chance... eh?")
  typeReplace("Eh? You feel a great pain in your heart and a heavy weight appear on your back.")
  clear()

  typeOut("ENEMY DETECTED", 0.5)
  typeOut(".", 0.5)
  typeOut(".", 0.5)
  typeOut(".", 0.5)
  clear()

  staminaE = 500
  healthE = 500
  energyE = 500
  speedE = 20
  
  name = "eh?"
  power = "100"
  attack = "10"
  health = "100"
  energy = "100"
  stamina = "100"
  defense = "5"
  speed = 0
  mainText = ["Attack", "Prepare", "Rest", "Check Enemy Stats"]
  extraText = ["Name: " + name, "Power Rating: " + power, "Attack: " + attack, "Health: " + health, "Energy: " + energy, "Stamina: " + stamina, "Defense: " + defense, "\nOptions: "]

  while True:
    clear()
    selection = createMenu(mainText, 0, 0, extraText, 0)

    if selection == "Check Enemy Stats":
      clear()
      print("Name: You didn't input a number\nPower Rating: eh?\nAttack: 100\nHealth: %s\nEnergy: %s\nStamina: %s\nDefense: 0\n" % (healthE, energyE, staminaE))
      print("Press any key to continue")
      readkeys.getkey()
      continue
    elif selection == "Rest":
      stamina = "100"
    elif selection == "Prepare":
      pass