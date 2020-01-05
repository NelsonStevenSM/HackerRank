if __name__=="__main__":

    N = int(input())

    for _ in range(N):

        (_, SetA) = (int(input()), set(map(int,input().split())))
        (_, SetB) = (int(input()), set(map(int,input().split())))


        print(len(SetA & SetB) == len(SetA))

