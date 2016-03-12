"""
try:
    statement
except [Exception]:
    statement
"""
import pdb

record = {'name': 'agnes', 'dept': 1}

try:
    loc = (1235.123, 4544.234)
    loc[0] = 432
    num = 1 + '2'
    record['age']
except KeyError:
    #: cause a KeyError
    print('Key {} does not exist'.format('age'))
# except TypeError:
#     print('You can not add a string to a number')
except Exception as err:
    pdb.set_trace()
    print('Something went wrong but I do not know what')
