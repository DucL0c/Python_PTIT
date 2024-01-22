def solve(s):
    sum = 0
    for i in s : sum += ord(i) - ord('0')
    return str(sum)
s = input()
dem = 0
while len(s)>1:
    s = solve(s)
    dem+=1
print(dem)