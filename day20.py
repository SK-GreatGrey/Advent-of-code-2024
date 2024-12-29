def p1(data):
    rows = data.split('\n')[:-1]
    grid = [list(row) for row in rows]

    height, width = len(grid), len(grid[0])
    
    start = None
    end = None

    for i, row in enumerate(grid):
        if 'S' in row:
            start = (row.index('S'), i)
        if 'E' in row:
            end = (row.index('E'), i)

    pos = end
    i = 0
    grid[end[1]][end[0]] = i
    while pos != start:
        x, y = pos
        i += 1
        for dx, dy in [(0,1), (1, 0), (-1, 0), (0, -1)]:
            if grid[y+dy][x+dx] in ['.','S']:
                grid[y+dy][x+dx] = i
                pos = (x+dx, y+dy)
                break

    cheats = 0
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == '#':
                continue

            for dx, dy in [(0,1), (1, 0), (-1, 0), (0, -1)]:
                nx, ny = x+2*dx, y+2*dy
                if 0 <= nx < width and 0 <= ny < height:
                    if grid[ny][nx] == '#':
                        continue

                    d = c-grid[ny][nx]-2
                    if d >= 100:
                        cheats += 1



    return cheats
                
                

def p2(data):
    rows = data.split('\n')[:-1]
    grid = [list(row) for row in rows]

    height, width = len(grid), len(grid[0])
    
    start = None
    end = None

    for i, row in enumerate(grid):
        if 'S' in row:
            start = (row.index('S'), i)
        if 'E' in row:
            end = (row.index('E'), i)

    pos = end
    i = 0
    grid[end[1]][end[0]] = i
    while pos != start:
        x, y = pos
        i += 1
        for dx, dy in [(0,1), (1, 0), (-1, 0), (0, -1)]:
            if grid[y+dy][x+dx] in ['.','S']:
                grid[y+dy][x+dx] = i
                pos = (x+dx, y+dy)
                break

    cheats = 0
    max_cheat = 20
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == '#':
                continue

            nx, ny = x, y
            for steps in range(1, max_cheat+1):
                for dx in range(steps):
                    dy = steps-dx
                    for nx, ny in [(x+dx,y+dy), (x+dy,y-dx),(x-dx,y-dy),(x-dy,y+dx)]:
                        if 0 <= nx < width and 0 <= ny < height:
                            if grid[ny][nx] == '#':
                                continue

                            d = c-grid[ny][nx]-steps
                            if d >= 100:
                                cheats += 1


    return cheats

def main():
    f = open('input20.txt', 'r')
    data = f.read()
    print(p1(data))
    print(p2(data))

if __name__ == '__main__':
    main()
