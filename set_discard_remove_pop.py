if __name__=="__main__":

    n = int(input())
    
    numbers = set(map(int,raw_input().split()))
    
    N = int(input())

    for _ in range(N):
        
        p1 = raw_input().split()

        if p1[0] == "remove":
            numbers.remove(int(p1[1]))
        elif p1[0] == "discard":
            numbers.discard(int(p1[1]))
        else:
            numbers.pop()
    

    print(sum(list(numbers)))
