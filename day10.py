
def score(grid, x, y, height, width):
    horizon = [(x, y)]
    for current in range(1, 10):
        newhorizon = []
        for (x, y) in horizon:
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if 0 <= x+dx < width and 0 <= y+dy < height:
                    newhorizon += [(x+dx, y+dy)]
        newhorizon = [(x, y) for x, y in newhorizon if grid[y][x] == current]

        horizon = newhorizon
    horizon = set(horizon)
    return sum([grid[y][x] == 9 for x, y in horizon])
                

def p1(data):
    rows = data.split('\n')[:-1]
    grid = [[int(x) for x in row] for row in rows]
    height, width = len(grid), len(grid[0])


    total = 0
    
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == 0:
                total += score(grid, x, y, height, width)
    return total

def rate(grid, x, y, height, width):
    horizon = [(x, y)]
    for current in range(1, 10):
        newhorizon = []
        for (x, y) in horizon:
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if 0 <= x+dx < width and 0 <= y+dy < height:
                    newhorizon += [(x+dx, y+dy)]
        newhorizon = [(x, y) for x, y in newhorizon if grid[y][x] == current]

        horizon = newhorizon
    return sum([grid[y][x] == 9 for x, y in horizon])

def p2(data):
    rows = data.split('\n')[:-1]
    grid = [[int(x) for x in row] for row in rows]
    height, width = len(grid), len(grid[0])


    total = 0
    
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == 0:
                total += rate(grid, x, y, height, width)
    return total


def main():
    f = open('input10.txt', 'r')
    data = f.read()
    print(p1(data))
    print(p2(data))


if __name__ == '__main__':
    main()

