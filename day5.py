
def p1(data):
    rules, updates = data.split('\n\n')


    rules_dict = {}
    for line in rules.split('\n'):
        a, b = line.split('|')
        if a in rules_dict:
            rules_dict[a].append(b)
        else:
            rules_dict[a] = [b]
        
    total = 0

    for update in updates.split('\n')[:-1]:
        numbers = update.split(',')
        #print(numbers)
        for i, n in enumerate(numbers):
            inorder = True
            if n in rules_dict:
                for num in rules_dict[n]:
                    if num in numbers[:i]:
                        inorder = False
                        break
                if not inorder:
                    break
                
        else:
            total += int(numbers[len(numbers)//2])
            
    return total

def test(rules, update):
    numbers = update.split(',')
    for i, n in enumerate(numbers):
        if n in rules:
            for num in rules[n]:
                if num in numbers[:i]:
                    return False
    return True

def p2(data):
    rules, updates = data.split('\n\n')


    rules_dict = {}
    for line in rules.split('\n'):
        a, b = line.split('|')
        if a in rules_dict:
            rules_dict[a].append(b)
        else:
            rules_dict[a] = [b]

    total = 0
    for update in updates.split('\n')[:-1]:
        if test(rules_dict, update):
            continue
        update = update.split(',')
        result = []
        while len(result) < len(update):
            
            inorder = True
            num = update.pop(0)
            for n in update:
                if n in rules_dict:
                    for rule in rules_dict[n]:
                        if rule == num:
                            inorder = False
                            break
                    if inorder == False:
                        break
            if inorder:
                result.append(num)
            else:
                update.append(num)
        total += int(result[-1])
                    
    return total

def main():
    f = open('input5.txt', 'r')
    data = f.read()
    print(p1(data))
    print(p2(data))


if __name__ == '__main__':
    main()
