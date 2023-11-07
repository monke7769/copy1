import sys
sys.stdin = open('gymnastics.in','r')
sys.stdout = open('gymnastics.out','w')

liste = [int(i) for i in input().split()]
K = liste[0] #K=3
N = liste[1] #N=4
biglist = []
for i in range(K):
    a = [int(j) for j in input().split()]
    biglist.append(a)
#print(biglist)

counter = 0
for i in range(1,N+1):
    for j in range(i,N+1):
        b = True
        k = 1
        if biglist[0].index(i) < biglist[0].index(j):
            c = 999
        else:
            c = -999
        while b == True and k < K:
            if biglist[k].index(i) < biglist[k].index(j):
                d = 999
            else:
                d = -999

            if c != d:
                b = False
            k += 1
        if b == True:
            counter += 1
            #print(i,j)
            
print(counter-N)
