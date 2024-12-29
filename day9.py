

def p1(data):
    data = [int(x) for x in list(data[:-1])]

    i, j = 0, 0
    isfile = True
    total = 0
    s = ""
    
    while len(data) > 0:
        
        if data[0] == 0:
            i += 1
            data.pop(0)
            isfile = not isfile
            continue

        else:
            data[0] -= 1
            if isfile:
                total += (i//2)*j
                s+=str(i//2)
            else:
                if len(data)%2==1:
                    data.pop(-1)
                    if len(data) == 0:
                        break
                if data[-1] == 0:
                    data[0] += 1
                    data.pop(-1)
                    continue
                else:
                    total += ((i+len(data)-1)//2)*j
                    s+=str((i+len(data)-1)//2)
                    data[-1] -= 1

        j += 1
            
    return total

def printfiles(data, values):
    for i, (a, b) in enumerate(zip(data, values)):
        b = str(b) if b <= 9 else chr(ord('a')+b-10)
        print(b*a if i % 2 == 0 else '.'*a, end='')
    print()

def p2(data):
    data = [int(x) for x in list(data[:-1])]
    values = [n for n in range(len(data)//2+1) for _ in range(2)]
    
    
    i, j = 1, len(data)-1
    mj = j
    adds = 0

    while i <= j:
        while i <= j:
            if data[i] >= data[j]:
                data[i] -= data[j]
                data = data[:i] + [0, data[j]] + data[i:]
                values = values[:i] + [values[j]]*2 + values[i:]
                data[j+1] += data[j+2]
                data[j+2] = 0
                adds += 1
                j += 2
                break
            else:
                i += 2
        j -= 2
        i = 1


    index = 0
    total = 0
    for i, (d, v) in enumerate(zip(data, values)):
        if i%2 == 0:
            for _ in range(d):
                total += index*v
                index += 1
        else:
            for _ in range(d):
                index += 1

    return total


def main():
    f = open('input9.txt', 'r')
    data = f.read()
    print(p1(data))
    print(p2(data))


if __name__ == '__main__':
    main()

