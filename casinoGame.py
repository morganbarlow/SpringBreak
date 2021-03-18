from numpy import random

list_of_nos = ["no","no thank you", "I'm alright", "I'll pass", "nah", "nope", "not gonna happen", "never", "pass", "not today", "I can't", "no way", "not a chance", "I'd rather not", "n"]


guessByColor = {
  "Black card" : 26,
  "Red card" : 26,
}

guessBySuit = {
  "Clubs" : 13,
  "Diamonds" : 13,
  "Hearts" : 13,
  "Spades" : 13,
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

guessBy = {
  "1" : guessByNumFace,
  "3" : guessBySuit,
  "5" : guessByColor
}
  
def getWallet (moneyCap) :
  user_wallet = random.randint(5,moneyCap)
  print(f'How about we start you off with ${user_wallet} in your stack for now then.')
  
  placeBet(user_wallet)

def userGuess (wallet, houseCard, bet) :
  # print(houseCard)
  
  print(f'${wallet} left in our wallet.')
  user_guess = input("What will your guess be?\n").lower()

  def continueGame(question) :
    letsPlay = input(question)
    print(f'\n********************\nYou have ${user_wallet}\n********************\n')
    if letsPlay in list_of_nos :
      print("Well have a good day.")
    else:  
      placeBet(user_wallet)

  if user_guess in houseCard.lower() :
    print("~~~~~~~~~~~~~~~~~~~~\nCongrats!\n~~~~~~~~~~~~~~~~~~~~\n")
    user_wallet = wallet + guessBy[bet][user_guess]
    print (f'You now have ${user_wallet} to play with.')
    continueGame('Would you like to go another round?\n')
  else: 
    user_wallet = wallet
    print("~~~~~~~~~~~~~~~~~~~~\nNot a winner this round.\n~~~~~~~~~~~~~~~~~~~~")
    continueGame("Would you like to try again?\n")

def ourGame(bet,wallet) :
  if bet == '5' :
    house_card = random.choice(list(guessByColor.keys()))
    user_wallet = wallet - 5
    # print(house_card)
    userGuess(user_wallet,house_card, bet)
  elif bet == '3' :
    house_card = random.choice(list(guessBySuit.keys()))
    user_wallet = wallet - 3
    # print(house_card)
    userGuess(user_wallet,house_card, bet)
  elif bet == '1' :
    house_card = random.choice(list(guessByNumFace.keys()))
    user_wallet = wallet - 1
    # print(house_card)
    userGuess(user_wallet,house_card, bet)
  else :
    user_wallet = wallet
    print("\n\nSorry that wasn't an option.\n\n")
    placeBet(user_wallet)




def placeBet (user_wallet) :
  user_bet = input (f"How much would you like to bet?\n It is ...\n $5 to guess the card color.\n{list(guessByColor.keys())}\n\n $3 to guess the card suit.\n{list(guessBySuit.keys())} \n\n $1 to guess the card number or face.\n {list(guessByNumFace.keys())}\n\n$")

  ourGame(user_bet,user_wallet)
     

def letsPlayAGame (question) :
  letsPlay = input(question).lower()
  if letsPlay in list_of_nos : {
    print("Well that is too bad.")
  }
  else : {
    getWallet(input("what's your wallet limit? (Please enter a whole number)\n$"))
  }
  

letsPlayAGame("Do you wanna play a game?\n")

