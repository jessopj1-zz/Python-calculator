import os
additionList=[]
additionList2=[]
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
    if operator == "1":

        while (done == "n"):
            numb2 = int(input("What is your next number? "))
            done = input("Are you done yet? [y/n]")
            additionList.append(num2)
        print("Sum of ", additionList2, " = ", sum(additionList2))

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
        print("The length of the hypotenuse is ", unknown**(1/2))

    elif type == "other":
        side = input("How long is one of the sides (the longer of the two) ")
        side2 = input("How long is the other side? ")
        print("The sum to work out the hypotenuse is as follows C squared + A squared = B squared")
        unknown=int(side)**2-int(side2)**2
        print("The length of the hypotenuse is ", unknown**(1/2))

    else:
        print("Incorrect command please start again")

else:
    print("Incorrect command please start again")
os.system("pause")
