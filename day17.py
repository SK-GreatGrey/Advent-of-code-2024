import copy

def operator(registers, opcode, operand):
    match operand:
        case 0|1|2|3:
            combo_operand = operand
        case 4:
            combo_operand = registers[0]
        case 5:
            combo_operand = registers[1]
        case 6:
            combo_operand = registers[2]
        case 7:
            combo_operand = -1
    match opcode:
        case 0: #adv
            registers[0] //= 2**combo_operand
        case 1: #bxl
            registers[1] ^= operand
        case 2: #bst
            registers[1] = combo_operand%8
        case 3: #jnz
            if registers[0] != 0:
                return (0, operand)
        case 4: #bxc
            registers[1] ^= registers[2]
        case 5: #out
            return (1, combo_operand%8)
        case 6: #bdv
            registers[1] = registers[0] // 2**combo_operand
        case 7:
            registers[2] = registers[0] // 2**combo_operand

def run(registers, program, target = None):
    outputs = []
    ip = 0
    registers = copy.copy(registers)
    while ip < len(program)-1:
        output = operator(registers, program[ip], program[ip+1])
        if output is None:
            ip += 2
        elif output[0] == 0:
            ip = output[1]
        else:
            ip += 2
            outputs.append(output[1])
            if target is not None:
                if outputs != target[:len(outputs)]:
                    break
            
    if target is not None:
        if outputs == target:
            return True
        else:
            return False
    if len(outputs) > 0:
        return outputs


def p1(data):
    registers, program = data.split('\n\n')
    registers = [int(reg.split(' ')[2]) for reg in registers.split('\n')]
    program = [int(x) for x in program.split(' ')[1].split(',')]

    return ','.join([str(s) for s in run(registers, program)])

def p2(data):
    registers, program = data.split('\n\n')
    registers = [int(reg.split(' ')[2]) for reg in registers.split('\n')]
    program = [int(x) for x in program.split(' ')[1].split(',')]

    #program = [0, 3, 5, 4, 3, 0]
    #registers = [2024, 0, 0]

    i = 1
    result = []
    while len(result) < len(program):
        i *= 2
        registers[0] = i
        result = run(registers, program)

    prev = result
    n = len(program)-1
    skip10 = True
    j = 0
    while n >= 0:
        if result[n:] == program[n:]:
            n -= 1
            j = 0
            continue
        i += 8**n
        j += 1
        registers[0] = i
        result = run(registers, program)
        prev = result
    return i
    

def main():
    f = open('input17.txt', 'r')
    data = f.read()
    print(p1(data))
    print(p2(data))

if __name__ == '__main__':
    main()
