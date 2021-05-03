# List Comprehension Part 2

'''
List comprehension is more Pythonic than loops and map to create lists.
The main advantage is related to the possibility to apply mapping and filtering in only one tool.
'''
# Adding filttering to List Comprehension
sentence = 'Iron Maiden is the best band ever.'
vowels = [i for i in sentence.lower() if i in 'aeiou']
print(vowels)

# Or even more complex functions
def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

consonants = [i for i in sentence if is_consonant(i)]
print(consonants)

# You can apply conditional inputs to your list
original_price = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
print(original_price)
price = [i if i > 0 else 0 for i in original_price]
print(price)

# Or other functions for conditional inputs
def get_price(price):
    return price if price > 0 else 0

prices = [get_price(i) for i in original_price]
print(prices)