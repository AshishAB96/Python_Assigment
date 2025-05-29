

def checkEligibility(Age):

    if Age < 0:
        Age = -Age


    if Age >= 18:
        return True
    else:
        return False 

def main():
    print("Enter your age :")
    iValue = int(input())

    bRet = checkEligibility(iValue)


    if bRet == True:
        print("Your are Eligible for Vote : ")
    else:
        print("You are not Eligible for vote : ")


if __name__ == "__main__":
    main()