s = input()
a = []
for i in range(len(s)):
    a.append(s[i])
def Try(a):
    res = []
    backtrack(a, [], res)
    return res
 
def backtrack(a, path, res):
    if not a:
        ans = ""
        for i in path:
            ans += i
        res.append(ans)
    for i in range(len(a)):
        backtrack(a[:i] + a[i+1:], path + [a[i]], res)
        
l = Try(a)
for i in l:
    print(i)