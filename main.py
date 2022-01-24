'''
2. Feladat
A program a pénzfeldobást modellezi. Kérdezze meg a felhasználótól a választását (fej vagy írás), majd adjon tájékoztatást, hogy eltalálta-e!
'''

from random import choice

beker = input('fej vagy iras? ')

lista=['fej','iras']

if beker == choice(lista):
    print('eltalaltad!')
else:
    print('nem talaltad el')
