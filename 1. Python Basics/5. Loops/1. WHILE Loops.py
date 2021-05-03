#######################################################
# The WHILE loop
#
# while <test-condition-is-true>:
#   statement or statements

# Simple WHILE loop
x = 0
while x < 10:
    print(x, end=', ')
    x += 1
# prints: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,

# WHILE loop with BREAK
x = 0
while x < 10:
    print(x, end=', ')
    x += 1
    if x == 5:
        break
# prints: 0, 1, 2, 3, 4,

# WHILE loop with CONTINUE
x = 0
while x < 10:
    x += 1
    if x % 2 == 0:
        continue
    print(x, end=', ')
# prints: 1, 3, 5, 7, 9,

# WHILE loop with CONTINUE and ELSE
x = 0
while x < 10:
    x += 1
    if x % 2 == 0:
        continue
    print(x, end=', ')
else:
    print('List has finished')
# prints: 1, 3, 5, 7, 9, List has finished
# "else" wont execute if the loop has been "broken"
