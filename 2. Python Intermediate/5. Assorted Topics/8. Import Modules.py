'''
______________________________________________________________________________________________________________
import X

imports the module X, and creates a reference to that module in the current namespace.
Or in other words, after you’ve run this statement, you can use X.name to refer to things defined in module X.

Example:
    import math
    PI = math.pi
    sin = math.sin(PI)
    cosine = math.cos(PI)

Alternative:
    import math as m
    PI = m.pi
    sin = m.sin(PI)
    cosine = m.cos(PI)

______________________________________________________________________________________________________________
from X import *
from X import a, b, c

imports the module X, and creates references in the current namespace to all public objects defined by
that module (that is, everything that doesn’t have a name starting with “_”).
Or in other words, after you’ve run this statement, you can simply use a plain name to refer to things
defined in module X.
But X itself is not defined, so X.name doesn’t work.
And if name was already defined, it is replaced by the new version.
And if name in X is changed to point to some other object, your module won’t notice.

Example:
    from math import factorial
    result = factorial(5)

    from random import randint, random
    rr = random()
    rr_int = randint(0, 10)

'''
