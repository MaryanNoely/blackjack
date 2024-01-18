############### Blackjack Project #####################

## Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
##################### Code #####################

from art import logo
import random
from replit import clear


def deal(amount):
  '''Returns a list of random cards based on the amount passed'''
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  return random.sample(cards,k=amount)

def calculate_score(cards):
  '''Return the score of the cards in the list, if return is 0 it means is a Black Jack'''
  score=sum(cards)
  if score==21 and len(cards)==2:
    return 0
  if 11 in cards and score > 21:
    idx= cards.index(11)
    cards[idx]=1
    score=sum(cards)
  return score

def black_jack_game():
  print(logo)
 
  #Initialization
  user_cards = []
  dealer_cards = []
  
  #Deal 2 cards
  user_cards += deal(2)
  dealer_cards += deal(2)
  user_score=calculate_score(user_cards)
  dealer_score=calculate_score(dealer_cards)
  print(f"Your cards: {user_cards}, current score: {user_score}")
  print(f"Computer's first card: {dealer_cards[0]}")
  if user_score ==0:
    print(compare(user_score, dealer_score))
    return
  another_card=input("Type 'y' to get another card, type 'n' to pass: ")

  #Ask user if more cards
  while another_card=="y":
    user_cards += deal(1)
    user_score=calculate_score(user_cards)
    if user_score>21:
      break
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {dealer_cards[0]}")
    another_card=input("Type 'y' to get another card, type 'n' to pass: ").lower()

  #Dealer cards to win or reach 21
  if user_score <=21 and user_score > 0 and dealer_score>0:
    while dealer_score <= user_score and dealer_score < 17:
      dealer_cards += deal(1)
      dealer_score=calculate_score(dealer_cards)

  print(f"Your cards: {user_cards}, final score: {user_score}")
  print(f"Computer's cards: {dealer_cards} final score: {dealer_score}")

  print(compare(user_score, dealer_score))

def compare(user_score, dealer_score):
  '''Present the winner of the round comparing scores'''
  if dealer_score == user_score:
    return "It's a draw"
  elif user_score==0:
    return "Black Jack! You win! XD"
  elif dealer_score == 0:
    return "Dealer wins with Black Jack"
  elif user_score>21:
    return "You lose!"  
  elif dealer_score>21 or dealer_score<user_score:
    return "You win! XD"
  else:
    return "You lose! :'("


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
  clear()
  black_jack_game()


  


  








##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

