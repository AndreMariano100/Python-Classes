"""
pprint.PrettyPrinter(indent, width, depth, stream, compact)
pprint.pprint(<data>)

"""
from pprint import pprint

data = {'First': {'A': 0,
                  'B': 1,
                  'C': 2,
                  'D': 3,
                  'E': 4,
                  'F': 5},
        'Second': {'G': 6,
                   'H': 7,
                   'I': 8,
                   'J': 9},
        'Third': {'K': 10,
                  'L': 11,
                  'M': 12}}

print(data)
pprint(data)
