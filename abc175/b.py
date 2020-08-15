def main():
    import sys
    N=int(sys.stdin.readline())
    L=list(map(int,sys.stdin.readline().split()))
    count=0
    for i in L:
        for j in L:
            if i==j:
                continue
            for k in L:
                if i==k or j==k:
                    continue
                
                lst=sorted([i,j,k])
                if lst[2]<lst[1]+lst[0]:
                    count+=1
  
    print(count//6)
main()