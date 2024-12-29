height, width = 103, 101

class Bot:
    def __init__(self, px, py, vx, vy):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy

    def move(self):
        self.px = (self.px + self.vx)%width
        self.py = (self.py + self.vy)%height

    def quad(self):
        if self.px == width//2 or self.py == height//2:
            return -1
        return 2*(self.px < width//2) + (self.py < (height//2))

    def __str__(self):
        return f'p={self.px},{self.py} v={self.vx},{self.vy}'


def printbots(coords):
    for i in range(height):
        s = ''
        for j in range(width):
            s += '*' if (j, i) in coords else ' '
        print(s)

def p1(data):
    bots = data.split('\n')[:-1]

    botlist = []
    for bot in bots:
        p, v = bot.split(' ')
        
        p = p.split(',')        
        px = int(p[0][2:])
        py = int(p[1])

        v = v.split(',')
        vx = int(v[0][2:])
        vy = int(v[1])
        
        botlist.append(Bot(px, py, vx, vy))

    for _ in range(100):
        for bot in botlist:
            bot.move()
    
    
    
    quadlist = [0]*4
    for bot in botlist:
        quad = bot.quad()
        if quad != -1:
            quadlist[quad] += 1

    result = 1
    for quad in quadlist:
        result *= quad

    return result
        
def p2(data):
    bots = data.split('\n')[:-1]

    botlist = []
    for bot in bots:
        p, v = bot.split(' ')
        
        p = p.split(',')        
        px = int(p[0][2:])
        py = int(p[1])

        v = v.split(',')
        vx = int(v[0][2:])
        vy = int(v[1])
        
        botlist.append(Bot(px, py, vx, vy))


    for i in range(11000):
        for bot in botlist:
            bot.move()

        rows = []
        no_rows = 5
        for _ in range(no_rows):
            rows.append(None)
        coords = set([(b.px, b.py) for b in botlist])
        count = 0
        
        for y in range(height):
            t = 0
            for x in range(width):
                if (x, y) in coords:
                    t += 1
            if t > 30:
                count += 1
        if count == 2:
            return i+1

def main():
    f = open('input14.txt', 'r')
    data = f.read()
    print(p1(data))
    print(p2(data))

if __name__ == '__main__':
    main()
