import itertools, json, random
from nltk.corpus import wordnet

def synwords(w):
    return set([s.name.split('.')[0] for s in wordnet.synsets(w)]) - set([w])

def find_paths(w):
    ret = []
    syns = synwords(w)
    for sw in syns:
        print "%s -> %s" % (w, sw)
        if sw == w:
            continue
        more = find_paths(sw)
        print 'more', more
        if len(more) == 0:
            ret.append([syns, sw])
        else:
            for tail in more:
                if w in tail:
                    continue
                ret.append([w] + tail)
    return ret

#for p in find_paths('dog'):
#    print p

syntree = {}
syntree['dog'] = synwords('dog')
for loop in range(100):
    for v in syntree.values():
        for w in v:
            if w not in syntree:
                syntree[w] = synwords(w)
print json.dumps(dict((k, sorted(v)) for k,v in syntree.iteritems()))

# path = [('dog', synwords('dog')),
#         ('frank', synwords('frank')),
#         ('blunt', synwords('blunt')),
#         ('dull', synwords('dull')),
#         ('dense', synwords('dense')),
# ]
# print path
