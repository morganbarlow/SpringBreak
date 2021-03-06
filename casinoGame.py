# my casino game will involve a standard deck of 52 card
# you may guess the COLOR for $5
# you may guess the SUIT for $3
# you may guess the NUMBER/FACE for $1

# I need a function that determines how much money they put in the pot,
    # which will determine if their guess will be a color, suit, or number
    # we will then also need to subratct that amount from our players wallet

# I need a function that will take in and keep track of our users guess

from numpy import random

guessByColor = {
  "red cards" : 26,
  "black cards" : 26,
}
list_of_nos = ["no","no thank you", "I'm alright", "I'll pass", "nah", "nope", "not gonna happen", "never", "pass", "not today", "I can't", "no way", "not a chance", "I'd rather not"]

def getWallet (moneyCap) :
  user_wallet = random.randint(moneyCap)
  print(f'How about we start you off with ${user_wallet} for now then.')

def letsPlayAGame (question) :
  user_answer = input(question).lower()
  if user_answer in list_of_nos : {
    print("Well that is too bad.")
  } 
  else : {
    getWallet(input("what's your wallet limit?\n"))
  }
  

letsPlayAGame("Do you wanna play a game?\n")
