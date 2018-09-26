from printgame import *
from card import *
import os
import time
import sys

#	os.system('clear')


class Game(object):
	def __init__(self, all_cards, num_players):
		self.all_cards = all_cards
		self.n = num_players
		self.curr_player = 0
		self.score_array = [0 for i in range(self.n)]
		self.count = 54
		self.rank_map = {
		'A':'Ace',
		'2':'Two',
		'3':'Three',
		'4':'Four',
		'5':'Five',
		'6':'Six',
		'7':'Seven',
		'8':'Eight',
		'9':'Nine',
		'T':'Ten',
		'J':'Jack',
		'Q':'Queen',
		'K':'King',
		'§':'Joker'
		}
		self.begin()

	def begin(self):
		animation = "|/-\\"
		while (self.count != 0):
			DisplaySet(self.all_cards, self.score_array, False)
			first = self.flipper('first')
			print('Nice work! Remember another ' + str(self.rank_map[first.rank]) + ' anywhere? ')
			second = self.flipper('second')
			if self.isMatch(first, second):
				print('GREAT WORK! YOU JUST GOT **10 MORE POINTS!**')
			else:
				print('AHH! THEY DON\'T MATCH. \nBUT BETTER LUCK NEXT TIME!')

			#animation for 3 seconds
			for i in range(30):
				time.sleep(0.1)
				sys.stdout.write("\r" + animation[i % len(animation)])
				sys.stdout.flush()

			self.curr_player = (self.curr_player+1)%self.n

		self.end_and_announce_winner()

	def flipper(self, turn):
		print('It\'s your turn player ' + str(self.curr_player+1))
		while True:
			card_string = input('Enter the ' + turn + ' unflipped card to flip - \'{a-i}{1-6}\': ')
			card_object = self.getCardObject(card_string)
			if self.canFlipCard(card_object):
				DisplaySet(self.all_cards)
				return card_object

		
	def isMatch(self, first, second):
		if first.rank == second.rank:
			self.calculate_score(self.curr_player)
			self.count -= 2
			return True
		first.hidden = True
		second.hidden = True
		return False
		

	def getCardObject(self, card):
		while True:
			if len(card) == 2 and 'a' <= card[0] <= 'i' and '1' <= card[1] <= '6':
				col = ord(card[0])-97
				row = 6-int(card[1])
				if 0 <= col < 9 and 0 <= row < 6: 
					return self.all_cards[row * 9 + col]
			else:
				card = input('Enter a valid position: ')

	def canFlipCard(self, card):
		if card.hidden is False:
			print('Already flipped. Flip another card. ')
			return False
		card.hidden = False
		return True


	def calculate_score(self, curr_player):
		self.score_array[curr_player]+=10


	def end_and_announce_winner(self):
		# CHANGE THIS TO USE THE OTHER CLASS and FUNCTION
		winning_idx = self.score_array.index(max(self.score_array))
		print('\nThe winner had a whopping score of ' + str(self.score_array[winning_idx]) + '! ')
		print('*** CONGRATULATIONS TO PLAYER ' + str(winning_idx+1) + '! ***\n*** YOU HAVE A VERY SHARP MEMORY! ***')

