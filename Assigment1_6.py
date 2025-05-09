def Checknum(no):
    if(no == 0):
        return "0"
    elif(no > 0):
        return True    
    elif(no < 0):
        return False
def main():

    print("Enter the number ")
    no = int(input())
    Ret = Checknum(no)
    if(Ret == True):
        print("Positive Number ")
    elif(Ret == False):
        print("Negative Number")
    elif(Ret == "0"):
        print("Zero")
if __name__ == "__main__":
    main()
