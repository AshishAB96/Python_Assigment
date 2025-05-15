


def AddDigits(no):
    isum = 0
    idigit = 0


    while(no != 0):
        idigit = no % 10
        isum = isum + idigit
        no = no // 10

    return isum 
    

def main():
    print("Enter the number : ")
    ivalue = int(input())

    result = AddDigits(ivalue)
    print("Addition of digit is ;",result)

if __name__ == "__main__":
    main()