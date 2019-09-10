if __name__=="__main__":

    n, m = raw_input().split()

    array = list(map(int, raw_input().split()))

    A = set(list(map(int, raw_input().split())))
    B = set(list(map(int, raw_input().split())))

    happiness = 0
    for i in array:
        if i in A : 
            happiness+=1
        
        if i in B :
            happiness-=1


    print(happiness)
