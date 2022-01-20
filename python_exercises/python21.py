import random as rd 

coin = ["h", "t"]
user = input("Type Heads or Tails [h/t]: ")
coin_flip = rd.choice(coin)
if (user.lower() == coin_flip):
    print("You Win!")
    print("You selected: " + user)
    print("The coin also selected: " + coin_flip)
else:
    print("You Lose!")
    print("You selected: " + user)
    print("The coin selected " + coin_flip)


