def draw_grid(grid):
    for line in [''.join(row) for row in grid]:
        print(line)

def p1(data):
    rows, moves = data.split('\n\n')
    grid = [list(row) for row in rows.split('\n')]
    moves = moves.replace('\n', '')

    height, width = len(grid), len(grid[0])
    x, y = 0, 0
    for i, row in enumerate(grid):
        if '@' in row:
            x, y = row.index('@'), i

    directions = {'^':(0, -1), 'v':(0, 1),'>':(1, 0),'<':(-1, 0)}
    for move in moves:
        dx, dy = directions[move]
        nx, ny = x+dx, y+dy
        
        push = False
        while grid[ny][nx] == 'O':
            push = True
            nx, ny = nx+dx, ny+dy

        if grid[ny][nx] == '#':
            continue
        else:
            if push:
                grid[ny][nx] = 'O'
                nx, ny = x+dx, y+dy
            grid[ny][nx] = '@'
            grid[y][x] = '.'
            y, x, = ny, nx

    total = 0
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == 'O':
                total += 100 * i + j
    return total
    
def checksum(grid):
    total = 0
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == '[':
                total += 100 * i + j
    return total
def p2(data):
    rows, moves = data.split('\n\n')
    rows = rows.replace('#', '##')
    rows = rows.replace('O', '[]')
    rows = rows.replace('.', '..')
    rows = rows.replace('@', '@.')
    grid = [list(row) for row in rows.split('\n')]
    moves = moves.replace('\n', '')

    height, width = len(grid), len(grid[0])
    x, y = 0, 0
    for i, row in enumerate(grid):
        if '@' in row:
            x, y = row.index('@'), i


    directions = {'^':(0, -1), 'v':(0, 1),'>':(1, 0),'<':(-1, 0)}
    j = 0
    for move in moves:
        if j%100 == 0:
            print(j//100, checksum(grid))
        j += 1
        dx, dy = directions[move]
        nx, ny = x+dx, y+dy
        if grid[ny][nx] == '.':
            grid[ny][nx] = '@'
            grid[y][x] = '.'
            y, x = ny, nx
            continue
        
        push = True
        ahead = [(nx, ny)]
        push_list = []
        while push:
            new_ahead = []
            for (ax, ay) in ahead:
                c = grid[ay][ax]
                if c == '#':
                    push = False
                    break
                elif c in '[]':
                    if not (ax, ay) in push_list:
                        push_list.append((ax, ay))
                    if move in '^v':
                        new_ahead.append((ax, ay+dy))
                        if c == '[':
                            new_ahead.append((ax+1, ay+dy))
                            if not (ax+1, ay) in push_list:
                                push_list.append((ax+1, ay))
                        else:
                            new_ahead.append((ax-1, ay+dy))
                            if not (ax-1, ay) in push_list:
                                push_list.append((ax-1, ay))
                    else:
                        new_ahead.append((ax+dx, ay))
            if len(new_ahead) == 0:
                break
            ahead = new_ahead
        if push:
            for tx, ty in push_list[::-1]:
                grid[ty+dy][tx+dx] = grid[ty][tx]
                grid[ty][tx] = '.'
            grid[ny][nx] = '@'
            grid[y][x] = '.'
            x, y = nx, ny


    return 0#checksum(grid)

def main():
    f = open('uppgift 15.txt', 'r')
    data = f.read()
    print(p1(data))
    print(p2(data))

if __name__ == '__main__':
    main()
