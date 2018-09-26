from card import *
import os
import subprocess as sp

class DisplaySet(object):
	suits_name = ['s', 'd', 'h', 'c', '§']
	suits_symbols = ['\u2660', '\u2666', '\u2665', '\u2663', '§']

	def __init__(self, curr_state, score_array = [], hideScore = True):
		self.curr_state = curr_state
		self.score_array = score_array
		self.show_begin_message()
		self.show_game()
		if False:
			self.cheat_code()
		if not hideScore:
			self.show_score()

	def cheat_code(self):
		for j in range(6):
			for i in self.curr_state[j*9: (j+1)*9]:
				print(i, end=' ') if i.hidden else print('**', end=' ')
			print('\n')


	def show_begin_message(self):
		os.system('clear')
		print('===== CURRENT GAME STATE =====\n')

	def print_letters(self):
		print('', end=6*' ')
		for i in range(9):
			print(chr(i+97), end=8*' ')
		print('')

	def show_game(self):
		facedown = [['┌─────┐'], ['│░░░░░│'], ['│░░░░░│'], ['│░░░░░│'], ['└─────┘']]
		self.print_letters()
		for j in range(6):
			result, lines = [], [[] for i in range(5)]
			for index, card in enumerate(self.curr_state[9*j : 9*(j+1)]):
				if card.hidden is not True:
					rank = card.rank[0]
					suit = self.suits_symbols[self.suits_name.index(card.suit)]
					faceup = [['┌─────┐'], ['│{}{}   │'.format(rank, ' ')], ['│  {}  │'.format(suit)], ['│   {}{}│'.format(' ', rank)], ['└─────┘']]
					for i in range(5):
						lines[i].append(faceup[i])
				else:
					for i in range(5):
						lines[i].append(facedown[i])

			for index, line in enumerate(lines):
				result.append('  '.join(i[0] for i in lines[index]))
			for i in range(5):
				result[i] = (' ' + str(6-j) + ' ' + result[i] + ' ' + str(6-j) + ' ') if (i == 2) else 3*' ' + result[i] + 3*' '
			print('\n'.join(result))
		self.print_letters()

	def show_score(self):
		print('\n ===== CURRENT SCORE =====')
		for idx, score in enumerate(self.score_array):
			print('Player ' + str(idx+1) + '\'s score: ' + str(score))
		print('\n')


class DisplayEndMessage(object):
	def __init__(self, winning_player):
		self.winning_player = winning_player
		self.show_end_message()

	def show_end_message(self):
		pass
