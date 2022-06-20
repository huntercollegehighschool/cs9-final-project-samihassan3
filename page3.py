def punch():
  import os
  import time
  import page5
  os.system('clear')
  print("You strike a blow onto the trolls arm, which does nothing.")
  time.sleep(1)
  print("The troll headbutts you and you fall to the ground while clutching your head. Then, the troll starts dragging you and you lose consciousness.")
  time.sleep(3)
  page5.unconscious()

def kick():
  import os
  import time
  os.system('clear')
  print("You kick the troll square in the jaw, but in doing so, you lost your balance and drop your torch.")
  time.sleep(1)
  print("While both you and the troll are on the ground, the torch starts to set the mineshaft into an inferno, leading to death of the both of you and the troll. Game Over.")
  redo = str(input("Enter E to start again. "))
  if redo == "E" or "e":
    os.system('clear')
    import main
    main.start()

def fire():
  import os
  import page5
  import time
  os.system('clear')
  print("You set fire to the troll and it falls to the ground. It dies and you loot it for a key.")
  time.sleep(1)
  print("Walking forward, you find a keyhole that opens a boulder door. The door opens to a lush wilderness.")
  time.sleep(2)
  page5.escape()

def dodge():
  import os
  import time
  os.system('clear')
  print("You juke the troll, which falls to the ground. However, it quickly gets up and is angrier than ever.")
  time.sleep(1)
  print("It vengefully lunges at you, knocking you out instantly.")
  time.sleep(2)
  import page5
  page5.unconscious()