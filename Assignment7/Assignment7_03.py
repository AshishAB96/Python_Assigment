

def main():

    Data = []

    print("Enter the size of list : ")     
    size = int(input())

    for i in range(size):
        no = int(input())   
        Data.append(no)


    fData = list(filter(lambda no : no % 2 ==0 , Data))

    print("Even number  : ",fData)


if __name__  == "__main__":
    main()