def main():
    import sys
    import numpy as np
    import itertools
    N,M,X=list(map(int,sys.stdin.readline().split()))
    C=[]
    for i in range(N):
        C.append(list(map(int,sys.stdin.readline().split())))

    C=np.array(C)
    costs=C[:,0]
    C=C[:,1:]
    cost=10**12
    for a in list(itertools.product([0,1], repeat=N)):
        if all((np.sum(C.T*np.array(a),axis=1)>=X).tolist()):
            cost=min(cost,np.sum(costs*np.array(a)))
    if cost==10**12:
        print(-1)
    else:
        print(cost)
        


main()