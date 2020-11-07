#一旦全部回収して、下に詰めて置きなおしてから、順番に取り直す
DEBUG=True
def log(x):
    if not DEBUG:
        return 
    if type(x)==list and type(x[0])==list:
        for line in x:
            print(line)
    else:
        print(x)

def main():
    import sys
    C=[[-1]*20 for _ in range(20)]
    C2=[[-1]*20 for _ in range(20)]
    
    poses=[(-1,-1)]*100
    poses2=[(-1,-1)]*100

    if DEBUG:
        filenum=0
        with open ('inputs/testCase_{}.txt'.format(filenum)) as f:
            lines=list(f.readlines())
            for i in range(100):
                y,x=map(int,lines[i].split())
                C[y][x]=i
                poses[i]=(y,x)
    else:
        for i in range(100):
            y,x=map(int,sys.stdin.readline().split())
            C[y][x]=i
            poses[i]=(y,x)


    output=[]
    stack=[]

    for h in range(20):
        for w in range(20):
            n=C[h][w if h%2==0 else 19-w]
            if n+1:
                stack.append(n)
                output.append('I')
            if w!=19:
                output.append('R' if h%2==0 else 'L')
            else:
                if h!=19:
                    output.append('D')

    cnt=0
    for i in range(5):
        for j in range(20):
            output.append('O')
            y=19-i
            x=j if i%2==0 else 19-j
            C2[y][x]=stack[-cnt-1]
            poses2[stack[-cnt-1]]=(y,x)
            cnt+=1
            if j!=19:
                output.append('R' if i%2==0 else 'L')
            else:
                if i!=4:
                    output.append('U')
    

    nowy=15
    nowx=19
    log(C2)
    for i in range(100):
        y,x=poses2[i]
        dy=y-nowy
        dx=x-nowx
        if dx>0:
            output+=['R']*dx
        else:
            output+=['L']*(-dx)

        if dy>0:
            output+=['D']*dy
        else:
            output+=['U']*(-dy)
        output.append('I')
        nowy=y
        nowx=x
    

    #スコアを50点単位で落とす
    # for _ in range(2):
    #     if nowy!=0:
    #         output.append('U')
    #     else:
    #         output.append('D')

    if DEBUG:
        with open ('outputs/out.txt','w') as f:
            f.write(''.join(output))
    else:
        print(''.join(output))

main()