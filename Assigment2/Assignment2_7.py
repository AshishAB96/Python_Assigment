



def DisplayPattern(no):

    for i in range(1, no + 1):
        for j in range(1, no + 1):
            print(j,end = "  ") 
        print()



def main():
    print("Enter the number ")  
    no = int(input())

    DisplayPattern(no)

if __name__ == "__main__":
    main()