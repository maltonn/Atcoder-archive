def main():
    import sys
    from bisect import bisect_left,bisect_right
    N,D,K=list(map(int,sys.stdin.readline().split()))
    if K!=0:
        pass
        
    lst1=[]
    lst2=[]
    lst_all=[]
    for i in range(N):
        P,S=list(map(int,sys.stdin.readline().split()))
        lst_all.append((P,S))
        if P==1:
            lst1.append(S)
        else:
            lst2.append(S)

    lst1.sort()
    lst2.sort()
    lst_all.sort(key=lambda x:x[1])

    c1=0
    c2=0
    for i in range(len(lst_all)):
        lst_all[i]=lst_all[i]+(c1 if lst_all[i][0]==1 else c2,)
        
        if lst_all[i][0]==1:
            c1+=1
        else:
            c2+=1

    # print(lst_all)

    if not lst1 or not lst2:
        print(max(len(lst1),len(lst2)))
        return
    
    dp1=[0]*len(lst1)
    dp2=[0]*len(lst2)

    for i,(p,t,c) in enumerate(lst_all):
        if p==1:
            if t-D>0:
                idx=bisect_right(lst2,t-D-1)
                dp1[c]=max(dp1[c-1] if c else 0,dp2[-1] if idx==len(dp2) else 0 if idx==0 else dp2[idx-1])+1
            else:
                dp1[c]=(dp1[c-1] if c else 0)+1
        else:
            if t-D>0:
                idx=bisect_right(lst1,t-D-1)
                dp2[c]=max(dp2[c-1] if c else 0,dp1[-1] if idx==len(dp1) else 0 if idx==0 else dp1[idx-1])+1
            else:
                dp2[c]=(dp2[c-1] if c else 0)+1
        # print(dp1)
        # print(dp2)
        # print('----')
    
    print(max(dp1[-1],dp2[-1]))

if __name__=='__main__':
    main()