import copy

memo = {}


numpad_dict = {'7':(0, 0), '8':(1, 0), '9': (2, 0),
               '4':(0, 1), '5':(1, 1), '6': (2, 1),
               '1':(0, 2), '2':(1, 2), '3': (2, 2),
               '0':(1, 3), 'A':(2, 3)}

keypad_dict = {            '^':(1, 0), 'A': (2, 0),
               '<':(0, 1), 'v':(1, 1), '>': (2, 1)}

def find_shortest(target, states, over_first, no_bots):
    if len(states) == 0:
        return 1, []
        for k in keypad_dict:
            if keypad_dict[k] == target:
                return k, []
    tx, ty = target
    cx, cy = states[0]
    new_target = ''
    while (cx, cy) != (tx, ty):
        dx, dy = tx-cx, ty-cy
        if ((len(states) == no_bots+1 and (cx, cy) == (0, 3)) or
            (len(states) < no_bots+1 and (cx, cy) == (0, 0))):
                return '', None
        if (over_first and cx != tx) or (not over_first and cy == ty):
            if dx < 0:
                new_target += '<'
            else:
                new_target += '>'
            dx = dx//abs(dx)
            cx += dx
        else:
            if dy < 0:
                new_target += '^'
            else:
                new_target += 'v'
            dy = dy//abs(dy)
            cy += dy
    new_target += 'A'
    steps, new_states = solve(new_target, states[1:], no_bots)
    
    states[0] = target
    for i, ns in enumerate(new_states):
        states[i+1] = ns
    return steps, states

def solve(target, states, no_bots):
    if (target, tuple(states), no_bots) in memo:
        return memo[(target, tuple(states), no_bots)]
    if target == '':
        return 0, states

    s1 = copy.deepcopy(states)
    s2 = copy.deepcopy(states)

    if len(s1) == no_bots+1:
        target_pos = numpad_dict[target[0]]
    else:
        target_pos = keypad_dict[target[0]]

    
    t1, s1 = find_shortest(target_pos, s1, True, no_bots)
    if s1 is not None:
        steps, s1 = solve(target[1:], s1, no_bots)
        t1 += steps

    t2, s2 = find_shortest(target_pos, s2, False, no_bots)
    if s2 is not None:
        steps, s2 = solve(target[1:], s2, no_bots)
        t2 += steps

    if s1 is None:
        rt, rs = t2, s2
    elif s2 is None:
        rt, rs = t1, s1

    elif t1 < t2:
        rt, rs = t1, s1
    else:
        rt, rs = t2, s2

    memo[(target, tuple(states), no_bots)] = rt, rs
    return rt, rs
    
def p1(data):
    targets = data.split('\n')[:-1]
    print(targets)

    total = 0
    for target in targets:
        steps, _ = solve(target, [(2, 3)]+[(2, 0) for _ in range(2)], 2)
        total += steps * int(target[:-1])
        
        #print(steps)

    
    return total

def p2(data):
    targets = data.split('\n')[:-1]
    print(targets)

    total = 0
    for target in targets:
        steps, _ = solve(target, [(2, 3)]+[(2, 0) for _ in range(25)], 25)
        total += steps * int(target[:-1])
        #print(steps, int(target[:-1]))
        #print(steps)

    
    return total

def main():
    f = open('input21.txt', 'r')
    data = f.read()
    print(p1(data))
    print(p2(data))

if __name__ == '__main__':
    main()
