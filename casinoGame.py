from numpy import random


list_of_nos = ["no","no thank you", "I'm alright", "I'll pass", "nah", "nope", "not gonna happen", "never", "pass", "not today", "I can't", "no way", "not a chance", "I'd rather not"]

def ourGame(bet) :
  guessByColor = {
    "red cards" : 26,
    "black cards" : 26,
  }

  if bet == '5' :
    house_card = random.choice(guessByColor.keys())
    print (house_card)
  else :
    print ("oh rats")

def placeBet (user_wallet) :
  user_bet = input ("How much would you like to bet?\n It is ...\n $5 to guess the color.\n $3 to guess the suit.\n $1 to guess the number or face.\n")

  ourGame(user_bet)
  
  
def getWallet (moneyCap) :
  user_wallet = random.randint(moneyCap)
  print(f'How about we start you off with ${user_wallet} in your stack for now then.')
  
  placeBet(user_wallet)
      

def letsPlayAGame (question) :
  user_answer = input(question).lower()
  if user_answer in list_of_nos : {
    print("Well that is too bad.")
  } 
  else : {
    getWallet(input("what's your wallet limit?\n"))
  }
  

letsPlayAGame("Do you wanna play a game?\n")
