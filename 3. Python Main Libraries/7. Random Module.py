from random import *

"""
Method 	            Description
seed() 	            Initialize the random number generator
getstate() 	        Returns the current internal state of the random number generator
setstate() 	        Restores the internal state of the random number generator
getrandbits() 	    Returns a number representing the random bits
randrange() 	    Returns a random number between the given range
randint() 	        Returns a random number between the given range
choice() 	        Returns a random element from the given sequence
choices() 	        Returns a list with a random selection from the given sequence
shuffle() 	        Takes a sequence and returns the sequence in a random order
sample() 	        Returns a given sample of a sequence
random() 	        Returns a random float number between 0 and 1
uniform() 	        Returns a random float number between two given parameters
triangular() 	    Returns a random float number between two given parameters, you can also set a mode parameter to
                    specify the midpoint between the two other parameters

betavariate() 	    Returns a random float number between 0 and 1 based on the Beta distribution (used in statistics)
expovariate() 	    Returns a random float number based on the Exponential distribution (used in statistics)
gammavariate() 	    Returns a random float number based on the Gamma distribution (used in statistics)
gauss() 	        Returns a random float number based on the Gaussian distribution (used in probability theories)
lognormvariate() 	Returns a random float number based on a log-normal distribution (used in probability theories)
normalvariate() 	Returns a random float number based on the normal distribution (used in probability theories)
vonmisesvariate() 	Returns a random float number based on the von Mises distribution (used in directional statistics)
paretovariate() 	Returns a random float number based on the Pareto distribution (used in probability theories)
weibullvariate() 	Returns a random float number based on the Weibull distribution (used in statistics)
"""

# 1. Generate random within range - randrange(self, start, stop=None, step=1) -  excludes the end point
for i in range(30):
    print(randrange(10), end='/')

# 2. Generate random within range - randrange() includes both end point
print()
for i in range(30):
    print(randint(0, 10), end='/')

# 3. Generate random between 0 and 1 - random()
print()
for i in range(30):
    print(round(random(), 2), end='/')

# 4. Generate random between two given values - uniform()
print()
for i in range(30):
    print(round(uniform(5, 6), 2), end='/')

# 5. Generate random respecting a statistical distribution
print()
for i in range(30):
    print(round(gauss(0, 1), 2), end='/')

local_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
# 6. Choose an element from a set
print()
for i in range(10):
    print(choice(local_list), end='/')

# 7. Choose number of elements from a set
print()
for i in range(10):
    print(choices(local_list, k=3), end='/')

# 8. Returns a sample from the set
print()
for i in range(10):
    print(sample(local_list, k=3), end='/')

# 9. Shuffle a list
print()
shuffle(local_list)
print(local_list)
