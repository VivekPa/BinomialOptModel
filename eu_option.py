import numpy as np
from stock_option import stockoption
import math


class euro_option(stockoption):
	'''
	calculate required preliminary parameters:
	u = factor change of upstate
	d = factor change of downstate
	qu = risk free upstate probability
	qd = risk free downstate probability
	M = number of nodes
	'''
	def __int_prms__(self):
		self.M = self.N + 1
		self.u = math.exp(self.sigma*math.sqrt(self.dt))
		self.d = 1./self.u
		self.qu = (math.exp((self.r-self.div)*self.dt)-self.d)/(self.u-self.d)
		self.qd = 1-self.qu

	def stocktree(self):
		stocktree = np.zeros([self.M, self.M])
		for i in range(self.M):
			for j in range(self.M):
				stocktree[j, i] = self.S0*(self.u**(i-j))*(self.d**j)
		return stocktree

	def option_price(self, stocktree):
		option = np.zeros([self.M, self.M])
		if self.is_call:
			option[:, self.M-1] = np.maximum(np.zeros(self.M), (stocktree[:, self.N] - self.K))
		else:
			option[:, self.M-1] = np.maximum(np.zeros(self.M), (self.K - stocktree[:, self.N]))
		return option

	def optpricetree(self, option):
		for i in np.arange(self.M-2, -1, -1):
			for j in range(0, i+1):
				option[j, i] = math.exp(-self.r*self.dt) * (self.qu*option[j, i+1]+self.qd*option[j+1, i+1])
		return option

	def begin_tree(self):
		stocktree = self.stocktree()
		payoff = self.option_price(stocktree)
		return self.optpricetree(payoff)

	def price(self):
		self.__int_prms__()
		self.stocktree()
		payoff = self.begin_tree()
		return payoff[0, 0]


euoption = euro_option(50, 45, 0.05, 1, 2, {'sigma': 0.5}) # example test

print(euoption.price())
