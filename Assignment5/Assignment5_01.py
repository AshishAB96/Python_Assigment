




def Sum(no1 , no2):

    Ans = 0

    Ans  = no1  + no2

    return Ans


def Difference(no1 , no2):
    Ans = 0

    Ans = no1 - no2

    return Ans 



def  Product(no1 , no2):
    Ans  = 0 
    Ans = no1 * no2
    return Ans


def Division(no1 ,no2):
    Ans = 0 

    Ans = no1 / no2

    return Ans



def main():
    print("Enter the first number :")
    iValue1 = int(input())

    print("Enter the Second number :")
    iValue2 = int(input())

    

    iRet  = Sum(iValue1 , iValue2)
    
    print("Sum is ",iRet)
    iRet = Difference(iValue1 , iValue2)

    print("Difference :",iRet)

    iRet =  Product(iValue1 , iValue2)

    print("Product is : ",iRet)


    iRet = Division(iValue1, iValue2)

    print("Division is : ",iRet)


if __name__ == "__main__":
    main()