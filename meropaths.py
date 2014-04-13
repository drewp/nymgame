import itertools, json
from nltk.corpus import wordnet

paths = []
nouns = wordnet.all_synsets('n')
for s in nouns:
    paths.append([s])

def grow_path(paths, p):
    meros = p[-1].part_meronyms()
    if len(meros) == 0:
        return
    elif len(meros) == 1:
        p.append(meros[0])
        grow_path(paths, p)
    else:
        head = p[:]
        for m in meros:
            if m is meros[0]:
                p.append(m)
            else:
                p2 = head[:] + [m]
                paths.append(p2)
                grow_path(paths, p2)

for p in paths:
    grow_path(paths, p)

        
for p in paths:
    if len(p) < 5:
        continue
    words = [syn.name.split('.')[0].replace('_',' ') for syn in p]
    line = json.dumps(words)
    if words[0] == 'united states' or 'america' in line or 'hemisphere' in line:
        continue
    print line
    
