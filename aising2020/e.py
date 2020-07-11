import sys #WA
def sub():
    N=int(sys.stdin.readline())
    lst=[(0,0,0)]*N
    for i in range(N):
        K,L,R=list(map(int,sys.stdin.readline().split()))
        lst[i]=(K,L,R)
    
    lst.sort(key=lambda x:-(x[1]-x[2]))#幸福度の大きい順

    memo=[0]*N
    score=0
    for k,l,r in lst:
        tmp=k-1
        flag=False
        while tmp+1:
            if memo[tmp]==0:
                memo[tmp]=1
                flag=True
                score+=l
                break
            tmp-=1

        if not flag:
            score+=r

    print(score)

def main():
    T=int(sys.stdin.readline())
    for _ in range(T):
        sub()

main()