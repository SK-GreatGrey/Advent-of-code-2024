import queue

def find_path(grid, start, end):
    sx, sy = start
    ex, ey = end

    height, width = len(grid), len(grid[0])
    
    horizon = queue.PriorityQueue()
    horizon.put((0, 0, sx, sy, []))
    visited = set()

    while not horizon.empty():
        f, g, x, y, path = horizon.get()
        if (x, y) in visited:
            continue
        else:
            visited.add((x, y))

        if (x, y) == (ex, ey):
            return f

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < width and 0 <= ny < height:
                if grid[ny][nx] != '#':
                    h = abs(ex-nx)+abs(ey-ny)
                    horizon.put((g+h+1, g+1, nx, ny, path+[(x, y)]))

    return -1

def p1(data):
    byte_list = data.split('\n')[:-1]
    byte_list = [tuple(int(x) for x in byte.split(',')) for byte in byte_list]

    height, width = 71, 71

    grid = [['.' for _ in range(width)] for _ in range(height)]
    
    for x, y in byte_list[:1024]:
        grid[y][x] = '#'

    start = (0, 0)
    end = (width-1, height-1)

    return find_path(grid, start, end)

    
        
    print(shortest)

def p2(data):
    byte_list = data.split('\n')[:-1]
    byte_list = [tuple(int(x) for x in byte.split(',')) for byte in byte_list]

    height, width = 71, 71

        
    start = (0, 0)
    end = (width-1, height-1)
    i = 1024
    j = len(byte_list)
    while j-i > 1:
        k = (j+i)//2
        grid = [['.' for _ in range(width)] for _ in range(height)]
    
        for x, y in byte_list[:k]:
            grid[y][x] = '#'
        if find_path(grid, start, end) == -1:
            j = k
        else:
            i = k

    x, y = byte_list[j-1]
    return f'{x},{y}'

def main():
    f = open('input18.txt', 'r')
    data = f.read()
    print(p1(data))
    print(p2(data))

if __name__ == '__main__':
    main()
