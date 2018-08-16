# BinomialOptModel
This is a simple python program to implement the Binomial Option Pricing Model. 
## Prerequisites
The only python module needed is numpy.
```python
import numpy as np
```
It is possible to do this without the numpy module, but dealing with matrices becomes very tedious without numpy.

## Binomial Option Pricing Model
Now let me explain the theory behind the model. The essential idea behind using the binomial model to price an option is to replicate the option using a combination of stocks and bonds and the value of the portfolio is equivilant to the price of the option. To understand this further, we need to explain a few terms. A more detailed version of the theory will be on ReadTheDocs.

### No Abritrage Condition

Arbitrage is the result of information imbalance, and results in an inefficient market. In particular, arbitrage allow one to increase the value of the portfolio without incurring any risk inherent in stocks. This will result in either the long or short position earning an infinite amount, which is not realistic. This however, does not mean arbitrage does not exist in real markets, but they are short lived. 

For our model, we assume that there is no arbitrage. We will see later that certain conditions result in no arbitrage. 


### Binomial Tree

First, we set up the binomial stock price tree. Given an initial stock price (at current time), we make a model of how the stock is gonna change over time. At every increment of time, the stock can go up or down by a certain factor. This forms the binomial stock price tree. 
-insert diagram-
The no arbitrage criteria means that the value of the portfolio that replicates the return of the option will equal to the price of the option. Therefore, given the return of the option at the end node, we can calculate recursively to find the value of the portfolio at the initial node, which is essentially the price of the option.

## Applying the Theory

The program was built in a few parts. First, I made a class with common attributes of stock options, such as strike price and time of expiry. A second class was built for the European Option, which can only be exercised at the end, and another for the American Option, which can be exercised anytime. Finally, I found the value of the portfolio recursively, solving for the price of the option.
