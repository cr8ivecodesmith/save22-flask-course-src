global NUMZILLA
NUMZILLA = 5

def add(n1, n2=3):
    """
    TODO: Implement this function
    TODO: Implement this yourself
    """
    ans = n1 + n2
    return ans

def add_global(n1, n2=3):
    """Implements a global change

    """
    global NUMZILLA
    NUMZILLA = NUMZILLA + n1 + n2


num1 = 5
#print(add(num1))

#: 4

#print(add(1, 5))
#: 6

#print(add(1, 5) + 5)
#: 11

#print('NUMZILLA TEST')
#print(NUMZILLA)
#: 5

add_global(4, 0)
#print(NUMZILLA)
#: 9



#print('LOCAL SCOPE TEST')
num_loc = 5  # module wide


# python default (pass by ref)
"""
num_loc(local) -------------------> 5
num_loc(module) --------------------^
"""

# creates copy on var manipulation and dereferences old val
"""
num_loc(local) -------------------> 5 + 6
"""

def local_scope():
    num_loc  # module wide num_loc
    num_loc1 = num_loc  # function scope var

    num_loc1 += 5  # attempts to change num_loc in function scope
    #print('module scope', num_loc)
    #print('local_scope', num_loc1)

local_scope()


print('{}PASS-BY-REFERENCE: MUTABLE{}'.format('=' * 5, '=' * 5))

def mod_list(seq):
    print('mod_list [in]:', seq)
    seq.append('new item')
    print('mod_list [out]:', seq)

outer_list = 'apple banana grapes'.split()
print('outer_list [before]:', outer_list)
mod_list(outer_list)
print('outer_list [after]:', outer_list)


print('{}PASS-BY-REFERENCE: IMMUTABLE{}'.format('=' * 5, '=' * 5))

def mod_string(seq):
    print('mod_string [in]:', seq)
    seq += ' (new item)'
    print('mod_string [out]:', seq)

outer_string = 'hello world!'
print('outer_string [before]:', outer_string)
mod_string(outer_string)
print('outer_string [after]:', outer_string)





