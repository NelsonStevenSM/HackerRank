if __name__=="__main__":
    _ = int(input())
    (_,setA) =(int(input()), set(map(int,input().split())))

    N = int(input())

    for _ in range(N):
        (cmd, lista) = (input().split()[0],set(map(int, input().split())))
        
        eval("setA.{0}({1})".format(cmd,lista))

    print (sum(setA))


