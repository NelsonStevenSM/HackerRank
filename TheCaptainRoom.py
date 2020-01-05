if __name__=="__main__":

    K = int(input())

    room = list(map(int,input().split()))

    kk = int((len(room)-1)/K)

    conjunto = set(room)

    for i in conjunto:
        cont = 0
        for j in room:
            if i == j :
                cont+=1

            if cont > 1:
                break

        if cont == 1:
            result = i
            print(result)
            break


