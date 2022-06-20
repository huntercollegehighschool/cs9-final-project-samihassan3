"""
Name(s): Sami Hassan
Name of Project: Adventure Game in a Mineshaft
"""
import os
import time
import page1
import page2

def start():
  name = str(input("What is your name? "))
  print(name + ",", "you are in an abandonded mineshaft, dust falling from the ceiling. There are two diverging hallways.")
  time.sleep(1)
  x = str(input("Which one would you like to go through? Enter left to go left and enter right to go right. Alternatively, you can enter 'stay' to stay in the main hallway. " ))
  if x == "left":
    lefthall()
  elif x == "right":
    righthall()
  elif x == "stay":
    stay()
  
def lefthall():
  os.system('clear')
  print("Very soon after you turn left, the ceiling behind you caves in.")
  time.sleep(2)
  print("Seeing as the only way to go is forward, you walk for a bit but the hallway gets darker and darker. You see a troll armed with a big club but your flashlight dies at that moment.")
  time.sleep(3)
  print("You can light a torch and risk the troll hearing you or you can attempt to stumble through the darkness.")
  y = str(input("Enter T to light torch or enter S to stumble. "))
  while y != "T" and y != "S":
    print("You must choose either T or S.")
    y = str(input("Enter T to light torch or enter S to stumble. "))
  if y == "T":
    page1.trollfight()
  elif y == "S":
    page1.headinjury()

def righthall():
  print("Very soon after you turn right, the ceiling behind you caves in.") 
  time.sleep(0.5)
  print("As you walk forward, you begin to notice remnants of old mining crew equipment: shattered flashlights, empty canteens.")
  time.sleep(0.5)
  print("You hear water dripping from a nearby cave.")
  z = str(input("Would you like to investigate the cave or continue through the main shaft? Enter I to investigate or C to continue walking. "))
  if z == "I":
    page2.investigate()
  if z == "C":
    page2.cont()

  
def stay():
  print("You stay too long and get crushed by the rock ceiling above you. ")
  time.sleep(1)
  redo = str(input("Enter E to start again. "))
  if redo == "E" or "e":
    os.system('clear')
    start()
start()