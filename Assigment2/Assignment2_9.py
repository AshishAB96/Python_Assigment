def CountDegit(no):
    iCnt = 0

    while(no != 0):
        iCnt = iCnt + 1
        no = no // 10

    return iCnt

def main():
    print("Enter the number :")
    ivalue = int(input())
    result = CountDegit(ivalue)
    print("Count is : ",result)


if __name__ == "__main__":
    main()