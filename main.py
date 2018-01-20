import os
print("This is John's awsome (basic) calculator here are a few ground rules:")
print("1. Only use two numbers")
print("2. No fractions")

numb = input("What is your first number?") #ask for the users input
print("1 = Add")
print("2 = Subtract")
print("3 = Divide")
print("4 = Times")
print("6 = Cube")
pythag=input("Would you like me to work out the length of the hypotenuse of a right angles triangle? [y/n]")

if operator == "5":
      print(numb," squared  is", int(numb)*int(numb))
elif operator == "6":
        print (numb, " cubed is",  int(numb)*int(numb)*int(numb))

    #ask user for their fist number
    numb = input("What is your first number?")
    print("1 = Add")
    print("2 = Subtract")
    print("3 = Divide")
    print("4 = Times")
    print("5 = Square")
    print("6 = Cube")
    print("7 = Square root")
    print("8 = Cube root")

    #ask user whoch operator they would like to use
    operator = input("What operator would you like to use?")
    #is square or cuben work out answer and end
    if operator == "5":
        print(numb," squared  is", int(numb)**2)
    elif operator == "6":
        print (numb, " cubed is",  int(numb)**3)
    elif operator == "7":
        print("The square root of ", numb, " is ", int(numb)**(1/2))
    elif operator == "8":
        print("The cube root of ", numb, " is ", int(numb)**(1/3))

    else:
        #if anything else ask for second number and work out answer
        numb2 = input("What is your second number?")
        if operator == "4":
            print(numb,"*",numb2,"=", int(numb)*int(numb2))
        elif operator == "3":
            print(numb,"/",numb2,"=", int(numb)/int(numb2))
        elif operator == "1":
            print(numb,"+",numb2,"=", int(numb)+int(numb2))
        elif operator == "2":
            print(numb,"-",numb2,"=", int(numb)-int(numb2))
        else:
            print("You did something wrong try again and make sure you read my rules.")
os.system("pause")
