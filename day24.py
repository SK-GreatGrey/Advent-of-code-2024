import copy
def operation(a, op, b):
    match op:
        case 'AND':
            return a & b
        case 'OR':
            return a | b
        case 'XOR':
            return a ^ b
    return 0

def p1(data):
    wires, gates = data.split('\n\n')
    wires = wires.split('\n')
    wires = {wire.split(': ')[0]: int(wire.split(': ')[1]) for wire in wires}
    gates = gates.split('\n')[:-1]
    gates = [gate.split(' ') for gate in gates]

    while len(gates) > 0:
        gate = gates.pop(0)
        w1, op, w2, _, w3 = gate
        if w1 not in wires or w2 not in wires:
            gates.append(gate)
            continue

        wires[w3] = operation(wires[w1], op, wires[w2])

    s = ''
    for wire in sorted(wires.keys()):
        if wire[0] == 'z':
            s += str(wires[wire])

    s = s[::-1]
    return int(s, 2)
        

def compute(wires, gates):
    wires = copy.deepcopy(wires)
    while True:
        new_gates = []
        for gate in gates:
            w1, op, w2, _, w3 = gate
            if w1 not in wires or w2 not in wires:
                new_gates.append(gate)
            else:
                wires[w3] = operation(wires[w1], op, wires[w2])
        if len(new_gates) == len(gates):
            break
        gates = new_gates
    s = ''
    for wire in sorted(wires.keys()):
        if wire[0] == 'z':
            s += str(wires[wire])

    s = s[::-1]
    return int(s, 2)


def p2(data):
    wires, gates = data.split('\n\n')
    wires = wires.split('\n')
    wires = {wire.split(': ')[0]: int(wire.split(': ')[1]) for wire in wires}
    gates = gates.split('\n')[:-1]
    gates = [gate.split(' ') for gate in gates]
    for g in gates:
        break
        if g[4] == 'gbf':
            g[4] = 'z09'
        elif g[4] == 'z09':
            g[4] = 'gbf'

        if g[4] == 'hdt':
            g[4] = 'z05'
        elif g[4] == 'z05':
            g[4] = 'hdt'

        if g[4] == 'nbf':
            g[4] = 'z30'
        elif g[4] == 'z30':
            g[4] = 'nbf'
    gate_dict = {g[4]: (g[0], g[2]) for g in gates}

    xor1 = {}
    xor2 = {}
    and1 = {}
    and2 = {}
    or1 = {}
    cout = {}
    for i in range(45):
        x = f'x{i:0>2}'
        y = f'y{i:0>2}'
        z = f'z{i:0>2}'
        xor1[i] = None
        xor2[i] = None
        and1[i] = None
        and2[i] = None
        or1[i] = None
        cin = cout[i-1] if i > 0 else None
        for g in gates:
            if x in g[0]+g[2] and y in g[0]+g[2]:
                if g[1] == 'XOR':
                    xor1[i] = g
                elif g[1] == 'AND':
                    and1[i] = g
                    
        if i == 0:
            cout[i] = and1[i][4] if and1[i] is not None else None
        if i > 0:
            x1o = xor1[i][4] if xor1[i] is not None else None
            a1o = and1[i][4] if and1[i] is not None else None
            for g in gates:
                if x1o in g[:4] or cin in g[:4]:
                    if g[1] == 'AND':
                        and2[i] = g
                    elif g[1] == 'XOR':
                        xor2[i] = g
            a2o = and2[i][4] if and2[i] is not None else None
            for g in gates:
                if a1o in g[:4] or a2o in g[:4]:
                    if g[1] == 'OR':
                        or1[i] = g
            if or1[i] is not None:
                cout[i] = or1[i][4]

    errors = []
    e = False
    while True:
        e1, e2 = None, None
        for i in range(1, 45):
            x = f'x{i:0>2}'
            y = f'y{i:0>2}'
            z = f'z{i:0>2}'

            
            if xor1[i][4] not in xor2[i][:4]:
                pass
                '''
                print('xor1 -> xor2')
                print(i, xor1[i])
                print(i, xor2[i])
                print()
                '''
            
            if i > 1 and or1[i-1][4] not in xor2[i][:4]:
                pass
                '''
                print('or1 -> xor2')
                print(i-1, or1[i-1])
                print(i, xor2[i])
                print(i, xor1[i])
                print()
                '''

            if xor1[i][4] not in and2[i][:4]:
                pass
                '''
                print('xor1 -> and2')
                print(i, xor1[i])
                print(i, and2[i])
                '''
                if e2 is None:
                    e2 = e1
                e1 = xor1[i][4]
                
            if i > 1 and or1[i-1][4] not in and2[i][:4]:
                pass
                '''
                print('or1 -> and2')
                print(i-1, or1[i-1])
                print(i, and2[i])
                '''

            if and1[i][4] not in or1[i][:4]:
                pass
                '''
                print('and1 -> or1')
                print(i, and1[i])
                print(i, or1[i])
                '''
                if e2 is None:
                    e2 = e1
                e1 = and1[i][4]
                    
                
            if and2[i][4] not in or1[i][:4]:
                pass
                '''
                print('and2 -> or1')
                print(i, and2[i])
                print(i, or1[i])
                '''

            if xor2[i][4] != z:                
                e1, e2 = xor2[i][4], z
                
            if e2 is not None:
                e = True
                break

        if e == False:
            break
        else:
            e = False
            errors += [e1, e2]
            for g in gates:
                if g[4] == e1:
                    g[4] = e2
                elif g[4] == e2:
                    g[4] = e1
                
        
        
    return ','.join(sorted(errors))

def main():
    f = open('input24.txt', 'r')
    data = f.read()
    print(p1(data))
    print(p2(data))

if __name__ == '__main__':
    main()
