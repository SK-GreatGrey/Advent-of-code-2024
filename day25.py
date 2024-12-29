def tree_add(tree, lock):
    if tree == []:
        tree += ([[] for _ in range(6)])
    
    for i in range(6-lock[0]):
        
        if len(lock) > 1:
            tree_add(tree[i], lock[1:])
        else:
            tree[i] += lock
    
        
    

def p1(data):
    items = data[:-1].split('\n\n')
    keys, locks = [], []

    for item in items:
        settings = [-1 for _ in range(5)]
        for row in item.split('\n'):
            for i, c in enumerate(row):
                settings[i] += c == '#'
        is_key = row == '#####'
        if is_key:
            keys.append(settings)
        else:
            locks.append(settings)


    lock_tree = []
    for lock in locks:
        tree_add(lock_tree, lock)

    no_combos = 0
    for key in keys:
        layer = lock_tree
        for pin in key:
            if layer == []:
                break
            layer = layer[pin]
        else:
            no_combos += len(layer)

    return no_combos

def p2(data):
    return 'A WINNER IS YOU!'

def main():
    f = open('input25.txt', 'r')
    data = f.read()
    print(p1(data))
    print(p2(data))

if __name__ == '__main__':
    main()
