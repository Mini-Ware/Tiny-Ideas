import random
alive = True
res = ""
check = random.randint(1,100)
tries = 0
while alive:
  res = int(input("Guess the number (1-100): "))
  tries = tries + 1
  if check == res:
    alive = False
    print("Thats correct! You took "+str(tries)+" attempts.")
  elif check > res:
    print("Higher!")
  elif check < res:
    print("Lower!")
