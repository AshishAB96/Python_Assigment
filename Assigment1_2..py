
def ChkNUm(no):
    if(no % 2 == 0):
        print("Given number is Even number ")
    else:
        print("Given number is Odd Number : ")


def main():
    print("Enter the number :")
    value = int(input())

    ChkNUm(value)


if __name__ == "__main__":
    main()