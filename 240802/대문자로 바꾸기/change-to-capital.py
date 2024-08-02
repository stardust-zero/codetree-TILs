l = []
for i in range(5):
    l.append(list(input().split()))
for i in l:
    for j in i:
        print(j.upper(), end=' ')
    print()