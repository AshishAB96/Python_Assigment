


Square  = lambda no : no * no

Cube = lambda no : no ** no
 




def main():
    print("enter the number : ")
    Value  = int(input())


    ret = Square(Value)

    print("Squre is : ",ret)

    ret = Cube(Value)

    print("Cube is ",ret)



if __name__ == "__main__":
    main()