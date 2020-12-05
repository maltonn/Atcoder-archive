import sys
def solve():
    cost=0
    ax,ay,bx,by,cx,cy=list(map(int,sys.stdin.readline().split()))
    if (ax>=0 and ay>=0) and (bx>=0 and by>=0) and (cx>=0 and cy>=0):
        pass
    elif (ax<=0 and ay<=0) and (bx<=0 and by<=0) and (cx<=0 and cy<=0):
        cost+=2
    else:
        cost+=1


    zen=(abs(x) for x in (ax,ay,bx,by,cx,cy))
    ax,ay,bx,by,cx,cy=zen
    
    x_far=max(ax,bx,cx)
    x_ner=x_far-1

    y_far=max(ay,by,cy)
    y_ner=y_far-1

    cost+=min(x_ner,y_ner)*3

    if [ax,bx,cx].count(x_ner)==2 and [ay,by,cy].count(y_ner)==2:
        cost+=2*abs(x_ner-y_ner)
    elif (y_ner<x_ner and [ax,bx,cx].count(x_ner)==1 and [ay,by,cy].count(y_ner)==2) or (y_ner>x_ner and [ax,bx,cx].count(x_ner)==2 and [ay,by,cy].count(y_ner)==1):
        cost+=1
        cost+=2*abs(x_ner-y_ner)
    else:
        cost+=1
        cost+=2*abs(x_ner-y_ner)
    return cost

def main():
    T=int(sys.stdin.readline())
    for _ in range(T):
        print(solve())


if __name__=='__main__':
    main()