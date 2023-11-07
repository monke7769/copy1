import sys
sys.stdin = open('evolution.in','r')
sys.stdout = open('evolution.out','w')

cows = []
traits = []
n = int(input())
for i in range(n):
    cLine = input().split(' ')
    k = int(cLine[0])
    cows.append(cLine[1:].copy()) # use .copy() when putting list into another list
    for j in range(k):
        if cLine[j+1] not in traits:
            traits.append(cLine[j+1])
#print(traits)

# use two pointers now
isProper = True
for i in range(len(traits)):
    for j in range(i+1,len(traits)):
        a = traits[i]
        b = traits[j]
        aNotB = False
        bNotA = False
        aAndB = False
        for cow in cows:
            if a in cow and b in cow:
                aAndB = True
            if a in cow and not b in cow:
                aNotB = True
            if b in cow and not a in cow:
                bNotA = True
        if aNotB and bNotA and aAndB:
            isProper = False
if isProper:
    print('yes')
else:
    print('no')
