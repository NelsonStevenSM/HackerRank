if __name__=="__main__":

    A = int(raw_input())
    A_newlis = set(list(map(int,raw_input().split())))

    B = int(input())
    B_newlis = set(list(map(int,raw_input().split())))

    DifA = A_newlis.difference(B_newlis)
    DifB = B_newlis.difference(A_newlis)

    uA_B = DifA.union(DifB)

    rspt = sorted(uA_B)

    for i in rspt:
        print(i)

    
