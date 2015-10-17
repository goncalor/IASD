
""" Defines the information on an Edge of a Graph. """

import sys

class EdgeInfo:

	transType= None
	duration= sys.maxsize
	price= sys.maxsize
	ti= sys.maxsize
	tf= sys.maxsize
	period= sys.maxsize

	def __init__(self, transType, duration, price, ti, tf, period):

		self.transType = transType
		self.duration = duration
		self.price = price
		self.ti = ti
		self.tf = tf
		self.period = period
