# Introduction ================================================================

def isPhoneNumber(text):
    """
    Return True if a text is a US phone number ==> 415-555-0000.
    """

    if len(text) != 12:
        return False        # not phone number sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False    # no area code
    if text[3] != '-':
        return False        # missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False    # no first 3 digits
    if text[7] != '-':
        return False        # missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False    # missing last 4 digits
    return True


print(isPhoneNumber('123-456-7890'))
print(isPhoneNumber('123 456-7890'))

message = 'Call me 415-555-1011 tomorrow, or at 422-555-9999.'

foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print(f'Phone number found: {chunk}')
        foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers.')

# # Regular Expressions (RegEx) ===============================================
#
# import re
#
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#
# # Search method ********
# mo = phoneNumRegex.search(message)
# print(mo)
# print(mo.group())
#
# # Find all method ********
# phoneList = phoneNumRegex.findall(message)
# print(phoneList)
# for phone in phoneList:
#     print(f'Phone number found: {phone}')
#
# # Groups () ********
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search('My number is 415-555-4242')
# print(f'Phone number found: {mo.group()}')
# print(f'Area code: {mo.group(1)}')
# print(f'Phone number: {mo.group(2)}')
# # Literal parentheses \( \)
# phoneNumRegex_2 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
# mo_2 = phoneNumRegex_2.search('My number is (415) 555-4242')
# print(f'Phone number found: {mo_2.group()}')
# print(f'Area code: {mo_2.group(1)}')
# print(f'Phone number: {mo_2.group(2)}')
#
# # Pipe character | ********
# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile lost a wheel.')
# print(mo.group())
# print(mo.group(1))
#
# # Question mark character ? (zero or one repetition) ********
# batRegex = re.compile(r'Bat(wo)?man')    # equals to r'Bat(man|woman)'
# mo = batRegex.search('The adventures of Batman.')
# print(mo.group())
# mo_2 = batRegex.search('The adventures of Batwoman.')
# print(mo_2.group())
# mo_3 = batRegex.search('The adventures of Batwowowowowoman.')
# print(mo_3 == None)
#
# phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('My phone number is 415-555-1234. Call me.')
# print(mo.group())
# mo_2 = phoneNumRegex.search('My phone number is 555-1234. Call me.')
# print(mo_2.group())
#
# # Star character * (zero or more repetitions) ********
# batRegex = re.compile(r'Bat(wo)*man')
# mo = batRegex.search('The adventures of Batman.')
# print(mo.group())
# mo_2 = batRegex.search('The adventures of Batwoman.')
# print(mo_2.group())
# mo_3 = batRegex.search('The adventures of Batwowowowowoman.')
# print(mo_3.group())
#
# # Plus character + (one or more repetitions) ********
# batRegex = re.compile(r'Bat(wo)+man')
# mo = batRegex.search('The adventures of Batman.')
# print(mo == None)
# mo_2 = batRegex.search('The adventures of Batwoman.')
# print(mo_2.group())
# mo_3 = batRegex.search('The adventures of Batwowowowowoman.')
# print(mo_3.group())
#
# # Exactly number of repetitions {} ********
# haRegex = re.compile(r'(Ha){3}')      # equal to r'HaHaHa'
# mo = haRegex.search('She said HaHaHa.')
# print(mo.group())
# mo_2 = haRegex.search('She said HaHaHaHa.')
# print(mo_2.group())
#
# # Range of repetitions {x,y} ********
# haRegex = re.compile(r'(Ha){3,5}')
# mo = haRegex.search('She said HaHaHa.')
# print(mo.group())
# mo_2 = haRegex.search('She said HaHaHaHaHa.')
# print(mo_2.group())
# mo_3 = haRegex.search('She said HaHaHaHaHaHaHaHaHaHaHaHaHaHaHa.')
# print(mo_3.group())
# # {,y} => no minimum number of repetitions
# # {x,} => no maximum number of repetitions
#
# # Greedy and non-greedy (?) matches ********
# digitRegex = re.compile(r'(\d){3,5}')       # greedy (default) => match the longest string possible
# mo = digitRegex.search('1234567890')
# print(mo.group())
# digitRegex_2 = re.compile(r'(\d){3,5}?')    # non-greedy       => match the shortest string possible
# mo_2 = digitRegex_2.search('1234567890')
# print(mo_2.group())
#
# # Groups in findall method ********
# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# phoneList = phoneNumRegex.findall('Call me 415-555-1011 tomorrow, or at 422-555-9999.')
# print(phoneList)
#
# phoneNumRegex_2 = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
# phoneList_2 = phoneNumRegex_2.findall('Call me 415-555-1011 tomorrow, or at 422-555-9999.')
# print(phoneList_2)
