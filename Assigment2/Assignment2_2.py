

def Display(no):
    for i in range(no):
        for j in range(no):
            print("*", end=" ")
        print()  # This moves to the next line after printing each row

def main():
    print("Enter the number : ")
    no1 = int(input())
    Display(no1)

if __name__ == "__main__":
    main()