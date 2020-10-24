import itertools

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
locations = 'DE ES AUS NL BR US'.split()
confirmed = [False, True, True, False, True]
nam_iter = itertools.cycle(names)

def get_attendees():
    #for participant in zip(names, locations, confirmed):
    #    print(participant)
    
    for i, name in enumerate(names):
        n = next(nam_iter)
        #print(n)
        if i > len(locations)-1:
            l = '-'
        else:
            l = locations[i]
            #print(l)
        if i > len(confirmed)-1:
            c = '-'
        else:
            c = confirmed[i]
            #print(c)
        participant = (n, l, c)
        print(participant)

if __name__ == '__main__':
    get_attendees()
