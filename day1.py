
def p1(data):
    l1, l2 = [], []
    for line in data.split('\n')[:-1]:
        a, b = line.split('   ')
        l1.append(int(a))
        l2.append(int(b))

    l1.sort()
    l2.sort()

    dist = 0
    for a, b in zip(l1, l2):
        dist += abs(a-b)

    return dist

def p2(data):
    l1, l2 = [], []
    for line in data.split('\n')[:-1]:
        a, b = line.split('   ')
        l1.append(int(a))
        l2.append(int(b))

    freq = {}
    for x in l2:
        if x not in freq:
            freq[x] = 1
        else:
            freq[x] += 1

    sim = 0
    for x in l1:
        if x not in l2:
            continue
        else:
            sim += x * freq[x]

    return sim


def main():
    f = open('input1.txt', 'r')
    data = f.read()
    print(p1(data))
    print(p2(data))

if __name__ == '__main__':
    main()
