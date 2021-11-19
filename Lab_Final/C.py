def too():
    try:
        x=float(input("Enter a number: "))
        y=float(input("Enter another number: "))
        print("The sum is",float(x+y))    
    except Exception as e:
         e="Error: Invalid input"
         print(e)
         too()
too()         
