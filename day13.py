import math

'''
start_x + n * step_x = start_y + n * step_y
'''

def solvemachine(a, b, prize, offset = 0):
    ax, ay = a
    bx, by = b
    px, py = prize
    px += offset
    py += offset

    mxa = math.ceil(px/ax)

    best = 0
    for na in range(mxa):
        x = na * ax
        if (px - x)%bx != 0:
            continue
        nb = (px - x)//bx
        if na*ay + nb*by == py:
            cost = na*3+nb
            if best == 0 or cost < best:
                best = cost

        
    return best

def solvemachine2(a, b, prize, offset = 0):
    ax, ay = a
    bx, by = b
    px, py = prize
    px += offset
    py += offset

    gcd_x, gcd_y = math.gcd(ax, bx), math.gcd(ay, by)
    if px%gcd_x != 0 or py%gcd_y != 0:
        return 0

    start_ax, start_ay = 0, 0
    step_ax, step_ay = 0, 0

    while (px - start_ax * ax)%bx != 0:
        start_ax += 1
        
    while (py - start_ay * ay)%by != 0:
        start_ay += 1
        
    
    step_ax = math.lcm(ax, bx)//ax
    step_ay = math.lcm(ay, by)//ay

    start_a = start_ax
    if ((start_ay-start_a)%math.gcd(step_ax, step_ay) != 0):
        return 0
    while start_a % step_ay != start_ay:
        start_a += step_ax

    step_a = math.lcm(step_ax, step_ay)

    px1 = px-start_a*ax
    py1 = py-start_a*ay
    px2 = px1-step_a*ax
    py2 = py1-step_a*ay

    mx1 = px1//bx
    mx2 = px2//bx
    my1 = py1//by
    my2 = py2//by

    e0 = my1-mx1
    de =(my1-mx1)-(my2-mx2)

    if e0%de != 0:
        return 0
    
    no_step_a = e0//de
    n=no_step_a*step_a+start_a
    m=(px-n*ax)//bx
    
    return 3*n+m

def p1(data):
    machines = data[:-1].split('\n\n')

    cost = 0
    for machine in machines:
        a, b, prize = machine.split('\n')
        
        a = a.split(' ')
        ax, ay = int(a[2][1:-1]), int(a[3][1:])
        
        b = b.split(' ')
        bx, by = int(b[2][1:-1]), int(b[3][1:])

        prize = prize.split(' ')
        px, py = int(prize[1][2:-1]), int(prize[2][2:])

        cost += solvemachine2((ax, ay), (bx, by), (px, py))
        
    return cost

def p2(data):
    machines = data[:-1].split('\n\n')

    cost = 0
    for machine in machines:
        a, b, prize = machine.split('\n')
        
        a = a.split(' ')
        ax, ay = int(a[2][1:-1]), int(a[3][1:])
        
        b = b.split(' ')
        bx, by = int(b[2][1:-1]), int(b[3][1:])

        prize = prize.split(' ')
        px, py = int(prize[1][2:-1]), int(prize[2][2:])

        cost += solvemachine2((ax, ay), (bx, by), (px, py), 10000000000000)
        
    return cost

def main():
    f = open('input13.txt', 'r')
    data = f.read()
    print(p1(data))
    print(p2(data))

if __name__ == '__main__':
    main()
