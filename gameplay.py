from printgame import *
from card import *
from computer import *
from utils import *
import os, time, sys

class Game(object):
	def __init__(self, all_cards, num_players, computer_mode, computer_level):
		self.computer_mode = computer_mode
		self.computer_level = computer_level
		self.all_cards = all_cards

		if self.computer_mode is True:
			self.comp_object = Computer(self.computer_level)

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

	def player_move(self):
		DisplaySet(self.all_cards, self.score_array, False)
		first = self.flipper('first')
		print('Nice work! Remember another ' + str(self.rank_map[first.rank]) + ' anywhere? ')
		second = self.flipper('second')
		if self.check_if_match(first, second):
			first_tup = (get_string_loc(get_card_idx(self.all_cards, first)), first)
			second_tup = (get_string_loc(get_card_idx(self.all_cards, second)), second)
			self.comp_object.push_into_memory(first_tup, second_tup)
	
	def check_if_match(self, first, second):
		if self.isMatch(first, second):
			print('GREAT WORK! YOU JUST GOT **10 MORE POINTS!**\nIT\'S YOUR TURN AGAIN! ')
			return True
		else:
			print('AHH! THEY DON\'T MATCH. \nBUT BETTER LUCK NEXT TIME!')
			self.curr_player = (self.curr_player+1)%self.n
			return False

	def begin(self):
		print('ARE YOU READY? LET\'S BEGIN!\nYou are Player 1, the Computer is Player 2.\n')
		while (self.count != 0):
			self.player_move()

			if self.computer_mode is True and self.curr_player == 1:
				while True:
					(first, second) = self.comp_object.computer_play(self.all_cards)
					if self.check_if_match(first, second) is False:
						break

			add_wait()

		self.end_and_announce_winner()

	def flipper(self, turn):
		print('It\'s your turn player ' + str(self.curr_player+1))
		while True:
			card_string = input('Enter the ' + turn + ' unflipped card to flip - \'{a-i}{1-6}\': ')
			card_object = self.getCardObject(card_string.strip())
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
		# TODO CHANGE THIS TO USE THE OTHER CLASS and FUNCTION
		winning_player = self.score_array.index(max(self.score_array))
		winning_score = self.score_array[winning_player]
		DisplayEndMessage(winning_player, winning_score)
