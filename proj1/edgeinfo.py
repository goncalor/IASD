
""" Defines the information on an Edge of a Graph. """

class EdgeInfo:

	def __init__(self, transType, duration, price, ti, tf,
			period):

		self.transType = transType
		self.duration = duration
		self.price = price
		self.ti = ti
		self.tf = tf
		self.period = period
