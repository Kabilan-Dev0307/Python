class testClass:
    #list out the items in the list
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")

    #function that checks whether the given number is Odd or Even
    def oddEven():
        num = int(input("Enter a number: "))
        if int(num) % 2 == 0:
            print(num, "is Even number")
        else:
            print(num, "is Odd number")

    #function that tells elegibility of marriage for male and female according to their age limit like 21 for male and 18 for female
    def Elegibility():
        gender = input("Enter Gender: ")
        age = int(input("Enter age: "))
        if age >= 21:
            print("Your Gender", gender)
            print("Your Age", age)
            print("ELIGIBLE FOR MARRIAGE")
        else:
            print("Your Gender", gender)
            print("Your Age", age)
            print("NOT ELIGIBLE FOR MARRIAGE")

    # calculate the percentage of your 10th mark
    def Percentage():
        sub1 = int(input("Enter Subject1 mark="))
        sub2 = int(input("Enter Subject2 mark="))
        sub3 = int(input("Enter Subject3 mark="))
        sub4 = int(input("Enter Subject4 mark="))
        sub5 = int(input("Enter Subject5 mark="))
        total_marks = 500
        marks = sub1 + sub2 + sub3 + sub4 + sub5
        percentage = (marks / total_marks) * 100    
        print("Subject1 =", sub1)
        print("Subject2 =", sub2)
        print("Subject3 =", sub3)
        print("Subject4 =", sub4)
        print("Subject5 =", sub5)
        print("Total : ", marks)   
        print("Percentage : ", percentage)
    
    #print area and perimeter of triangle using class and functions
    def Triangle():
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        side1 = float(input("Enter the first side of the triangle: "))
        side2 = float(input("Enter the second side of the triangle: "))
        side3 = float(input("Enter the third side of the triangle: "))
        
        area = 0.5 * base * height
        perimeter = side1 + side2 + side3
        
        print("Breadth : ", base)
        print("Height : ", height)    
        print("Area formula: (Height*Breadth)/2")
        print("Area of the triangle:", area)
        print("Height1 : ", side1)
        print("Height2 : ", side2)
        print("Breadth : ", side3)
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of the triangle:", perimeter)