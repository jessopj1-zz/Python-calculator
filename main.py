print("This is John's awsome (basic) calculator here are a few ground rules:")
print("1. Only use two numbers")
print("2. No fractions")

numb = input("What is your first number?") #ask for the users input
print("1 = Add")
print("2 = Subtract")
print("3 = Divide")
print("4 = Times")
print("5 = Square")
print("6 = Cube")

operator = input("What operator would you like to use?") #life=42
if operator == "5":
      print(numb," squared  is", int(numb)*int(numb))
elif operator == "6":
        print (numb, " cubed is",  int(numb)*int(numb)*int(numb))

else:
    numb2 = input("What is your second number?")
    if operator == "4":
        print(numb,"*",numb2,"=", int(numb)*int(numb2))
    elif operator == "3":
          print(numb,"/",numb2,"=", int(numb)/int(numb2))
    elif operator == "1":
          print(numb,"+",numb2,"=", int(numb)+int(numb2))
    elif operator == "2":
          print(numb,"-",numb2,"=", int(numb)-int(numb2))
os.system("pause")
