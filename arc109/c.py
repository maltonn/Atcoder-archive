def Fight(hands):
    if len(hands)==1:
        return hands[0]
        
    winners=[]
    for i in range(len(hands),2):
        winners.append(hands[i] if (hands[i+1]-hands[i])%3-1 else hands[i+1])
    
    Fight(tuple(winners))

def main():
    import sys
    n,k=list(map(int,sys.stdin.readline().split()))
    s=list(map(int,sys.stdin.readline().split()))
    dic={
        'R':0,
        'P':1,
        'S':2,
    }
    hands=[dic[x] for x in s]
    
    for i in range(n):
        


if __name__=='__main__':
    main()