def main():
    n = int(input())
    n2 = input().split()
    moves = 0
    
    list = []
    for x in n2:
        list.append(int(x))
    
    for i in range(n-1):
        if list[i] > list[i+1]:
            moves += (list[i] - list[i+1])
            list[i+1] = list[i]
    
    if list[n - 1 ] < list[n - 2]:
        moves += (list[n -2] - list[n - 1])
    
    print(moves)

    
if __name__ == "__main__":
    main()