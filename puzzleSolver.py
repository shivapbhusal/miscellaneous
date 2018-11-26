'''
Program to Solve puzzles
'''

from itertools import permutations

perm = permutations(list('apple'),5)

words = []
f = open('/usr/share/dict/words')
for word in f:
    word = word.strip()
    words.append(word)

for item in perm:
    if str(item) in words:
        print(str(item))

