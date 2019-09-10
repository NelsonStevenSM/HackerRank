if __name__=="__main__":

    n = int(input())
    English = set(map(int,input().split()))

    m = int(input())
    France = set(map(int,input().split()))

    print("Union: ",len(English | France))
    print("Intersección: ",len(English & France))
    print("Diferencia: ",len(English - France))
    print("Diferencia Simetrica: ",len(English ^ France))

