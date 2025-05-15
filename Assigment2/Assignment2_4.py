def Addfactor(no):
    isum = 0
    i = 0

    for i in range(1,no):
        if(no % i == 0):
            isum = isum + i

    return isum

def main():
    print("Enter the number : ")
    ivalue = int(input()) 
    result = Addfactor(ivalue)
    print("Addition is : ",result)

if __name__ == "__main__":
    main()