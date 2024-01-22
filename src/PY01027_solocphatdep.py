s = input()
d = 1
for i in range(len(s)):
    if s[i]=='6': continue
    elif s[i]=='8':
        if s[i-1] == '8':
            if s[i-2] != '6':
                d = 0
                break
        elif s[i-1] == '6': continue
        else:
            d = 0
            break
    else:
        d = 0
        break
if d == 1: print("YES")
else: print("NO")