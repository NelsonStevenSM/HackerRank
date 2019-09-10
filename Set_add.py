if __name__=="__main__":

    stamp = []

    N = int(input())

    for i in range(N):

        country = input()

        if len(stamp) == 0:
            stamp.append(country)
        else:
            if country not in stamp :
                stamp.append(country)
            else:
                continue



    print(len(stamp))



