def main():
    import sys
    import numpy as np
    H,W=list(map(int,sys.stdin.readline().split()))
    room=np.zeros((H,W))
    for i in range(H):
        for j,s in enumerate(sys.stdin.readline().strip()):
            if s=='.':
                room[i,j]=1
    
    count=0
    for h in range(H):
        for w in range(W-1):
            if np.sum(room[h,w:w+2])==2:
                count+=1
    for w in range(W):
        for h in range(H-1):
            if np.sum(room[h:h+2,w])==2:
                count+=1
    
    print(count)
        
main()