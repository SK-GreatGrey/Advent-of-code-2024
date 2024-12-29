import re


def p1(data):
    muls = re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)', data)
    total = 0
    for mul in muls:
        a, b = mul[4:-1].split(',')
        total += int(a) * int(b)
    
    return total

def p2(data):
    i = 0
    total = 0
    while True:
        data = data[i:]
        dont = re.search('don\'t\(\)', data)

        if dont is None:
            muls = re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)', data)
        else:
            muls = re.findall('mul\([0-9]{1,3},[0-9]{1,3}\)', data[:dont.span()[0]])
        
        for mul in muls:
            a, b = mul[4:-1].split(',')
            total += int(a) * int(b)


        if dont is None:
            break
        do = re.search('do\(\)', data[dont.span()[1]:])
        if do is None:
            break
        i = do.span()[1]+dont.span()[1]
    return total


def main():
    f = open('input3.txt', 'r')
    data = f.read()
    print(p1(data))
    print(p2(data))

if __name__ == '__main__':
    main()
