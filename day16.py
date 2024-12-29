import queue, copy

def showpath(grid, path):
    total = 0
    for i, row in enumerate(grid):
        s = ""
        for j, c in enumerate(row):
            s += c if (j,i) not in path else 'X'
        print(s)
        total += s.count('X')
    print(total)
    
        

def p1(data):
    rows = data.split('\n')[:-1]
    grid = [list(row) for row in rows]

    sx, sy = 0, 0
    ex, ey = 0, 0

    for i, row in enumerate(rows):
        for j, c in enumerate(row):
            if c == 'S':
                sx, sy = j, i
            elif c == 'E':
                ex, ey = j, i

    horizon = queue.PriorityQueue()
    horizon.put((0, 0, sx, sy, 1, 0, []))
    visited = set()
    result = 1000000000000
    while not horizon.empty():
        f, g, x, y, dx, dy, path = horizon.get()
        if (x, y, dx, dy) in visited:
            continue
        else:
            visited.add((x, y, dx, dy))

        if f > result:
            continue
        if (x, y) == (ex, ey):
            result = min(result, g)
            continue

        nx, ny = x+dx, y+dy
        if grid[ny][nx] != '#':
            h = abs(ex-nx)+abs(ey-ny)
            horizon.put((g+h+1, g+1, nx, ny, dx, dy, path+[(x, y)]))

        h = abs(ex-x)+abs(ey-y)
        g += 1000
        horizon.put((g+h, g, x, y, dy, dx, path+[(x, y)]))
        horizon.put((g+h, g, x, y, -dy, -dx, path+[(x, y)]))

    return result

def p2(data):
    rows = data.split('\n')[:-1]
    grid = [list(row) for row in rows]

    sx, sy = 0, 0
    ex, ey = 0, 0

    for i, row in enumerate(rows):
        for j, c in enumerate(row):
            if c == 'S':
                sx, sy = j, i
            elif c == 'E':
                ex, ey = j, i


    horizon = queue.PriorityQueue()
    horizon.put((0, 0, sx, sy, 1, 0, []))
    visited = {}
    alt_paths = {}
    result = 1000000000000
    best_path = []
    while not horizon.empty():
        f, g, x, y, dx, dy, path = horizon.get()

        if (x, y, dx, dy) in visited:
            if g == visited[(x, y, dx, dy)]:
                if (x, y, dx, dy) not in alt_paths:
                    alt_paths[(x, y, dx, dy)] = set()
                alt_paths[(x, y, dx, dy)] |= set(path)
            continue
        else:
            visited[(x, y, dx, dy)] = g
            
        if f > result:
            continue
        if (x, y) == (ex, ey):
            path.append((x, y, dx, dy))
            if g < result:
                best_path = path
                result = g
            continue

        
        nx, ny = x+dx, y+dy
        if grid[ny][nx] != '#':
            h = abs(ex-nx)+abs(ey-ny)
            horizon.put((g+h+1, g+1, nx, ny, dx, dy, path+[(x, y, dx, dy)]))

        h = abs(ex-x)+abs(ey-y)
        g += 1000
        horizon.put((g+h, g, x, y, dy, dx, path+[(x, y, dx, dy)]))
        horizon.put((g+h, g, x, y, -dy, -dx, path+[(x, y, dx, dy)]))

    to_check = set(copy.copy(best_path))
    all_paths = set()
    while len(to_check) > 0:
        step = to_check.pop()
        all_paths.add(step)
        if step in alt_paths:
            to_check |= alt_paths[step]-all_paths
            all_paths |= alt_paths[step]
    
    return len(set((x,y) for x, y, _, _ in all_paths))

def main():
    f = open('input16.txt', 'r')
    data = f.read()
    print(p1(data))
    print(p2(data))

if __name__ == '__main__':
    main()
