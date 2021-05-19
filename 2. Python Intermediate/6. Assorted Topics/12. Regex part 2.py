"""
Shorthand character class       Represents
\d                              Any numeric digit from 0 to 9.
\D                              Any character that is not a numeric digit from 0 to 9.
\w                              Any letter, numeric digit, or the underscore character.
                                (Think of this as matching “word” characters.)
\W                              Any character that is not a letter, numeric digit, or the underscore character.
\s                              Any space, tab, or newline character.
                                (Think of this as matching “space” characters.)
\S                              Any character that is not a space, tab, or newline.

Character(s) 	Meaning
. 	            Matches any single character except newline
^ 	            Anchors a match at the start of a string
                Complements a character class
$ 	            Anchors a match at the end of a string
* 	            Matches zero or more repetitions
+ 	            Matches one or more repetitions
? 	            Matches zero or one repetition
                Specifies the non-greedy versions of *, +, and ?
                Introduces a lookahead or lookbehind assertion
                Creates a named group
{}  	        Matches an explicitly specified number of repetitions
\ 	            Escapes a metacharacter of its special meaning
                Introduces a special character class
                Introduces a grouping backreference
[] 	            Specifies a character class
| 	            Designates alternation
()  	        Creates a group
:               Designate a specialized group
#               Designate a specialized group
=               Designate a specialized group
! 	            Designate a specialized group
<> 	            Creates a named group
"""

import re

lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, ' \
    '7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, ' \
    'and 1 partridge in a pear tree'

xmasRegex = re.compile(r'\d+\s\w+')
xmasList = xmasRegex.findall(lyrics)
print(xmasList)
for i in xmasList:
    print(i)

# # Make your own character class
# vowelRegex = re.compile(r'[aeiouAEIOU]')         # same as r'(a|e|i|o|u|A|E|I|O|U)'
# vowelList = vowelRegex.findall('Ropocop eats baby food.')
# print(vowelList)
#
# doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
# doubleVowelList = doubleVowelRegex.findall('Ropocop eats baby food.')
# print(doubleVowelList)
#
# notVowelRegex = re.compile(r'[^aeiouAEIOU]')         # ^ caret makes it a negative character class
# notVowelList = notVowelRegex.findall('Ropocop eats baby food.')
# print(notVowelList)
#
# # Dot character . (Matches any single character except newline)
# atRegex = re.compile(r'.at')
# atList = atRegex.findall('The cat in the hat sat on the flat mat.')
# print(atList)
#
# atRegex2 = re.compile(r'.{1,2}at')
# atList2 = atRegex2.findall('The cat in the hat sat on the flat mat.')
# print(atList2)
#
# # Dot-star character .* (Matches anything except newline)
# nameRegex = re.compile(r'First name: (.*) Last name: (.*)')
# nameList = nameRegex.findall('First name: Professor Andre Last name: Mariano')
# print(nameList)
#
# piping = 'First name: Jordana Last name: Veiga\nFirst name: Walber Last name: Capaci\nFirst name: Jose Last name: Jean'
# print(piping)
# pipingRegex = re.compile(r'First name: (.*) Last name: (.*)')
# pipingList = pipingRegex.findall(piping)
# print(pipingList)
#
# serve = '<To serve humans> for dinner.>'
# greedy = re.compile(r'<(.*)>')
# print(greedy.findall(serve))
# nongreedy = re.compile(r'<(.*?)>')
# print(nongreedy.findall(serve))
#
# pythonCourse = '4. Flow control\n5. Loops\n6. Lists\n7. Strings'
# print(pythonCourse)
#
# dotStar = re.compile(r'.*')
# print(dotStar.search(pythonCourse))
# print(dotStar.search(pythonCourse).group())
# print(dotStar.findall(pythonCourse))
#
# # re.DOTALL (Makes the . dot match newlines)
# dotStarAll = re.compile(r'.*', re.DOTALL)
# print(dotStarAll.search(pythonCourse))
# print(dotStarAll.search(pythonCourse).group())
# print(dotStarAll.findall(pythonCourse))
#
# # re.IGNORECASE (To make the matching case-insensitive)
# vowelRegex = re.compile(r'[aeiou]')
# vowelRegex2 = re.compile(r'[aeiou]', re.I)
# print(vowelRegex.findall('A.N. loves A.F.'))
# print(vowelRegex2.findall('A.N. loves A.F.'))
#
# # Sub() method - Find and replace
# secret = 'Agent Alice gave the secret documents to Agent John'
#
# agentsRegex = re.compile(r'Agent \w+')
# print(agentsRegex.findall(secret))
# cripto = agentsRegex.sub('REDACTED', secret)
# print(cripto)
#
# agentsRegex2 = re.compile(r'Agent (\w)\w*')
# print(agentsRegex2.findall(secret))
# cripto2 = agentsRegex2.sub(r'Agent \1*****', secret)
# print(cripto2)