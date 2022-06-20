
def investigate():
  import os
  import time
  os.system('clear')
  print("As you enter the cave, you see a stunning green pool of water below you. The aroma reminds you of somewhere you've never gone but still feels slightly familiar.")
  time.sleep(3)
  d = str(input("Would you like to relax near the edge of the pool, or would you like to take a nice dive? Enter 'relax' to stay near the edge, or enter 'dive' to jump in. "))
  if d == "dive":
    import page4
    page4.dive()
  if d == "relax":
    import page4
    page4.relax()

def cont():
  import os
  import time
  os.system('clear')
  print("As you walk through the mineshaft, you get more tired, thirsty. Your flashlight dies out.")
  time.sleep(2)
  print("At this point, you have walked for 2 hours straight, finding nothing except a small security camera hiding in the wall.")
  b = str(input("You can either turn back and go to the water cave, or continue your forward expedition. Enter 'cave' to go back, and 'walk' to continue trekking."))
  if b == "cave":
    investigate()
  if b == "walk":
    import page4
    page4.walk()
    