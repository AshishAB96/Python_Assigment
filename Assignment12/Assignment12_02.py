class Circle:
    PI = 3.14
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
    def Accept(self,A):
        self.Radius = A
    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * (Circle.PI) * self.Radius

    def Display(self):

        print("Radius is : ",self.Radius)
        print("Area of Circle is ",self.Area)
        print("Area of Circumference is ",self.Circumference)

def main():

    Obj1 = Circle()
    Obj2 = Circle()

    Obj1.Accept(10.2)
    Obj1.CalculateArea()
    Obj1.CalculateCircumference()
    Obj1.Display()

    Obj2 = Circle()
    Obj2.Accept(11.2)
    Obj2.CalculateArea()
    Obj2.CalculateCircumference()
    Obj2.Display()

if __name__ == "__main__":
    main()