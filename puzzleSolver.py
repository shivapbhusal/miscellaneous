'''
Program to Solve puzzles
'''

from itertools import permutations

perm = permutations(list('apple'),5)

words = set()
f = open('/usr/share/dict/words')
for word in f:
    word = word.strip()
    words.add(word.lower())

for item in perm:
    if ''.join(item) in words:
        print(str(''.join(item)))

