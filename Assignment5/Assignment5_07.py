

def Area(length  , width ):

    Area = 0
    Area = length * width 

    return Area

def Perimeter(length , Width):
    Perimeter = 0

    Perimeter = 2 * (length + Width)

    return Perimeter



def main():
    print("Enter the length : ")
    value1 = int(input())

    print("Enter the Width : ")
    value2 = int(input())

    ret = Area(value1,value2)
    print("Area is  : ",ret)

    ret = Perimeter(value1 , value2)
    print("Perimeter is : ",ret)


if __name__ == "__main__":
    main()