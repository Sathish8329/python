print("Welcome to Treasure Island\nNow you have to find the a big Island and you have to find the treasure in the Island.\n")
direction = input("Do you want to go left or right?\n")
if direction == "right":
  print("Fall into a hole.\nGame Over.")
else:
  swim_wait = input("After turning left you reached the lake? Do you want to swim or wait for a boat?\n")
  if swim_wait == "swim":
    print("Attacked by trout.\nGame Over.")
  else:
    door = input("You have safely landed in Island, which has three doors, select any one to find the treasure eg red, blue, yellow?\n")
    if door == "red":
      print("Burned by fire.\nGame Over")
    elif door == "blue":
      print("Eaten by beasts.\nGame Over.")
    elif door == "yellow":
      print("You Win!")
    else:
      print("Game Over.")
