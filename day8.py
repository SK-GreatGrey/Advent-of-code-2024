import itertools

def p1(data):
    rows = data.split('\n')[:-1]
    grid = [list(row) for row in rows]

    symbols = set(data)
    symbols.remove('\n')
    symbols.remove('.')

    height, width = len(rows), len(rows[0])

    antinodes = set()

    for symbol in symbols:
        positions = [(x, y) for y, row in enumerate(rows) for x, c in enumerate(row) if c == symbol]
        for a, b in itertools.combinations(positions, 2):
            ax, ay = a
            bx, by = b

            dx, dy = ax-bx, ay-by

            if 0 <= ax+dx < width and 0 <= ay+dy < height:
                antinodes.add((ax+dx, ay+dy))
            if 0 <= bx-dx < width and 0 <= by-dy < height:
                antinodes.add((bx-dx, by-dy))
        
    return len(antinodes)


def p2(data):
    rows = data.split('\n')[:-1]
    grid = [list(row) for row in rows]

    symbols = set(data)
    symbols.remove('\n')
    symbols.remove('.')

    height, width = len(rows), len(rows[0])

    antinodes = set()

    for symbol in symbols:
        positions = [(x, y) for y, row in enumerate(rows) for x, c in enumerate(row) if c == symbol]
        for a, b in itertools.combinations(positions, 2):
            ax, ay = a
            bx, by = b

            dx, dy = ax-bx, ay-by

            a1x, a1y = ax, ay
            a2x, a2y = bx, by
            
            while 0 <= a1x < width and 0 <= a1y < height:
                antinodes.add((a1x, a1y))
                a1x, a1y = a1x+dx, a1y+dy
                
            while 0 <= a2x < width and 0 <= a2y < height:
                antinodes.add((a2x, a2y))
                a2x, a2y = a2x-dx, a2y-dy
                
    return len(antinodes)

def main():
    f = open('input8.txt', 'r')
    data = f.read()
    print(p1(data))
    print(p2(data))


if __name__ == '__main__':
    main()
