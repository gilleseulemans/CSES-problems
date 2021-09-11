def main():
    n = input()
    list1 = []
    
    list2 = [1]
    counter = 1

    for i in n:
        list1.append(i)
    current = list1[0]
    for i in range(len(list1) - 1):
        
        if current == list1[i+1]:
            counter += 1
            list2.append(counter)
        else:
            
            counter = 1
            current = list1[i+1]

    list2.sort()
    
    print(list2[len(list2) -1])



        



if __name__ == "__main__":
    main()
