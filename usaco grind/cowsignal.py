import sys
sys.stdin = open('cowsignal.in','r')
sys.stdout = open('cowsignal.out','w')

M,N,K = map(int, input().split())
signal = [input() for w in range(M)]
for i in range(K*M):
    for j in range(N):
        print(signal[i//K][j]*K,end='')
    print()
    
