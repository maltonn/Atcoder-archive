#一旦全部回収して、真ん中に置きなおしてから、順番に取り直す
#回収と置きなおしを同時に行う（置きなおしの作業100回分がなくなる）
#取り直しの際、「次の次」を見つけたら、それを拾って「次」の近くに置く

DEBUG=False
def log(x):
    if not DEBUG:
        return 
    if type(x)==list and type(x[0])==list:
        for line in x:
            print(line)
    else:
        print(x)

def dist(y1,y2,x1,x2):
    return abs(y2-y1)+abs(x2-x1)

def goto(nowy,y,nowx,x):
    output=[]
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
    return output
    
def main():
    import sys
    from collections import deque
    C=[[-1]*20 for _ in range(20)]
    C2=[[-1]*20 for _ in range(20)]
    
    poses=[(-1,-1)]*100
    poses2=[(-1,-1)]*100

    if DEBUG:
        filenum=5
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
    stack=deque()

    h=0
    w=0
    dr='R'
    while True:
        y=h
        x=w
        n=C[y][x]
        if n+1:#数字マス
            if 5<=y<=14 and 5<=x<=14:#数字マス＆中
                C2[y][x]=C[y][x]
                poses2[C[y][x]]=(y,x)
            else:#数字マス＆外
                stack.append(n)
                output.append('I')
                C2[y][x]=-1
        else:#空マス
            if 5<=y<=14 and 5<=x<=14:#空マス＆中
                n=stack.pop()
                output.append('O')
                C2[y][x]=n
                poses2[n]=(y,x)
            else:#空マス＆外
                pass
    
        if y==10 and x==9:
            break


        if y==x+1 and y<=9:
            dr='R'
        elif y==x and y>9:
            dr='L'
        elif y+x==19 and y<=9:
            dr='D'
        elif y+x==19 and y>9:
            dr='U'
        
        output.append(dr)
        if dr=='R':
            w+=1
        elif dr=='L':
            w-=1
        elif dr=='D':
            h+=1
        elif dr=='U':
            h-=1
        else:#no case
            pass

    nowy=10
    nowx=9
    log(C2)


    for i in range(100):
        y,x=poses2[i]

        if i!=99:
            ynxt,xnxt=poses2[i+1]#「次の次」
            
            mn=100
            yspace=-1
            xspace=-1
            for d1 in [-2,-1,0,1,2]:
                for d2 in [-2,-1,0,1,2]:
                    if C2[y+d1][x+d2]==-1:
                        tmp=dist(nowy,ynxt,nowx,xnxt)+dist(ynxt,y+d1,xnxt,x+d2)+2*dist(y+d1,y,x+d2,x)
                        #sart -> 「次の次」　→　「次」付近の空きマス　→　「次」　→「次」付近の開きマス（「次の次」が入ってる）
                        if tmp<mn:
                            yspace=y+d1
                            xspace=x+d2
                            mn=tmp
            
            if mn<dist(nowy,y,nowx,x)+dist(y,ynxt,x,xnxt):#途中で「次の次」を拾って「次」の近くに置いておくかどうか
                output+=goto(nowy,ynxt,nowx,xnxt)
                output.append('I')
                C2[ynxt][xnxt]=-1

                output+=goto(ynxt,yspace,xnxt,xspace)
                output.append('O')
                C2[yspace][xspace]=i+1
                poses2[i+1]=(yspace,xspace)
                nowy=yspace
                nowx=xspace


        output+=goto(nowy,y,nowx,x)
        output.append('I')
        C2[y][x]=-1
        nowy=y
        nowx=x


    if DEBUG:
        with open ('outputs/out.txt','w') as f:
            f.write(''.join(output))
    else:
        print(''.join(output))

main()