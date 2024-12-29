def mix(a, b):
    return a ^ b

def prune(a):
    return a % 16777216

def p1(data):
    secrets = data.split('\n')[:-1]
    secrets = [int(s) for s in secrets]



    for i, s in enumerate(secrets):
        for _ in range(2000):
            t = s * 64
            s = mix(s, t)
            s = prune(s)
            
            t = s // 32
            s = mix(s, t)
            s = prune(s)
            
            t = s * 2048
            s = mix(s, t)
            s = prune(s)

            secrets[i] = s
    return sum(secrets)

def p2(data):
    secrets = data.split('\n')[:-1]
    secrets = [int(s) for s in secrets]


    #secrets = [1,2,3,2024]
    scores = {}
    sequences =set()
    for i, s in enumerate(secrets):
        seq = []
        prev = s%10
        scores[i] = {}
        for j in range(2000):
            t = s * 64
            s = mix(s, t)
            s = prune(s)
            
            t = s // 32
            s = mix(s, t)
            s = prune(s)
            
            t = s * 2048
            s = mix(s, t)
            s = prune(s)

            secrets[i] = s
            seq.append(s%10-prev)
            seq = seq[-4:]
            
            prev = s%10

            if len(seq) == 4 and tuple(seq) not in scores[i]:
                scores[i][tuple(seq)] = prev
                sequences.add(tuple(seq))

    best = 0
    for seq in sequences:
        score = sum([scores[i][seq] for i in scores.keys() if seq in scores[i]])
        if score > best:
            best = score

    return best

def main():
    f = open('input22.txt', 'r')
    data = f.read()
    print(p1(data))
    print(p2(data))

if __name__ == '__main__':
    main()
