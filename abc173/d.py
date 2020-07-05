def main():
    import sys
    N=int(sys.stdin.readline())
    A=list(map(int,sys.stdin.readline().split()))
    if N==2:
        print(A[0])
        return

    
    A.sort(reverse=True)
    score=A[0]
    count=1
    
    
    for a in A[1:]:
        score+=a
        count+=1
        if count==N-1:
            break

        score+=a
        count+=1
        if count==N-1:
            break
    
    print(score)

main()