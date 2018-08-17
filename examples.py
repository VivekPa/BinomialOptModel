from eu_option import euro_option

# example calculation of European Option Price.

option_eu = euro_option(50, 45, 0.05, 1, 2, {'sigma': 0.5})

print(option_eu.price())
