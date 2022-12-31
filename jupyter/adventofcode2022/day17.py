#!/usr/bin/env python
# coding: utf-8

# # Day 17
# 
# https://adventofcode.com/2022/day/17
# 
# ## Part 1

# In[1]:


test_data = """\
>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""
test_data


# In[2]:


from itertools import cycle

def get_shape(idx, y):
    idx = idx % 5
    # ..++++.
    if idx == 0: 
        return [(i+2, y) for i in range(4)]
    # ...+...
    # ..+++..
    # ...+...
    elif idx == 1: 
        return [(3, y+2), (3, y)] + [(i+2, y+1) for i in range(3)]
    # ....+..
    # ....+..
    # ..+++..
    elif idx == 2:
        return [(4, y+2), (4, y+1)] + [(i+2, y) for i in range(3)]
    # ..+....
    # ..+....
    # ..+....
    # ..+....
    elif idx == 3:
        return [(2, y+i) for i in range(4)]
    # ..++...
    # ..++...
    elif idx == 4:
        return [(2+i, y+j) for i in range(2) for j in range(2)]
    assert False

def move_left(shape):
    if any([_x[0] <= 0 for _x in shape]):
        return shape
    else:
        return set([(x-1, y) for x, y in shape])

def move_right(shape):
    if any([_x[0] >= 6 for _x in shape]):
        return shape
    else:
        return set([(x+1, y) for x, y in shape])

def move_down(shape):
    return set([(x, y-1) for x, y in shape])

def move_up(shape):
    return set([(x, y+1) for x, y in shape])


def solution1(data, N=2022):
    jets = cycle(data)
    space = set([(x, 0) for x in range(7)])
    top = 0
    for i in range(N):
        s = set(get_shape(i, top+4))
        #print("new shape:", s)
        while True:
            jet = next(jets)

            if jet == "<":
                s = move_left(s)
                if s & space: # check for collision 
                    s = move_right(s) # undo
            else:
                s = move_right(s)
                if s & space:
                    s = move_left(s)
            s = move_down(s)
            if s & space:
                space |= move_up(s)
                top = max([_x[1] for _x in space])
                break
    print("Solution:", top)
    return top

sol1 = solution1(test_data)
assert sol1 == 3068
print("test passed")


# In[3]:


with open("day17.txt") as f:
    inp_data = f.read()

sol1 = solution1(inp_data)
assert sol1 == 3163
print("test passed")


# ## Part 2

# In[ ]:


print("Part 2")
N = 1000000000000
sol2 = solution1(test_data, N=N)

assert sol2 == 1514285714288
print("test passed")


# In[ ]:


import time
_t = time.time()
sol2 = solution1(inp_data, N=N)
print("elapsed time:", time.time() - _t)
assert sol2 == 3015
print("test passed")


# In[ ]:




