
def find(grid, y, x, height, width):
    total = 0
    if grid[y][x] != 'X':
        return 0
    
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dy == 0 and dx == 0:
                continue
            
            ty, tx = y, x
            for c in ['M', 'A', 'S']:
                ty += dy
                tx += dx
                if not 0 <= ty < height:
                    break
                if not 0 <= tx < width:
                    break

                if grid[ty][tx] != c:
                    break
            else:
                total += 1
                
    return total

def p1(data):
    rows = data.split('\n')[:-1]
    grid = [list(row) for row in rows]

    height = len(grid)
    width = len(grid[0])
    total = 0
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 'X':
                total += find(grid, row, col, height, width)

    return total

def find2(grid, y, x):
    if grid[y][x] != 'A':
        return 0
    
    c1 = grid[y-1][x-1] + grid[y+1][x+1]
    c2 = grid[y-1][x+1] + grid[y+1][x-1]
    c1 = ''.join(sorted(list(c1)))
    c2 = ''.join(sorted(list(c2)))
    if c1 == 'MS' and c2 == 'MS':
        return 1
    else:
        return 0

def p2(data):
    rows = data.split('\n')[:-1]
    grid = [list(row) for row in rows]

    height = len(grid)
    width = len(grid[0])
    total = 0
    for row in range(1, height-1):
        for col in range(1, width-1):
            if grid[row][col] == 'A':
                total += find2(grid, row, col)

    return total


def main():
    f = open('input4.txt', 'r')
    data = f.read()
    print(p1(data))
    print(p2(data))

if __name__ == '__main__':
    main()
