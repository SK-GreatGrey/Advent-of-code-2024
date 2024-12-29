
def p1(data):
    safe = 0
    for line in data.split('\n')[:-1]:
        levels = line.split(' ')
        difs = []
        for i in range(1, len(levels)):
            difs.append(int(levels[i]) - int(levels[i-1]))



        mult = 1
        if difs[0] < 0:
            mult = -1

        for d in difs:
            if not 1 <= d*mult <= 3:
                break
        else:
            safe += 1

    return safe

def test(levels):
    difs = []
    for i in range(1, len(levels)):
        difs.append(levels[i] - levels[i-1])
    mult = 1
    if difs[0] < 0:
        mult = -1

    for d in difs:
        if not 1 <= d*mult <= 3:
            break
    else:
        return True

def p2(data):
    safe = 0
    for line in data.split('\n')[:-1]:
        levels = line.split(' ')
        levels = [int(l) for l in levels]
        if test(levels):
            safe += 1
        else:
            for i in range(len(levels)):
                alt_levels = levels.copy()
                alt_levels = alt_levels[:i] + alt_levels[i+1:]
                if test(alt_levels):
                    safe += 1
                    break
        
            


    

    return safe


def main():
    f = open('input2.txt', 'r')
    data = f.read()
    print(p1(data))
    print(p2(data))

if __name__ == '__main__':
    main()
