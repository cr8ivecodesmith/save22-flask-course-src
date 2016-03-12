record = {'name': 'agnes', 'dept': 1}

records = [
    {'name': 'jay', 'dept': 5},
    {'name': 'jay', 'dept': 5},
    {'name': 'jay', 'dept': 5},
    {'name': 'ralph', 'dept': 3},
    {'name': 'taki', 'dept': 2},
]

name_count = {}
for k in records:
    # Noticed how `in` works for dictionaries?
    if k.get('name') in name_count:
        name_count[k.get('name')] += 1
    else:
        name_count[k.get('name')] = 1
print('name_count', name_count)


print(record['name'])
print(record.get('name'))
# print(record['age'])
print('using get:', record.get('age', 'age is not set'))

"""
print('before:', record)
del record['dept']
print('after:', record)
"""

print('keys:', [i for i in record.keys()])
print('values:', [i for i in record.values()])

for v in record.items():
    # print(k, ':', v)
    print(v)

