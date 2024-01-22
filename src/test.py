import re

lines = []
while True:
    try:
        lines.append(input())
    except:
        break

for line in lines:
    s = re.split(r'[.!?]', line)
    for i in s:
        tmp = i.strip().lower().split()
        res = ' '.join(tmp).capitalize()
        if res[-1] not in '!.?':
            res += '.'
        if res[-2] == ' ':
            res = res[:-2] + res[-1]

        print(res, end = ' ')