from numpy import random


list_of_nos = ["no","no thank you", "I'm alright", "I'll pass", "nah", "nope", "not gonna happen", "never", "pass", "not today", "I can't", "no way", "not a chance", "I'd rather not"]

def userGuess (wallet, houseCard) :
  # print(houseCard)
  print(f'${wallet} left in our wallet.')
  user_guess = input("What will your guess be?\n")

  def continueGame(wallet, question) :
    letsPlay = input(question)
    
    if letsPlay in list_of_nos :
      print("Well have a good day.")
    else:  
      placeBet(wallet)

  if user_guess in houseCard.lower() :
    print("Congrats!")
    user_wallet = wallet + 10
    print (f'You now have ${user_wallet} to play with.')
    continueGame(user_wallet,'Would you like to go another round?')
  else: 
    print("Not a winner this round.")
    print(user_wallet)
    continueGame(user_wallet, "Would you like to try again?\n")

def ourGame(bet,wallet) :
  guessByColor = {
    "red card" : 26,
    "black card" : 26,
  }

  guessBySuit = {
    "Spade" : 13,
    "Club" : 13,
    "Heart" : 13,
    "Diamond" : 13,
  }

  guessByNumFace = {
    "Ace" : 4,
    "2" : 4,
    "3" : 4,
    "4" : 4,
    "5" : 4,
    "6" : 4,
    "7" : 4,
    "8" : 4,
    "9" : 4,
    "10" : 4,
    "Jack" : 4,
    "Queen" : 4,
    "King" : 4,
  }

  if bet == '5' :
    house_card = random.choice(list(guessByColor.keys()))
    user_wallet = wallet - 5
    print(house_card)
    userGuess(user_wallet,house_card)
  elif bet == '3' :
    house_card = random.choice(list(guessBySuit.keys()))
    user_wallet = wallet - 3
    userGuess(user_wallet,house_card)
  elif bet == '1' :
    house_card = random.choice(list(guessByNumFace.keys()))
    user_wallet = wallet - 1
    userGuess(user_wallet,house_card)
  else :
    print("Sorry that wasn't an option.")



def placeBet (user_wallet) :
  user_bet = input ("How much would you like to bet?\n It is ...\n $5 to guess the card color.\n $3 to guess the card suit.\n $1 to guess the card number or face.\n")

  ourGame(user_bet,user_wallet)
  
  
def getWallet (moneyCap) :
  user_wallet = random.randint(5,moneyCap)
  print(f'How about we start you off with ${user_wallet} in your stack for now then.')
  
  placeBet(user_wallet)
      

def letsPlayAGame (question) :
  letsPlay = input(question).lower()
  if letsPlay in list_of_nos : {
    print("Well that is too bad.")
  }
  else : {
    getWallet(input("what's your wallet limit?\n"))
  }
  

letsPlayAGame("Do you wanna play a game?\n")

