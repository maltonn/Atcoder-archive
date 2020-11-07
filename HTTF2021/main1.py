#愚直に0から順番にとってく
DEBUG=True
def log(x):
    if DEBUG:
        print(x)

def main():
    import sys
    C=[[-1]*20 for _ in range(20)]
    poses=[(-1,-1)]*100

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
    nowy=0
    nowx=0
    
    for i in range(100):
        y,x=poses[i]
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
        
    if DEBUG:
        with open ('outputs/out.txt','w') as f:
            f.write(''.join(output))
    else:
        print(''.join(output))

main()