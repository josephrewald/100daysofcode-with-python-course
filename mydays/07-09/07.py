NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    NMS_NODUB = []
    [NMS_NODUB.append(x) for x in names if x not in NMS_NODUB]
    
    NMS_CAPS = []
    for name in NMS_NODUB:
        NMS_CAPS.append(name.title())
    
    return NMS_CAPS

def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    names.sort(reverse=True, key=lambda s: s.split()[1])
    return names


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)

    shortest = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    for name in names:
        first = name.split()[0]
        if len(first) < len(shortest):
            shortest = first
    return shortest

print(sort_by_surname_desc(NAMES))
print(shortest_first_name(NAMES))
