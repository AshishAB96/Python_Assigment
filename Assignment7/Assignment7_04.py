from  functools import reduce










def main():
    data = []
    print("enter the size of list:")    
    size = int(input())


    for i in range(size):
        no = int(input())   
        data.append(no) 


    rData = reduce(lambda A,B: A * B  , data)


    print("Product is : ",rData)



if __name__ == "__main__":
    main()