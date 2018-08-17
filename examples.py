from eu_option import euro_option

option_eu = euro_option(50, 45, 0.05, 1, 2, {'tk': 'AAPL', 'is_cal': True, 'start': '2017-01-01',
                                             'end': '2018-01-01'})

print(option_eu.price())
