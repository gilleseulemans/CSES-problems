def main():
    n = int(input())
    n2 = input().split()
    if n == 2:
        print(2)
        return
    list1 = []
    list2 = []
    num = 0

    for i in n2:
        if i not in list2:
            list2.append(int(i));

    list2.sort()
    list2.reverse()

    for i in range(len(list2) -1):
        if list2[i] != list2[i+1] +1:
            num = list2[i+1] +1

    if num == 0:
        print(list2[len(list2)])
    else:
        print(num)     

if __name__ == "__main__":
    main()  

