target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇

number = 0
for num in range(0, target+1, 2):
  number += num
  if number > num:
    num = number
print(num)
