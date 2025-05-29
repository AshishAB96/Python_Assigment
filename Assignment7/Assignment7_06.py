'''
    problem : Accept the list from user and return list of prime number 

'''

def DiplayPrime(iValue):

    iList = []
     
    for i in iValue :
        bFlag = False
        for j in range(2,iValue[i]):
            if(iValue[i] % j == 0):
                bFlag = True 
                break
        if bFlag == False:
            iList.append(iValue[i])
    
    return iList


def main():

    iValue = []

    print("Eneter the Size of list : ")
    try:
        iSize = int(input())
    
    except(ValueError):
        print("Invalid input ! , pealse enter the Valid input : ")
        return

    print("Eneter the Elements : ")
    for i in range(iSize):
        ino = int(input())
        iValue.append(ino)

    iRet = DiplayPrime(iValue)
    print("Prime number are : ",iRet)

if __name__ == "__main__":
    main()