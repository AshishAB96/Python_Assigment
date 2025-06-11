
class Arithematic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
    
    def Accept(self, A, B ):

        self.Value1 = A

        self.Value2 = B


    def Addition(self):

        Ans = self.Value1 + self.Value2

        return Ans
    
    def Substraction(self):

        Ans = self.Value1 - self.Value2

        return Ans

    def Multiplication(self):

        Ans = self.Value1 * self.Value2

        return Ans
    
    def Division(self):


        Ans = self.Value1 / self.Value2

        return Ans

def main():

    Obj1 = Arithematic()
    Obj2 = Arithematic()    

    Obj1.Accept(11,21)
    ret = Obj1.Addition()
    print("Addition is : ",ret)

    ret = Obj1.Substraction()
    print("Addition is : ",ret)

    ret = Obj1.Multiplication()
    print("Substraction is : ",ret)

    ret = Obj1.Division()

    print("Division is ",ret)
    

if __name__ == "__main__":
    main()