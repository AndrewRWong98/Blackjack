############### Blackjack Project #####################

## There is one deck, and cards are removed from the deck as they are drawn.
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
deckCardCounter = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4] #theres four aces, four 2's, etc.
## The cards in the list have equal probability of being drawn.
## The computer is the dealer.

import random
from art import logo
from replit import clear 

def checkCardValidity():  #this function is generally used for drawing cards, and making sure we dont draw 5 of the same card
	cardValidityCheck=False #now we make sure theres actually cards of this in the deck, dont wanna have a hand full of 5 2's in a single deck BJ
	while(cardValidityCheck==False):
				randTemp=random.randint(0,12) #choose a spot in deck list
				if deckCardCounter[randTemp]>0:
					deckCardCounter[randTemp]-=1 #take one of that type of card out
					cardValidityCheck=True #it was a valid card and can be added to player hand
	return randTemp

def blackjack():
	#setting the gamestate
	playerHand=[]
	dealerHand=[]

	#initial player draw
	randTemp=random.randint(0,12)
	playerHand.append(cards[randTemp])
	deckCardCounter[randTemp]-=1 #this line of code subtracts one of that card from the deck, theres 4 kinds of each card (A, 2, 3, J, K, etc.)
	#print(deckCardCounter[randTemp])
	randTemp=random.randint(0,12)
	playerHand.append(cards[randTemp])#player starts with 2 cards
	deckCardCounter[randTemp]-=1 

	#dealer draws initial cards
	randTemp=random.randint(0,12)
	dealerHand.append(cards[randTemp]) #facedown just assumed and program will force first draw
	deckCardCounter[randTemp]-=1
	dealerHand.append("?") #facedown card the dealer always has

	playerSum=playerHand[0]+playerHand[1] #sum of first two cards
	#edge case of 2 aces initial hand
	if playerHand[0]==11 and playerHand[1]==11:
		playerHand[1]=1
		playerSum=playerHand[0]+playerHand[1]

	#print initialgame state
	print(logo)
	#print(f"Your cards: {playerHand}, current score: {playerSum}")
	#print(f"Dealer's first card: {dealerHand}")
	#gameOver=False
	playerBlackjack=False
	playerBust=False
	#two conditions above are hard game overs
	playersTurn=True
	while playersTurn==True: #will handle the player's turn 
		print(f"Your cards: {playerHand}, current score: {playerSum}")
		print(f"Dealer's first card: {dealerHand}")
		playerChoice=input('Choose "Hit" or "Stand" please: ').lower()
		if playerChoice=="hit":
			randTemp=checkCardValidity() #draw a random card, make sure it's valid and not the 5th of its kind value-wise
			drawnCard=cards[randTemp] 
			playerHand.append(drawnCard) #add a card to their hand
			#print(f"adding card {drawnCard}") #debug statement
			playerSum+=playerHand[len(playerHand)-1] #playerSum+= last card in hand, index taken using len()-1
			if playerSum>21: #possible bust, check for ace
				if 11 in playerHand:
					playerHand[playerHand.index(11)]=1 #set ace from 11 to 1
					playerSum=0 #reset and recalculate the new playerSum
					for i in range(len(playerHand)):
						playerSum+=playerHand[i]
				else: #definitely bust
					playersTurn=False
					playerBust=True
			if playerSum==21: #player won or drawn the game, no need to continue
				playersTurn=False
				playerBlackjack=True
				print("Blackjack!")
		else: #assume any other input is them standing
			playersTurn=False
	#end player's turn

	#now Dealer's turn: will draw until dealerHandSum>playerHandSum, if hand is <17, they must take another card
	randTemp=checkCardValidity()
	dealerHand[1]=cards[randTemp] #set the dealer's facedown card to be faceup
	dealerSum=dealerHand[0]+dealerHand[1]
	#print(f"debug dealer just drew card 1")
	if playerBust==True: #dealer just reveals face down card and auto wins		
	#edge case 2 aces != 22
		if dealerHand[0]==11 and dealerHand[1]==11:
			dealerHand[0]=1
			dealerHand[1]=1
			dealerSum=2
		print(f"Your cards: {playerHand}, final score: {playerSum}")
		print(f"Dealer's final hand: {dealerHand}, final score: {dealerSum}")
		print("You bust! You lose :(")
		return
	if dealerSum==21:
		if playerBlackjack==True:
			print(f"Your cards: {playerHand}, final score: {playerSum}")
			print(f"Dealer's final hand: {dealerHand}, final score: {dealerSum}")
			print("Draw! No winners!")
		else:
			print(f"Your cards: {playerHand}, final score: {playerSum}")
			print(f"Dealer's final hand: {dealerHand}, final score: {dealerSum}")
			print("Dealer blackjack! You lose :(")

	#dealer doesnt have blackjack nor playerBust
	#print("now dealersTurn=true")
	dealersTurn=True
	while dealersTurn==True:
		#print("debug start of dealer loop")
		#dealer win
		randTemp=checkCardValidity()
		dealerHand.append(cards[randTemp]) #add hand to dealer 
		dealerSum+=dealerHand[len(dealerHand)-1] #new dealer score 
		#dealer bust?
		if dealerSum >21:
			#print("debug: dealersum>21")
			if 11 in dealerHand:
				dealerHand[dealerHand.index(11)]=1 #set ace from 11 to 1
				dealerSum=0 #reset and recalculate the new dealerSum
				for i in range(len(dealerHand)):
					dealerSum+=dealerHand[i]
			else: #definitely bust
				dealersTurn=False
				print(f"Your cards: {playerHand}, final score: {playerSum}")
				print(f"Dealer's final hand: {dealerHand}, final score: {dealerSum}")
				print("Dealer bust, you win! :)")
		elif dealerSum>16 and dealerSum==playerSum:
			#print("debug dealersum>16 and tie")
			dealersTurn=False
			print(f"Your cards: {playerHand}, final score: {playerSum}")
			print(f"Dealer's final hand: {dealerHand}, final score: {dealerSum}")
			print("Draw! No winners!")
		elif dealerSum>playerSum:
			#print("debug: dealersum>playersum")
			print(f"Your cards: {playerHand}, final score: {playerSum}")
			print(f"Dealer's final hand: {dealerHand}, final score: {dealerSum}")
			print("You lose :(")
			dealersTurn=False
		#print("debug: end of dealer loop")
		#else the loop repeats and the dealer draws a card 
	
#end blackjack()

programOver=False
while programOver==False:
	wantPlayBlackjack=input("Do you want to play a game of BlackJack? Type \"y\" or \"n\": ").lower()
	clear()
	if wantPlayBlackjack=="y":
		blackjack()
	else:
		programOver=True