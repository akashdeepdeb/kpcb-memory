import os
import random

class Card(object):
    def __init__(self, suit, rank, hidden):
        self.suit = suit
        self.rank = rank
        self.hidden = hidden

    def __str__(self):
    	return str(self.suit) + str(self.rank)

def print_letters():
	print('', end=6*' ')
	for i in range(9):
		print(chr(i+97), end=8*' ')
	print('')

def ascii_version_of_card(cards):
	suits_name = ['s', 'd', 'h', 'c', '§']
	suits_symbols = ['\u2660', '\u2666', '\u2665', '\u2663', '§']
	facedown = [['┌─────┐'], ['│░░░░░│'], ['│░░░░░│'], ['│░░░░░│'], ['└─────┘']]
	os.system('clear')
	print('===== ARE YOU READY FOR MEMORY? =====\n')
	print_letters()
	for j in range(6):
		result, lines = [], [[] for i in range(5)]
		for index, card in enumerate(cards[9*j : 9*(j+1)]):
			if card.hidden is not True:
				rank = card.rank[0]
				suit = suits_symbols[suits_name.index(card.suit)]
				faceup = [['┌─────┐'], ['│{}{}   │'.format(rank, ' ')], ['│  {}  │'.format(suit)], ['│   {}{}│'.format(' ', rank)], ['└─────┘']]
				for i in range(5):
					lines[i].append(faceup[i])
			else:
				for i in range(5):
					lines[i].append(facedown[i])

		for index, line in enumerate(lines):
			result.append('  '.join(i[0] for i in lines[index]))
		for i in range(5):
			result[i] = (' ' + str(6-j) + ' ' + result[i] + ' ' + str(6-j) + ' ') if (i == 2) else '   ' + result[i] + '   '
		print('\n'.join(result))
	print_letters()


card_ranks = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
card_suits = ['s', 'h', 'd', 'c']
card_jokers = [Card('§', '§',True), Card('§', '§',True)]
card_list = [Card(j, i, True) for j in card_suits for i in card_ranks] + card_jokers
random.shuffle(card_list)
card_list[23].hidden = False
card_list[42].hidden = False

ascii_version_of_card(card_list)