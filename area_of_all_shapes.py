choice = 0
while(choice!=5):
    print("1. find area of circle")
    print("2. find area of triangle")
    print("3. find area of square and rectangle")
    print("4. find simple interest")
    print("5. Exit")
    choice = int(input("enter your choice:"))
    if choice==1:
        PI = 3.14
        radius = int(input("enter the circle's radius:"))
        area = PI * radius * radius
        circumference = 2 * PI * radius
        print(f"area of circle is {area}")
        print(f"circumfrence of circle is {circumference}")
    elif choice==2:
        a=float(input("enter first side"))
        b=float(input("enter second side"))
        c=float(input("enter third side"))

        s=(a*b*c)/2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
    elif choice==3:
        side = int(input("enter side of square:"))
        square_area = side*side
        width = float(input("enter width:"))
        height = float(input("enter height:"))
        area = width * height
        peri = 2 * (width + height)
        print(f"area of square is {square_area}")
        print(f"area of rectangle is {area}")
        print(f"perimeter is {peri}")
    elif choice==4:
        p=int(input("enter P:"))
        r=int(input("enter R:"))
        n=int(input("enter N:"))
        i=(p*r*n)/100
        print(f"simple interest is {i}")
    elif choice==5:
        exit()
    else:
        print("Game Over")