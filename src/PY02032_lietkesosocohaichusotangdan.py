import re
r = '\d\d'
s = input()
print(" ".join(sorted(set(re.findall(r, s)))))