



def CheckLarge(Data):   

    iMax = 0
    if Data[0] > Data[1]:
        if Data[0] > Data[2]:
            if Data[0] > Data[3]:
                iMax = Data[0]

        else:
            iMax = Data[3]
    elif Data[1] > Data[2]:
        if Data[1] > Data[3]:
                iMax = Data[1]
        else:
            iMax = Data[3]
    elif Data[2] > Data[3]:
        iMax = Data[2]
    else:
        iMax  = Data[3]

    return iMax


def main():
    num = []

    print("enter the 3 number : ")

    for i in range(4):
        no = int(input())
        num.append(no)  

    iRet = CheckLarge(num)

    print("large number is : ",iRet)


if __name__ == "__main__":
    main()