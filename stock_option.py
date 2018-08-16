import math

class stockoption():

	def __init__(self, S0, K, r, T, N, prm):
		'''
		S0 = initial stock price
		K = strike price
		r = risk free interest rate per annum
		T = length of option in years
		N = number of binomial iterations
		prm = dictionary with additional parameters
		'''
		self.S0 = S0
		self.K = K
		self.r = r
		self.T = T
		self.N = N
		'''
		further parameters:

		div = dividend paid
		sigma = volatility of stock
		is_call = call or put option
		eu_option = European or American option
		'''
		self.div = prm.get('div', 0)
		self.sigma = prm.get('sigma', 0)
		self.is_call = prm.get('is_call', True)
		self.eu_option = prm.get('eu_option', True)

		'''
		derived values:

		dt = time per step, in years
		df = discount factor
		'''
		self.dt = T/float(N)
		self.df = math.exp(-(r-self.div)*self.dt)

	