import math
import numpy as np
import pandas as pd
import pandas_datareader.data as pdr
import fix_yahoo_finance as yf
yf.pdr_override()


class stock_vol:

	def __init__(self, tk, start, end):
		self.tk = tk
		self.start = start
		self.end = end
		all_data = pdr.get_data_yahoo(self.tk, start=self.start, end=self.end)
		self.stock_data = pd.DataFrame(all_data['Adj Close'])
		self.stock_data_2 = np.square(self.stock_data)

	def mean_sigma(self):
		var = np.std(self.stock_data)
		sigma = var[-1]
		return sigma

'''
s = stock_vol('AAPL', '2015-01-01', '2016-01-01')
print(s.mean_sigma())
'''
