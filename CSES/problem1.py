#algo that takes in a pos int n if n is even the algo devides it by 2
# if n is odd multi by 3 +1 the algo repeats this until 1 

input = int(input())

def main():
    number = input
    list = []
    list.append(number)
    while number != 1:
        if number % 2 == 0:
            number = int(number / 2)
        else:
            number = int(number * 3 + 1 )
        list.append(number)

    for x in range(len(list)):
        print(list[x], end = " ")

        

  




if __name__ == "__main__":
    main()      
