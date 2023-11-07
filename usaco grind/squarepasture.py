# guaranteed no overlaps!

import sys
sys.stdin = open('square.in','r')
sys.stdout = open('square.out','w')

p1 = [int(i) for i in input().split()]
p2 = [int(i) for i in input().split()]

ylist = [p1[1],p1[3],p2[1],p2[3]]
xlist = [p1[0],p1[2],p2[0],p2[2]]

s = max(max(ylist)-min(ylist),max(xlist)-min(xlist))

print(s**2)