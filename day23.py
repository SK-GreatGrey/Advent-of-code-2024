def p1(data):
    connections = data.split('\n')[:-1]
    connections = [c.split('-') for c in connections]
    connections += [[b,a] for a,b in connections]
    
    con_dict = {}
    for a, b in connections:
        if a not in con_dict:
            con_dict[a] = set()
        con_dict[a].add(b)

    triples = set()
    for a in con_dict:
        ans = con_dict[a]
        for b in ans:
            bns = con_dict[b]
            for c in ans & bns:
                x = sorted([a,b,c])
                triples.add(tuple(x))

    no_triples = 0
    for a,b,c in triples:
        if 't' in [a[0], b[0], c[0]]:
            no_triples += 1


        
        
    return no_triples
        
    

def p2(data):
    connections = data.split('\n')[:-1]
    connections = [c.split('-') for c in connections]
    #connections += [[b,a] for a,b in connections]
    
    con_dict = {}
    for a, b in connections:
        if a not in con_dict:
            con_dict[a] = set()
        con_dict[a].add(b)
        if b not in con_dict:
            con_dict[b] = set()
        con_dict[b].add(a)

    best = 0
    best_net = None
    for a, b in connections:
        ans = con_dict[a] & con_dict[b]
        ans |= set((a, b))
        
        connected = False
        while not connected:
            internals = {c:len([x for x in ans if x in con_dict[c]]) for c in ans}
            if len(set(internals.values())) == 1:
                connected = True
            else:
                prune = min(internals.values())
                for k in internals.keys():
                    if internals[k] == prune:
                        ans.remove(k)
        if len(ans) > best:
            best = len(ans)
            best_net =  ','.join(sorted(ans))

    return best_net

def main():
    f = open('input23.txt', 'r')
    data = f.read()
    print(p1(data))
    print(p2(data))

if __name__ == '__main__':
    main()



