def main():
    DEBUG=True

    import sys
    if DEBUG:
        f=open('in1.txt')
        id,N,K=list(map(int,f.readline().split()))
    else:
        id,N,K=list(map(int,sys.stdin.readline().split()))
    
    root_A=[[] for _ in range(N)]

    for i in range(N):
        if DEBUG:
            root_A[i]=list(map(int,list(f.readline().strip())))
        else:
            root_A[i]=list(map(int,list(sys.stdin.readline().strip())))
    min_loss=10001
    final_output=[]
    for n in range(2,K+1):
        A=root_A.copy()
        memo=[[0]*N for _ in range(N)]
        output=[]
        pre_output=[]
        loss=0  
        for i in range(N):
            for j in range(N):
                if j+1<N and A[i][j]==A[i][j+1]:
                    memo[i][j+1]=1
                # elif j+2<N and A[i][j]==A[i][j+2]:
                #     A[i][j+1]=A[i][j]
                #     pre_output.append((i,j+1,A[i][j]))
                #     memo[i][j+1]=1

                if i+1<N and A[i][j]==A[i+1][j]:
                    memo[i+1][j]=1
                # elif i+2<N and A[i][j]==A[i+2][j]:
                #     A[i+1][j]=A[i][j]
                #     pre_output.append((i+1,j,A[i][j]))
                #     memo[i+1][j]=1

                if A[i][j]==n or memo[i][j]:
                    memo[i][j]=1
                else:
                    output.append((i,j,n))
                    loss+=1
                    memo[i][j]=1
                
                

        if loss<min_loss:
            final_output=pre_output+output
            min_loss=loss
        
    print(len(final_output))
    for i,j,n in final_output:
        if not DEBUG:
            print(i+1,j+1,n)

    if DEBUG:
        f.close()
        with open ('out1.txt','w') as f:
            f.write(str(len(final_output))+'\n')
            for i,j,n in final_output:
                f.write('{} {} {}\n'.format(i,j,n))
            
main()