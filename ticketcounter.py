print("welcome to the ticket counter")
age = int(input("what is your age?\n"))


if age <= 12:
  print("pay Rs 5")
  parents = input("have you been with your parents? yes or no")
  if parents == "yes":
    print("you get a free ticket")
  else:
    print("Sorry pay the full price")
  #else parents == "others":
   # print("Sorry we dont understand")
elif age <= 18:
  print("pay Rs 10")
  girlfriend = input("are you with your girlfriend? yes or no")
  if girlfriend == "yes":
    print("you get a free ticket")
  else:
    print("Sorry pay the full price")
elif age <= 25:
  print("pay Rs 12")
  girlfriend = input("are you with your girlfriend? yes or no")
  if girlfriend == "yes":
    print("you get a free ticket")
  else:
    print("Sorry pay the full price")
elif age <= 30:
  print("pay Rs 15")
  wife = input("are you with your wife? yes or no")
  if wife == "yes":
    print("pay double the price")
  else:
    print("enjoy! its totally free")
else:
  print("pay Rs 18")
