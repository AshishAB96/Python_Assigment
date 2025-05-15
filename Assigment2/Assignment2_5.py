def ChekPrime(no):

    bFlag = False 

    for i in range(2,no):
        if(no % i == 0):
            bFlag = False  
            break
        else:
            bFlag = True    
    return bFlag 

def main():
    print("Enter the number : ")
    ivalue = int(input())
    
    ret = ChekPrime(ivalue)

    if(ret == True):
        print("Given number is prime number :")
    else:
        print("Given number is not prime number ") 
        
if __name__ == "__main__":
    main()