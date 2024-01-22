def solve(s):
    s = s.lower()
    l = len(s)
    if len(s)<3: return False
    if s[len(s) - 3:] != '.py':
        return False
    for i in s:
        if ord(i)<97 and ord(i)>122 and i!='.' and i!='_':
            return False
    return True


s = input()
if solve(s): print("yes")
else: print("no")