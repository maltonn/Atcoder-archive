#RE
from collections import deque
from typing import Deque


def main():
    import sys
    from collections import deque
    N=int(sys.stdin.readline())
    in_lst=[0]*(2*N)
    out_lst=[0]*(2*N)
    
    dic={}
    for i in range(N):
        A,B=list(map(int,sys.stdin.readline().split()))
        dic[i+1]=(A-1,B-1,B-A-1)
        if A!=-1 and B!=-1 and B<=A:
            print('No')
            return
        if A!=-1:
            in_lst[A-1]=i+1
        if B!=-1:
            out_lst[B-1]=i+1

    st=set()
    for i in range(2*N):
        p=in_lst[i]
        if p:
            tmp=dic[p]
            if tmp[0]!=-2 and tmp[1]!=-2:
                st.add(p)
        
        p=out_lst[i]
        if p:
            tmp=dic[p]
            if tmp[0]!=-2 and tmp[1]!=-2:
                st.remove(p)
        if len(st)>=2:
            for j,p in enumerate(tuple(st)):
                k=-1
                if j==0:
                    k=dic[p][2]
                elif k!=dic[p][2]:
                    print('No')
                    return
                    
    deq=deque()
    idx=-1
    while True:
        idx+=1
        if idx==2*N:
            print('Yes')
            return

        if in_lst[idx]==0 and out_lst[idx]==0:
            for p in range(1,N+1):
                if dic[p][0]!=-2 and dic[p][1]!=-2:
                    continue
                if dic[p][0]==-2 and idx<dic[p][1]:
                    deq.appendleft((in_lst.copy(),out_lst.copy(),1,idx,p))
                if dic[p][1]==-2 and dic[p][1]<idx:
                    deq.appendleft((in_lst.copy(),out_lst.copy(),2,idx,p))
            break

    while deq:
        in_lst,out_lst,io,idx,p=deq.popleft()
        a,b,c=dic[p]
        
        if io==1:
            dic[p]=(idx,b,b-idx-1)
            in_lst[idx]=p
        elif io==2:
            dic[p]=(a,idx,idx-a-1)
            out_lst[idx]=p

        st=set()
        for i in range(2*N):
            p=in_lst[i]
            if p:
                tmp=dic[p]
                if tmp[0]!=-2 and tmp[1]!=-2:
                    st.add(p)
            
            p=out_lst[i]
            if p:
                tmp=dic[p]
                if tmp[0]!=-2 and tmp[1]!=-2:
                    st.remove(p)
            if len(st)>=2:
                flag=False
                for j,p in enumerate(tuple(st)):
                    k=-1
                    if j==0:
                        k=dic[p][2]
                    elif k!=dic[p][2]:
                        flag=True
                        break
                if flag:
                    break
        else:
            while True:
                idx+=1
                if idx==2*N:
                    print('Yes')
                    return

                if in_lst[idx]==0 and out_lst[idx]==0:
                    for p in range(1,N+1):
                        if dic[p][0]!=-2 and dic[p][1]!=-2:
                            continue
                        if dic[p][0]==-2 and idx<dic[p][1]:
                            deq.appendleft((in_lst.copy(),out_lst.copy(),1,idx,p))
                        if dic[p][1]==-2 and dic[p][1]<idx:
                            deq.appendleft((in_lst.copy(),out_lst.copy(),2,idx,p))
                    break


    print('No')

main()