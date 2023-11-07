import math
N = int(input())
preferred = input().split()
for i in range(len(preferred)):
    preferred[i] = int(preferred[i])
current = input().split()
for j in range(len(current)):
    current[j] = int(current[j])
diff = [preferred[i]-current[i] for i in range(N)]
l = [0]*N
switch = 0
subset = []
for i in diff:
    if i == 0:
        diff.remove(i)
switch = max(diff)+max(diff)-min(diff)
print(switch)
