"""
Given an array, find the int that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
"""

#My solution, lol not Pythonic at all fml
def find_it(seq):
    l = len(seq)
    count = 0
    for y in seq:
        for x in seq:
            if y == x:
                count += 1
        if count % 2 != 0:
            return y
            break

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))

#correct output = 5

"""
The best solution someone else submitted:

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
"""
