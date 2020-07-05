def main():
    import sys
    import itertools
    import numpy as np
    H,W,K=list(map(int,sys.stdin.readline().split()))
    C=np.zeros((H,W))
    for i in range(H):
        C[i]=[1 if x=='#' else 0 for x in sys.stdin.readline().strip()]

    nums = [0,1]
    count=0
    for pat in itertools.product(nums, repeat=H+W):
        patH=list(i for i,x in enumerate(pat[:H]) if x==1)
        patW=list(i for i,x in enumerate(pat[H:]) if x==1)
        CH=C[patH]
        if CH.shape[0]:
            CHW=CH[:,patW]
            p=np.count_nonzero(CHW)
            if p==K:
                count+=1


    print(count)

    


main()