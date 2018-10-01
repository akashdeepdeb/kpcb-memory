import time, sys, os

from card import *

def add_wait():
	animation = "|/-\\"
	#animation for 2 seconds
	for i in range(20):
		time.sleep(0.1)
		sys.stdout.write("\r" + animation[i % len(animation)])
		sys.stdout.flush()


def get_card_idx(all_cards, which_card):
	for idx, card in enumerate(all_cards):
		if card == which_card:
			return idx


def get_string_loc(idx):
	return chr(97 + int(idx%9)) + str(6-int(idx/9))