def Factorial(no):
    Factorial = 1
    for i in range(1,no + 1):
        Factorial = i * Factorial
    return Factorial
        
def main():
    print("Enter the Number : ")
    no = int(input())

    result = Factorial(no)  
    print("factorail is : ",result)

if __name__ == "__main__":
    main()