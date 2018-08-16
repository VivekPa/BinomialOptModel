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
	def int_prms(self):
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
	def optionprice(self):
		option = np.zeros([self.M, self.M])
		option[:, self.N] = np.maximum(np.zeros(self.M), (stocktree[:, self.N]-self.K) if self.is_call else (self.K-stocktree[:, self.N]))
		for i in np.arange(self.M-2, -1, -1):
			for j in range(0, i+1):
				option[j, i] = math.exp(-self.r*self.dt) * (self.qu*option[j, i+1]+self.qd*option[j+1, i+1])

		return option[0, 0]
	def price(self):
		self.int_prms()
		self.stocktree()
		payoff = self.optionprice()
		return payoff
