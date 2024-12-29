import copy

rotations = list('^>v<')
movement = {'^':(-1, 0), '>':(0, 1), 'v':(1, 0), '<':(0, -1)}

def move(grid, x, y, d):

    height, width = len(grid), len(grid[0])
    
    dy, dx = movement[d]
    ny, nx = y+dy, x+dx
    if not (0 <= ny < height and 0 <= nx < width):
        blocked = False
    else:
        blocked = (grid[ny][nx] == '#')
    if blocked:
        d = rotations[(rotations.index(d) + 1)%4]
    else:
        y, x = ny, nx
    return x, y, d

def p1(data):
    rows = data.split('\n')[:-1]
    grid = [list(row) for row in rows]

    x, y = 0, 0
    d = ''
    
    for i, row in enumerate(grid):
        for c in rotations:
            if c in row:
                d = c
                y = i
                x = row.index(c)

    height, width = len(grid), len(grid[0])

    while 0 <= y < height and 0 <= x < width:
        grid[y][x] = 'X'
        x, y, d = move(grid, x, y, d)
        
    total = 0
    for row in grid:
        total += row.count('X')
    
    return total




def loopcheck(grid, x, y, d):
    grid = copy.deepcopy(grid)
    
    dy, dx = movement[d]
    ny, nx = y+dy, x+dx
    
    height, width = len(grid), len(grid[0])
    if not(0 <= ny < height and 0 <= nx < width):
        return False
    if grid[ny][nx] != '.':
        return False
    grid[ny][nx] = '#'

    x, y, d = move(grid, x, y, d)

    while 0 <= y < height and 0 <= x < width:
        if d in grid[y][x]:
            return True
        if grid[y][x] == '.':
            grid[y][x] = d
        else:
            grid[y][x] += d
            
        dy, dx = movement[d]
        ny, nx = y+dy, x+dx
        if not (0 <= ny < height and 0 <= nx < width):
            blocked = False
        else:
            blocked = (grid[ny][nx] == '#')
        if blocked:
            d = rotations[(rotations.index(d) + 1)%4]
        else:
            y, x = ny, nx  
    else:
        return False

    
def p2(data):
    rows = data.split('\n')[:-1]
    grid = [list(row) for row in rows]

    x, y = 0, 0
    d = ''

    rotations = list('^>v<')
    movement = {'^':(-1, 0), '>':(0, 1), 'v':(1, 0), '<':(0, -1)}
    
    for i, row in enumerate(grid):
        for c in rotations:
            if c in row:
                d = c
                y = i
                x = row.index(c)

    height, width = len(grid), len(grid[0])

    grid[y][x] = '.'
    options = set()

    while 0 <= y < height and 0 <= x < width:
        if grid[y][x] == '.':
            grid[y][x] = d
        else:
            grid[y][x] += d
            
        dy, dx = movement[d]
        ny, nx = y+dy, x+dx
        if not (0 <= ny < height and 0 <= nx < width):
            blocked = False
        else:
            blocked = (grid[ny][nx] == '#')
        if blocked:
            d = rotations[(rotations.index(d) + 1)%4]
        else:
            if loopcheck(grid, x, y, d):
                options.add((ny, nx))
            y, x = ny, nx

    return len(options)

def main():
    f = open('input6.txt', 'r')
    data = f.read()
    print(p1(data))
    print(p2(data))


if __name__ == '__main__':
    main()
