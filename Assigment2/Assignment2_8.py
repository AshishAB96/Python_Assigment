def  DisplayPattern(no):
    
    for i in range(1, no + 1):
        for j in range(1, no + 1):
            if ((i == j ) or (i > j)):
                print(j , end= "  ")
            else:
                print(" " , end = "  ")
        print()       

def main():
    print("Emter the number : ")
    no = int(input())
    DisplayPattern(no)

if  __name__  == "__main__":
    main()