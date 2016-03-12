"""
Expressions

|| or
&& and
! not

PEMDAS

"""
"""
num1 = 5
num2 = 5

if num1 < num2 or (num1 == num2):
    print(num1, 'is less than', num2)
elif num1 > num2:
    print(num1, 'is greater than', num2)
else:
    print('What happened?')
"""


# For loops
# for(i; cond; i++) { code }
# i = 0
fruits = ['apple', 'grapes', 'tomatoes']
for idx, val in enumerate(fruits):
    # print(idx, ':', val)
    pass

fruits2 = [(0, 'apple'), (1, 'grapes'), (2, 'tomatoes')]
for idx, val in fruits2:
    # print(idx, ':', val)
    pass

while fruits2:
    i = fruits2.pop()
    # Code logic to do something with i
