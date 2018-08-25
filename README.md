# BinomialOptModel
This is a simple python program to implement the Binomial Option Pricing Model. 

## Getting Started
This model is not meant to be used to trade real options but it is a good starting point to learn about implementing options pricing in Python. 

If you would like to use it for development or to integrate it into your own model, either clone or download it. 

```
git clone https://github.com/VivekPa/BinomialOptModel
```


## Prerequisites 
This model uses modules such as `pandas`, `numpy`, `pandas_dataframe`.


## Binomial Option Pricing Model
Now let me explain the theory behind the model. Essentially, the idea behind using the binomial model to price an option is to replicate the option using a combination of stocks and bonds and the value of the portfolio is equivilant to the price of the option. To understand this further, we need to explain a few terms. A more detailed version of the theory will be on ReadTheDocs.

### No Abritrage Condition

Arbitrage is the result of information imbalance, and results in an inefficient market. In particular, arbitrage allow one to increase the value of the portfolio without incurring any risk inherent in stocks. This will result in either the long or short position earning an infinite amount, which is not realistic. This however, does not mean arbitrage does not exist in real markets, they are just very short lived.

For our model, we assume that there is no arbitrage. We will see later that certain conditions result in no arbitrage. 


### Binomial Tree

First, we set up the binomial stock price tree. Given an initial stock price `S0`, we make a model of how the stock is gonna change over time. At every increment of time, the stock can either go up or down by a certain factor `u` or `d` respectively. This forms the binomial stock price tree. 
-insert diagram-
There is also the risk free interest rate `r`, which is the rate of return on money put in a risk free bond or in a bank. One implication of the no arbitrage criteria is that $d<1+r<u$ The no arbitrage criteria means that the value of the portfolio that replicates the return of the option will equal to the price of the option. Therefore, given the return of the option at the end node, we can calculate recursively to find the value of the portfolio at the initial node, which is essentially the price of the option.

## Applying the Theory

The program was built in a few parts. First, I made a class with common attributes of stock options, such as strike price and time of expiry. A second class was built for the European Option, which can only be exercised at the end, and another for the American Option, which can be exercised anytime. Finally, I found the value of the portfolio recursively, solving for the price of the option.
