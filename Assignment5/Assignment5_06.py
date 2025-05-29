




def CelToFer(temp):

    Fehreneit = (temp * 9 / 5) + 32 

    return Fehreneit



def main():
    print("Enter the tempreture in Celsius  : ")
    Value = int(input())

    ret = CelToFer(Value)

    print("Temperature is Fahrenheit : ",ret)

if __name__ == "__main__":
    main()