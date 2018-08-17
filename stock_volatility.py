import math
import pandas as pd
import pandas_datareader.data as pdr
import fix_yahoo_finance as yf
yf.pdr_override()


class stock_vol:

	def get_data(self, tk, start, end):
		all_data = pdr.get_data_yahoo(tk, start=start, end=end)
		stock_data = pd.DataFrame(all_data['Adj Close'])
		return stock_data

	def exp_sigma(self, stock_data):
		stock_data_2 = stock_data**2
		sigma = math.sqrt((stock_data_2.ewm(span=252).mean()-stock_data.ewm(span = 252).mean())*252)
		return sigma
	
	def mean_sigma(self):
		stock_data_2 = stock_data**2
		sigma = math.sqrt((stock_data_2.mean()-stock_data.mean())*252)
		return sigma
