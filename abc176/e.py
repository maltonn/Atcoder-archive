def argmaxs(lst):
    mx=max(lst)
    output=[]
    for i,a in enumerate(lst):
        if a==mx:
            output.append(i)
    
    return output
    
def main():
    import sys
    H,W,M=list(map(int,sys.stdin.readline().split()))
    y_lst=[0]*H
    x_lst=[0]*W
    bumbs=[set() for _ in range(H)]

    for i in range(M):
        h,w=list(map(int,sys.stdin.readline().split()))
        y_lst[h-1]+=1
        x_lst[w-1]+=1
        bumbs[h-1].add(w-1)

    output=max(x_lst)+max(y_lst)
    
    
    argys=argmaxs(y_lst)
    argxs=argmaxs(x_lst)
    argx_set=set(argxs)

    k=1
    for y in argys:
        if not(argx_set <= bumbs[y]):
            k=0
            break

    
    print(output-k)
main()