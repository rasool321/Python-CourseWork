l = list(map(int,input().split()))
for i in l:
    if i == 0:
        l.remove(i)

print(l)
print(len(l))
