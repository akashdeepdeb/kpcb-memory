from printgame import *
from card import *
from utils import *
import os, time, sys, random



# ACTS AS A FIFO CACHE

class Computer(object):
	def __init__(self, level):
		self.computer_score = 0
		self.all_cards = []
		self.capacity = 3*level
		self.computer_memory = list()

	#updates after every turn
	def get_all_current_cards(self):
		self.hidden_cards = list()
		for idx, card in enumerate(self.all_cards):
			if card.hidden is True:
				self.hidden_cards.append((get_string_loc(idx), card))

	def push_into_memory(self, card1, card2):
		self.computer_memory.append(card1)
		self.computer_memory.append(card2)
		if len(self.computer_memory) > self.capacity:
			while len(self.computer_memory) != self.capacity:
				self.computer_memory.pop(0)

	def print_card_message(self, card, turn):
		print('\nPLAYER 2 JUST FLIPPED THE ' + turn.upper() + ' CARD AT: ' + card)
		if turn == 'first':
			print('\nPLAYER 2\'s NEXT PLAY IS...')

	#play `first` random card from board [NOT MEMORY]
	#check if you have `second` card [IN MEMORY]
		#if so, erase second from memory
		#if not, select `second` random card from board 
			#if match, play both
			#if not match, push both cards into memory and pop 2 others [from queue if full]
	def update_cards(self, new_card):
		for card in self.all_cards:
			if card == new_card[1]:
				card.hidden = False
				break
		self.get_all_current_cards()

	def computer_step(self, curr_card, turn):
		self.update_cards(curr_card)
		DisplaySet(self.all_cards)
		self.print_card_message(curr_card[0], turn)
		add_wait()

	def computer_play(self, all_cards):
		
		print('PLAYER 2 IS THINKING NOW...')
		add_wait()

		self.all_cards = all_cards
		self.get_all_current_cards()
		first = random.choice(self.hidden_cards)

		self.computer_step(first, 'first')

		flag = False
		second = None
		for idx, card in enumerate(self.computer_memory):
			if first[1].rank == card[1].rank and first[1].suit != card[1].suit:
				pop_idx = idx
				second = card
				flag = True
				break

		if flag:
			self.computer_memory.pop(pop_idx)
			self.computer_step(second, 'second')
			return (first[1], second[1])
		else:
			second = random.choice(self.hidden_cards)
			self.computer_step(second, 'second')
			if (second[1].rank == first[1].rank and first[1].suit != card[1].suit) is not True:
				self.push_into_memory(first, second)
			return (first[1], second[1])

