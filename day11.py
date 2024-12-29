
def blink(stone):
    if stone == 0:
        return [1]
    elif len(str(stone))%2 == 0:
        s = str(stone)
        return [int(s[:len(s)//2]), int(s[len(s)//2:])]
    else:
        return [stone*2024]

memo = {}
def blinkn(stone, n):
    if n == 0:
        return 1
    
    if (stone, n) in memo:
        return memo[(stone, n)]

    result = 0
    for s in blink(stone):
        result += blinkn(s, n-1)

    memo[(stone, n)] = result
    return result
        

def p1(data):
    stones = data.split(' ')
    stones = [int(x) for x in stones]

    for _ in range(25):
        newstones = []
        for stone in stones:
            newstones += blink(stone)
        stones = newstones

    return len(stones)

def p2(data):
    stones = data.split(' ')
    stones = [int(x) for x in stones]

    no_blinks = 75
    total = 0
    for stone in stones:
        total += blinkn(stone, no_blinks)

    return total


def main():
    f = open('input11.txt', 'r')
    data = f.read()
    print(p1(data))
    print(p2(data))

if __name__ == '__main__':
    main()
