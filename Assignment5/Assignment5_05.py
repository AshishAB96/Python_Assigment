


def CheckEvenOdd(no):

    if no % 2 == 0:
        return True
    else:
        return False
    
def main():
    print("entee the number : ")
    iValue = int(input())


    bRet = CheckEvenOdd(iValue)

    if bRet == True:
        print(iValue," number if Even number ")
    else:
        print(iValue,"number if Odd Number : ")

if __name__ == "__main__":
    main()