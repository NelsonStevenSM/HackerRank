if __name__=="__main__":

    SetA = set(map(int,input().split()))
    N = int(input())
    cont = 0
    for _ in range(N):
        SetB = set(map(int,input().split()))
        
        if len(SetA & SetB) == len(SetB):
            cont+=1


    if cont == N : 
        print("True")
    else:
        print("False")


