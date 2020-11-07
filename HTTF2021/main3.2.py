#一旦全部回収して、下に詰めて置きなおしてから、順番に取り直す
#回収と置きなおしを同時に行う（置きなおしの作業100回分がなくなる）
#x,y入れ替え
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
    from collections import deque
    C=[[-1]*20 for _ in range(20)]
    C2=[[-1]*20 for _ in range(20)]
    
    poses=[(-1,-1)]*100
    poses2=[(-1,-1)]*100

    if DEBUG:
        filenum=0
        with open ('inputs/testCase_{}.txt'.format(filenum)) as f:
            lines=list(f.readlines())
            for i in range(100):
                x,y=map(int,lines[i].split())
                C[x][y]=i
                poses[i]=(y,x)
    else:
        for i in range(100):
            x,y=map(int,sys.stdin.readline().split())
            C[x][y]=i
            poses[i]=(y,x)


    output=[]
    stack=deque()

    for h in range(20):
        for w in range(20):
            y=h
            x=w if h%2==0 else 19-w
            n=C[x][y]
            if n+1:#数字マス
                if h<15:#数字マス＆上層
                    stack.append(n)
                    output.append('I')
                    C2[x][y]=-1
                else:#数字マス＆下層
                    C2[x][y]=C[x][y]
                    poses2[C[x][y]]=(y,x)
            else:
                if h<15:#空マス＆上層
                    pass
                else:#空マス＆下層
                    n=stack.pop()
                    output.append('O')
                    C2[x][y]=n
                    poses2[n]=(y,x)

            if w!=19:
                output.append('D' if h%2==0 else 'U')
            else:
                if h!=19:
                    output.append('R')

    nowy=19
    nowx=0
    log(C2)
    for i in range(100):
        y,x=poses2[i]
        dy=y-nowy
        dx=x-nowx
        if dx>0:
            output+=['D']*dx
        else:
            output+=['U']*(-dx)

        if dy>0:
            output+=['R']*dy
        else:
            output+=['L']*(-dy)
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