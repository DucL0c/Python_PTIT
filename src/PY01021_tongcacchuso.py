for _ in range(int(input())):
    s = input()
    l = []
    sum = 0
    for i in range(len(s)):
        if s[i].isdigit():
            sum += int(s[i])
        else:
            l.append(s[i])
    l.sort()
    for i in l:
        print(i,end="")
    print(sum)