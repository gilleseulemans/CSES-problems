#first input line contains an integer n
#giving numbers between 1 and n with one missing number, find tehe number

def main():
    n = int(input())
    n2 = input().split()
    i = n
    sum = 0
    sum2 = 0
    list = []

    for x in n2:
            sum2 += int(x)
        

    while i != 0:
        sum += i
        i -= 1

    number = sum - sum2

    print(number)
        
    



 

 
         

if __name__ == "__main__":
    main()  