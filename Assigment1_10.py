
def Displaylen(str):
    iCnt = 0
    i = 0

    while(i < len(str)):
        iCnt = iCnt + 1
        i = i + 1
    return  iCnt


def main():
    print("Enter the string : ")
    str = input()       

    Ret = Displaylen(str)
    print("Length is :",Ret)

if __name__ == "__main__":
    main()