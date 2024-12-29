
def p1(data):
    rows = data.split('\n')[:-1]
    grid = [list(row) for row in rows]

    area, perimeter = {}, {}
    height, width = len(grid), len(grid[0])
    mapped = set()
    regions = {}
    
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if (j, i) in mapped:
                continue

            plantid = 0
            while c+str(plantid) in regions:
                plantid += 1

            plantid = c+str(plantid)
            regions[plantid] = set()
            
            horizon = [(j, i)]
                
            while len(horizon) > 0:
                x, y = horizon.pop()
                if (x, y) in mapped:
                    continue
                
                mapped.add((x, y))
                regions[plantid].add((x, y))
                
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < width and 0 <= ny < height:
                        if grid[ny][nx] == c:
                            horizon.append((nx, ny))

    area, perimeter = {}, {}

    for plantid in regions:
        area[plantid] = len(regions[plantid])
        for x, y in regions[plantid]:

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x+dx, y+dy
                if (nx, ny) not in regions[plantid]:
                    if plantid in perimeter:
                        perimeter[plantid] += 1
                    else:
                        perimeter[plantid] = 1

    total = 0
    for region in regions:
        total += area[region] * perimeter[region]

    return total

def p2(data):
    rows = data.split('\n')[:-1]
    grid = [list(row) for row in rows]

    area, perimeter = {}, {}
    height, width = len(grid), len(grid[0])
    mapped = set()
    regions = {}
    
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if (j, i) in mapped:
                continue

            plantid = 0
            while c+str(plantid) in regions:
                plantid += 1

            plantid = c+str(plantid)
            regions[plantid] = set()
            
            horizon = [(j, i)]
                
            while len(horizon) > 0:
                x, y = horizon.pop()
                if (x, y) in mapped:
                    continue
                
                mapped.add((x, y))
                regions[plantid].add((x, y))
                
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < width and 0 <= ny < height:
                        if grid[ny][nx] == c:
                            horizon.append((nx, ny))

    area, edges = {}, {}

    for plantid in regions:
        area[plantid] = len(regions[plantid])
        edges[plantid] = {}
        for x, y in regions[plantid]:

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x+dx, y+dy
                if (nx, ny) not in regions[plantid]:
                    if (dx, dy) not in edges[plantid]:
                        edges[plantid][(dx, dy)] = set()
                    edges[plantid][(dx, dy)].add((x,y))

    
    total = 0         
    for region in regions:
        edgecount = 0
        for edgedir in edges[region]:
            es = edges[region][edgedir]
            dx, dy = (1, 0) if edgedir[0] == 0 else (0, 1)
            while len(es) > 0:
                edgecount += 1
                x, y = es.pop()
                n = 1
                while (x+n*dx, y+n*dy) in es:
                    es.remove((x+n*dx, y+n*dy))
                    n+=1
                    
                n = 1
                while (x-n*dx, y-n*dy) in es:
                    es.remove((x-n*dx, y-n*dy))
                    n+=1
        total += area[region] * edgecount

                

    return total

def main():
    f = open('input12.txt', 'r')
    data = f.read()
    print(p1(data))
    print(p2(data))

if __name__ == '__main__':
    main()
