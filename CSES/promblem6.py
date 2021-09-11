#t is number of tests
t = int(input())
i = 0


while i != t :
    number = 0
    yx = input().split()
    rij = int(yx[0])
    kol = int(yx[1])

    if kol == 1 and rij == 1:
        number = 1

    elif kol > rij and kol % 2 != 0:
        number = kol*kol - (rij -1)
    

    elif kol > rij and kol % 2 == 0:
        number = (kol - 1) * (kol-1) + rij


    elif kol < rij and rij %2 == 0:
        number = rij*rij - (kol -1)

    elif kol < rij and rij % 2 != 0:
        number = (rij - 1) * (rij -1) + kol
    elif kol == rij and kol%2 != 0:
        



    print(number)





    

