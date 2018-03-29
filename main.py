import os
def power(x, y):
    return x**y

additionList=[]
print("This is John's awsome (basic) calculator here are a few ground rules:")
print("Only use two numbers")
print("No fractions")
print("I can do lots of different types of things including working out the length of a hypotenuse of a right angled triangle, I can also calculate different types of averages, or I can do normal calculator things like addition, subtraction, division, multiplication, square and cube rooting and a few other things")
print("Normal = 1")
print("Averages = 2")
print("Pythagoras' theorum = 3")
#asks user what they want to do
mode=input("Which mode would you like to use: ")

if mode == "1":
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Square, Square Root, Cube, Cube root")
    operator = input("Which operator would you like to use? ")
    if operator == "1":

        while (done == "n"):
            numb2 = int(input("What is your next number? "))
            done = input("Are you done yet? [y/n]")
            additionList.append(num2)
        print("Sum of ", additionList, " = ", sum(additionList))

    elif operator == "2":

        print(numb,"-",numb2,"=", int(numb)-int(numb2))

    elif operator == "3":

        print(numb,"/",numb2,"=", int(numb)/int(numb2))

    elif operator == "4":
        numb = input("What is your fist number? ")
        ans = numb
        numb2 = int(input("What is your next number? "))

        while (done == "n"):
            numb2 = int(input("What is your next number? "))
            done = input("Are you done yet? [y/n]")
            additionList.append(numb2)
            ans = ans*numb2

        print(additionList, "all multiplied = ", ans)

    elif operator == "5":
        x = input("What number would you like to use? ")
        print("To what power would you like to work it out")
        y = input("0.5 is the square root, 0.33333 is the cube root")
        ans=power(x, y)
        print("your answer is", ans)

    else:
        print("You did something wrong try again and make sure you read my rules.")

elif mode == "2":
    print("At the moment I can only work out the mean I will try and add more at a later date")
    num = int(input("Please input your first number: "))
    additionList.append(num)
    done = "n"
    while (done == "n"):
        num2 = int(input("What is your next number? "))
        done = input("Are you done yet? [y/n]")
        additionList.append(num2)

    print("The mean of your numbers is ", sum(additionList)/len(additionList))

elif mode == "3":
    type = input("Do you want to find out the length of the hypotenuse or one of the other side? [other/hyp]")

    if type == "hyp":
        side = input("How long is one of the sides (that you know) ")
        side2 = input("How long is the other side? ")
        print("The sum to work out the hypotenuse is as follows A squared + B squared = C squared")
        unknown=int(side)**2+int(side2)**2
        print("The length of the hypotenuse is ", power(unknown, 0.5)

    elif type == "other":
        side = input("How long is one of the sides (the longer of the two) ")
        side2 = input("How long is the other side? ")
        print("The sum to work out the hypotenuse is as follows C squared + A squared = B squared")
        unknown=int(side)**2-int(side2)**2
        print("The length of the hypotenuse is ", power(unknown, 0.5))

    else:
        print("Incorrect command please start again")

else:
    print("Incorrect command please start again")
os.system("pause")
