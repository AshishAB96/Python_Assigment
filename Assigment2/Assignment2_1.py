import Arithematic



def main():
    print("Enter the first number :")
    value1 = int(input())

    print("Enter the Second number :")
    value2 = int(input())

    result = Arithematic.Addition(value1 , value2)
    print("Addition of two number is : ",result)

    result = Arithematic.Substraction(value1 , value2)
    print("Substraction of two number is : ",result)
       
    result = Arithematic.Division(value1 , value2)
    print("Division  of two number is : ",result)   

    result = Arithematic.Multiplication(value1 , value2)
    print("Multiplication  of two number is : ",result)    

    
if __name__ == "__main__":
    main()