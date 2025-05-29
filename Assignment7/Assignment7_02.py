





def main():

    num = []
    print("Enter the size of list ")
    size = int(input())


    print("Enter the Elements : ")
    
    for i in range(size):
        no = int(input())

        num.append(no)


    mnum  = list(map(lambda no : no * 2,num))
    print("Doubled List : ",mnum)

    

if __name__ == "__main__":



    main()