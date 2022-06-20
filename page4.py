#Use of this page is optional. If you use code here, make sure either import page4 or from page4 import * appear on your main.py page.
def dive():
  import time
  print("When you jump in, you find that the water is very cold yet calming to the extent that it becomes eerie in a way. You close your eyes and relax, with the water slowly pulling you down until you drown.")
  time.sleep(4)
  import page5
  page5.backroom()

def relax():
  import time
  print("You feel the water tugging at you from below, beckoning you to join it. Soon, you fall asleep and plunge into the water below. You drown in the water and then are pronounced dead.")
  time.sleep(3)
  import page5
  page5.backroom()

def walk():
  import time
  print("You continue walking for 4 days and eventually pass out, but right before, a troll comes out from behind a wall and carries you away.")
  time.sleep(4)
  import page5
  page5.unconscious()