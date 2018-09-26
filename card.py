class Card(object):
	def __init__(self, rank, suit, hidden):
		self.rank = rank
		self.suit = suit
		self.hidden = hidden

	def __str__(self):
		return str(self.rank) + str(self.suit)