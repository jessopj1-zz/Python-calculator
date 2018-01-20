import os
mylist=[]
mylist2=[]
print("This is John's awsome (basic) calculator here are a few ground rules:")
print("1. Only use two numbers")
print("2. No fractions")
print("I can do lots of different types of things including working out the length of a hypotenuse of a right angled triangle, I can also calculate different types of averages, or I can do normal calculator things like addition, subtraction, division, multiplication, square and cube rooting and a few other things")
print("Normal = 1")
print("Averages = 2")
print("Pythagoras' theorum = 3")
#asks user what they want to do
mode=int(input("Which mode would you like to use: "))

if mode == "1":
    #ask user for their fist number
    numb = int(input("What is your first number? "))
    mylist2.append(numb)
    #Asks which operation they would like to perform
    print("1 = Add")
    print("2 = Subtract")
    print("3 = Divide")
    print("4 = Times")
    print("5 = Square")
    print("6 = Cube")
    print("7 = Square root")
    print("8 = Cube root")

    #Ask user which operator they would like to use
    operator = input("What operator would you like to use? ")
    #If square/cube or square/cube root work out answer and end
    if operator == "5":
        print(numb," squared  is", int(numb)**2)
    elif operator == "6":
        print (numb, " cubed is",  int(numb)**3)
    elif operator == "7":
        print("The square root of ", numb, " is ", int(numb)**(1/2))
    elif operator == "8":
        print("The cube root of ", numb, " is ", int(numb)**(1/3))
    #Asks for second number then works out the answer
    numb2 = input("What is your second number? ")
    elif operator == "1":
        while (done == "n"):
            numb2 = int(input("What is your next number? "))
            done = input("Are you done yet? [y/n]")
            mylist.append(num2)
        print("Sum of ", mylist2, " = ", sum(mylist2))
    elif operator == "2":
        print(numb,"-",numb2,"=", int(numb)-int(numb2))
    elif operator == "3":
        print(numb,"/",numb2,"=", int(numb)/int(numb2))
    elif operator == "4":
        print(numb,"*",numb2,"=", int(numb)*int(numb2))


    else:
        print("You did something wrong try again and make sure you read my rules.")
elif mode == "2":
    print("At the moment I can only work out the mean I will try and add more at a later date")
    num = int(input("Please input your first number: "))
    mylist.append(num)
    done = "n"
    while (done == "n"):
        num2 = int(input("What is your next number? "))
        done = input("Are you done yet? [y/n]")
        mylist.append(num2)

    print("The mean of your numbers is ", sum(mylist)/len(mylist))
elif mode == "3":
    side=input("How long is one of the sides (that you know) ")
    side2 = input("How long is the other side? ")
    print("The sum to work out the hypotenuse is as follows A squared + B squared = C squared")
    hypotenuse=int(side)*int(side)+int(side2)*int(side2)
    print("The length of the hypotenuse is ", hypotenuse**(1/2))

else:
    print("You did something wrong please start again")
os.system("pause")
