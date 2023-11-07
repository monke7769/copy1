import sys
sys.stdin = open('cowtip.in','r')
sys.stdout = open('cowtip.out','w')

N = int(input())
grid = []
for i in range(N):
    line = []
    for j in input():
        line.append(int(j))
    grid.append(line)
#grid = [[0,0,1],[1,1,1],[1,1,1]]
counter = 0
def allZeros():
    e = True
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                pass
            elif grid[i][j] == 1:
                e = False
                return e
    return e

while not allZeros():
    for i in range(N-1,-1,-1):
        for j in range(N-1,-1,-1):
            if grid[i][j] == 1:
                a = i
                b = j
                #print(a,b)
                break
        if grid[i][j] == 1:
            break
    for i in range(0,a+1):
        for j in range(0,b+1):
            if grid[i][j] == 1:
                grid[i][j] = 0
            elif grid[i][j] == 0:
                grid[i][j] = 1
    #print(grid)
    counter += 1
print(counter)
