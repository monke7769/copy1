N = int(input())
cows = [int(i) for i in input().split()]
cows.sort()
cows.reverse()
#print(cows)
e = 0
l = []
for i in range(N):
    if (i+1)*cows[i] >= e:
        e = (i+1)*cows[i]
        l.append(cows[i])
print(e,min(l))
