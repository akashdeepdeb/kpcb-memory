# first set all the cards here and the state changes with every step of the game

# add the cross product of all cards and then append the 2 jokers to this list

# shuffle these cards 

# gameplay begins right after this

# ask current player how many players in the game
# 	- if 1-5 players, play normally. 
#	- if 1 player, add computer as player and enter godmode (optional)

# get player names and start game by having a scoreboard 

# keep track of how many cards have been turned and calculate scores accordingly

# when all cards have been turned, end game and output winner

from card import *
from gameplay import *
import random
import os
import subprocess as sp

def main():
	card_ranks = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
	card_suits = ['s', 'h', 'd', 'c']
	card_jokers = [Card('§', '§',True), Card('§', '§',True)]
	card_list = [Card(i, j, True) for j in card_suits for i in card_ranks] + card_jokers
	random.shuffle(card_list)
	os.system('clear')
	# ask how many players the user wants to play with from 2-5
	n = int(input('===== WELCOME TO THE MEMORY GAME HUMANS, ROBOTS AND MOCHI =====\nHow many players would like to play memory today? '))

	start = Game(card_list, n)

main()