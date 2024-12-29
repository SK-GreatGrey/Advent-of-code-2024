import itertools


def evaluate(target, parts, operators):
    total = parts[0]
    for p, o in zip(parts[1:], operators):
        if o == '*':
            total *= p
        elif o == '+':
            total += p
        elif o == '|':
            total = int(str(total) + str(p))
    return total == target

def p1(data):
    problems = data.split('\n')[:-1]

    total = 0
    for problem in problems:
        target, parts = problem.split(': ')
        target = int(target)
        parts = [int(part) for part in parts.split(' ')]

        for operators in itertools.product('*+', repeat=len(parts)-1):
            if evaluate(target, parts, operators):
                total += target
                #print(problem)
                break

    return total
              


def p2(data):
    problems = data.split('\n')[:-1]

    total = 0
    for problem in problems:
        target, parts = problem.split(': ')
        target = int(target)
        parts = [int(part) for part in parts.split(' ')]

        for operators in itertools.product('*+|', repeat=len(parts)-1):
            if evaluate(target, parts, operators):
                total += target
                #print(problem)
                break

    return total

def main():
    f = open('input7.txt', 'r')
    data = f.read()
    print(p1(data))
    print(p2(data))


if __name__ == '__main__':
    main()
