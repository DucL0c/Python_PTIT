with open('VANBAN.in','r') as file:
    lines = file.readlines()
    myMap = {}
    Max = 0
    for line in lines:
        a = line.strip().split()
        for i in a:
            if i==i[::-1]:
                if len(i)>Max:
                    Max = len(i)
                if i not in myMap:
                    myMap[i] = 1
                else:
                    myMap[i] += 1
    for i,j in myMap.items():
        if len(i)==Max:
            print(f"{i} {j}")