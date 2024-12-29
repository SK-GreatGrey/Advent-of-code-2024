memo = {}
def match(patterns, target):
    if target == '':
        return True
    
    if target in memo:
        return memo[target]

    possible = False
    for pattern in patterns:
        if pattern == target[:len(pattern)]:
            possible = match(patterns, target[len(pattern):])

        if possible:
            break

    memo[target] = possible
    return possible

memo2 = {}
def match_all(patterns, target):
    if target == '':
        return 1
    
    if target in memo2:
        return memo2[target]

    possible = 0
    for pattern in patterns:
        if pattern == target[:len(pattern)]:
            possible += match_all(patterns, target[len(pattern):])


    memo2[target] = possible
    return possible

def p1(data):
    patterns, targets = data.split('\n\n')
    patterns = patterns.split(', ')
    targets = targets.split('\n')[:-1]

    total = 0
    for target in targets:
        total += match(patterns, target)

    return total

def p2(data):
    patterns, targets = data.split('\n\n')
    patterns = patterns.split(', ')
    targets = targets.split('\n')[:-1]

    total = 0
    for target in targets:
        total += match_all(patterns, target)

    return total

def main():
    f = open('input19.txt', 'r')
    data = f.read()
    print(p1(data))
    print(p2(data))

if __name__ == '__main__':
    main()
