def trollfight():
  import os
  import page3
  import time
  os.system('clear')
  print("The troll hears you light the torch and starts rushing towards you.")
  time.sleep(1)
  a = str(input("Enter 'punch' to attack the troll with your hands, enter 'kick' to kick the troll, enter 'fire' to attack with your torch, or enter 'dodge' to attempt to dodge the rushing troll. "))
  if a == "punch":
    page3.punch()
  if a == "kick":
    page3.kick()
  if a == "fire":
    page3.fire()
  if a == "dodge":
    page3.dodge()

def headinjury():
  import os
  import time
  import page5
  os.system('clear')
  print("Whilst stumbling in the dark, you accidentally slam your head into the rock ceiling.")
  time.sleep(1)
  print("The troll hears this, and walks over and looks at you with a sense of pity. The troll starts to carry you, and then you fall asleep.")
  time.sleep(3)
  page5.unconscious()