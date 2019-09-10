def merge_the_tools(N,k):
    subsequente = []
    for t in range(0,len(N),k):
        for u in range(t,t+k):
            if len(subsequente) == 0:
                subsequente.append(N[u])
            else :
                if N[u] not in subsequente:
                    subsequente.append(N[u])

        print("".join(subsequente))

        subsequente = []


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


        
        
