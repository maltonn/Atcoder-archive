from typing import Deque


def main():
    import sys
    import numpy as np
    from collections import deque
    N=int(sys.stdin.readline())
    A=list(map(int,sys.stdin.readline().split()))
    B=list(map(int,sys.stdin.readline().split()))
    deq=Deque()
    res=0
    for i in range(N):
        if deq and deq[-1][1]*(A[i]-B[i])>0:
            idx,diff=deq.pop()
            res+=max(A[idx],B[idx])
            res+=max(A[i],B[i])
        else:
            deq.append((i,A[i]-B[i]))

    lst=list(deq)
    diff_lst=[diff for idx,diff in lst]
    sorted_arg=np.argsort(-np.abs(np.array(diff_lst))).tolist()
    #↑絶対値の大きい順

    lst2=[-1]*N
    for idx in sorted_arg[:len(sorted_arg)//2]:
        idx2=lst[idx][0]
        if A[idx2]>B[idx2]:
            res+=A[idx2]
            lst2[idx]=1
        else:
            res+=B[idx2]
            lst2[idx]=0
        
main()