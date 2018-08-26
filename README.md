# BinomialOptModel
This is a python program to price American and European Options using the Binomial Option Pricing Model. 

## Getting Started
This model is not meant to be used to trade real options but it is a good starting point to learn about implementing options pricing in Python. 

If you would like to use it for development or to integrate it into your own model, either clone or download it. 

```
git clone https://github.com/VivekPa/BinomialOptModel
```


## Prerequisites 
This model uses modules such as `pandas`, `numpy`, `pandas_dataframe` and `fix_yahoo_finance`. You can install them using `pip` with the following code:
```
pip install pandas numpy pandas_dataframe fix_yahoo_finance
```

## Preliminary Example
The following is an example of how this model will be implemented to price an option in real time. 

Consider and Apple stock option, with strike price 215, spot price 217.58, risk free interest rate 0.05, time 0.1 and 40 iterations. We analyse the stock price from 2017-08-18 to 2018-08-18 to find the volatility. Now, to price the option, the following code will be executed:

```python
from eu_option import EuroOption

option_eu = EuroOption(
    217.58,
    215,
    0.05,
    0.1,
    40,
    {"tk": "AAPL", "is_cal": True, "start": "2017-08-18", "end": "2018-08-18"},
)

print(option_eu.price())
```

## Key Principles
The binomial model for pricing stock options is a well tested and old model. The following key priciples and objectives have guided me in building this model:

1. Customisation of the model is imperative. 
    + The presence of exotic options require the model be flexible. This is why I have separated each component of the model into classes in different files.
2. Volatility modelling must be improved to predict volatility more accurately. 
    + I have implemented a simple exponentially weighted standard deviation to calculate the volatility from stock price data taken from Yahoo Finance.
3. A key assumption is that volatility will remain relatively constant in the period of our analysis. 
    + Although it is a relatively loose assumption, it is required for the model to work. 



## New Features to be Implemented

I indend to improve this volatility model by implementing new research.

## Overview of Binomial Option Pricing Model
Now let me explain the theory behind the model. Essentially, the idea behind using the binomial model to price an option is to replicate the option using a combination of stocks and bonds and the value of the portfolio is equivilant to the price of the option. To understand this further, we need to explain a few terms.

### No Abritrage Condition

Arbitrage is the result of information imbalance, and results in an inefficient market. In particular, arbitrage allow one to increase the value of the portfolio without incurring any risk inherent in stocks. This will result in either the long or short position earning an infinite amount, which is not realistic. This however, does not mean arbitrage does not exist in real markets, they are just very short lived.

For our model, we assume that there is no arbitrage. We will see later that certain conditions result in no arbitrage. 


### Binomial Tree

First, we set up the binomial stock price tree. Given an initial stock price `S0`, we make a model of how the stock is gonna change over time. At every increment of time, the stock can either go up or down by a certain factor `u` or `d` respectively. This forms the binomial stock price tree. 
-insert diagram-
There is also the risk free interest rate `r`, which is the rate of return on money put in a risk free bond or in a bank. One implication of the no arbitrage criteria is that `d < 1+r < u`. The no arbitrage criteria means that the value of the portfolio that replicates the return of the option will equal to the price of the option. Therefore, given the return of the option at the end node, we can calculate recursively to find the value of the portfolio at the initial node, which is essentially the price of the option.

## Conclusion

Although not a model to beat the market, this model is the best way to learn both about stock option pricing and Python programming. Personally, this project is my first medium scale Python project, so if you enjoyed this or learnt something, don’t forget to leave a star! If you intend to read further about options pricing, I would recommend Stochastic Calculus for Finance I and II by Steven Shreve.