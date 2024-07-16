print("Welcome to Treasure Island")
direction = input("Do you want to go left or right?\n")
if direction == "right":
  print("Fall into a hole.\nGame Over.")
else:
  swim_wait = input("Do you want to swim or wait?\n")
  if swim_wait == "swim":
    print("Attacked by trout.\nGame Over.")
  else:
    door = input("Which door eg red, blue, yellow?\n")
    if door == "red":
      print("Burned by fire.\nGame Over")
    elif door == "blue":
      print("Eaten by beasts.\nGame Over.")
    elif door == "yellow":
      print("You Win!")
    else:
      print("Game Over.")
