name = 'taki ralph jerome'.split()
name.extend(name)

# Make the items in the list unique
# Approach 1
new_names = []
#print('before:', name)
"""
for n in name:
    if n not in new_names:
        new_names.append(n)

#print('after:', new_names)
"""

# Approach 2
new_names = list(set(name))
#print('after:', new_names)


#print('{}CUSTOM SORTING{}'.format('='*5, '='*5))
vegetables = 'okra sitaw bataw patani'.split()

alpha_sort = sorted(vegetables)
#print(alpha_sort)

rev_sort = sorted(vegetables, reverse=True)
#print(rev_sort)

# Sorts by string length
#print(sorted(vegetables, key=len, reverse=True))

def sort_second(val):
    # passed the value: (0, 'okra')
    return val[1]

"""

veg_ids = [(i, v) for i, v in enumerate(vegetables)]

list_comp = [val for i in seq]

"""

veg_ids = []
for i, v in enumerate(vegetables):
    veg_ids.append(
        (i, v)
    )

#print(sorted(veg_ids, key=sort_second))

records = [
    {'name': 'jay', 'dept': 5},
    {'name': 'ralph', 'dept': 3},
    {'name': 'taki', 'dept': 2},
]

def sort_dept(val):
    return val['dept']

record_names = []
for v in (i for i in records):
    record_names.append(v['name'])
print('record_names:', record_names)
# print('record_names:', [v['name'] for v in records if v['name'].startswith('t')])


#print(records)
#print(sorted(records, key=sort_dept))


print('{}TUPLES{}'.format('='*5, '='*5))
coord = (1234.123, 12356.125)

# Value unpacking
c_x, c_y = coord

print('c_x', c_x)
print('c_y', c_y)







