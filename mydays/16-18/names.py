import random

NAMES = ['arnold schwarzenegger',
 'alec baldwin',
 'bob belderbos',
 'julian sequeira',
 'sandra bullock',
 'keanu reeves',
 'julbob pybites',
 'bob belderbos',
 'julian sequeira',
 'al pacino',
 'brad pitt',
 'matt damon',
 'brad pitt']

splitNAMES = [name.split() for name in NAMES]
backNAMES = [ name[1].title()+' '+name[0].title() for name in splitNAMES    ]
#print(backNAMES)

firstnames = [name.split()[0].title() for name in NAMES]

def gen_pairs():
    while True: # Must include iteration in the function
        pair = ['','']
        while pair[0] == pair[1]:
            pair = random.sample(firstnames, 2)
        yield f'{pair[0]} teams up with {pair[1]}'

pair = gen_pairs()
for _ in range(10):
    print(next(pair))




































#def gen_name():
#    for _ in NAMES:
#        yield random.choice(NAMES)
#
#single = gen_name()
#
#print(next(single))
#
#def gen_pair():
#    yield( next(single).split()[0].title(), 'teams up with', next(single).split()[0].title() )
#
#pairs = gen_pair()
#for _ in range(10):
#    print(_)
#    next(pairs)
