import numpy as np
import pandas as pd
import pandas_datareader.data as pdr
import fix_yahoo_finance as yf

yf.pdr_override()


class StockVol:

    def __init__(self, tk, start, end):
        self.tk = tk
        self.start = start
        self.end = end
        all_data = pdr.get_data_yahoo(self.tk, start=self.start, end=self.end)
        self.stock_data = pd.DataFrame(all_data["Adj Close"])
        self.log_return = np.log(self.stock_data) - \
            np.log(self.stock_data.shift(1))

    def mean_sigma(self):
        st = self.log_return.ewm(span=252).std()
        sigma = st.iloc[-1]
        return sigma


if __name__ == "__main__":
    s = StockVol("AAPL", "2015-01-01", "2016-01-01")
    print(s.mean_sigma())
