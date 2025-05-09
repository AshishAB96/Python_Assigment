


def CheckNum(no):
    bFlag = False
    if(no % 5 == 0):
        bFlag = True
    else:
        bFlag = False

    return bFlag

def main():
    print("Enter the number :" )    
    no = int(input())

    ret = CheckNum(no)
    
    if(ret == True):
        print("True")
    else:
        print("Flase")



if __name__ == "__main__":
    main()