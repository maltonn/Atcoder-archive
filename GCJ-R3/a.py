def solve():
    X,Y,M=input().split()
    X=int(X)
    Y=int(Y)
    dic={
        'S':(0,-1),
        'N':(0,1),
        'W':(-1,0),
        'E':(1,0),
    }
    L=[dic[x] for x in M]
    
    for i in range(len(M)):
        if L[i][0]:
            X+=L[i][0]
        else:
            Y+=L[i][1]
        d=abs(X)+abs(Y)-i-1
        print(X,Y,d)
        if d<=0:
            return i+1

    return 'IMPOSSIBLE'

def main():
    T=int(input())
    for case in range(1,T+1):
         print('Case #{}: {}'.format(case,solve()))

main()