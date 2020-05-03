import sys
import numpy as np
def solve():
    R,S=list(map(int,sys.stdin.readline().split()))
    deck=np.tile(np.arange(1,R+1),(S))

    mx=R
    output=[]
    while True:
        poses=np.where(deck==mx)[0]
        if poses[0]==R*S-(R-mx+1)*S:
            mx-=1
            if mx==1:
                break
        else:
            current=R*S-(R-mx)*S
            for i in range(len(poses)):
                if poses[-i-1]==current-1:
                    current-=1
                    continue
                else:
                    goto=current-1
                    break

            a=deck[:poses[0]+1]
            b=deck[poses[0]+1:goto+1]
            c=deck[goto+1:]
            deck=np.hstack((b,a,c))
            output.append((poses[0]+1,goto-poses[0]))
    return len(output),output

def main():
    T=int(input())
    for case in range(1,T+1):
        num,path=solve()
        print('Case #{}: {}'.format(case,num))
        for p in path:
            print(' '.join(map(str,p)))
    
main()