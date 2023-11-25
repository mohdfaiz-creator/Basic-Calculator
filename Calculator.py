print("welcome to Faiz's calculator")
x = input("What is your first number:")
y = input("What is your second numbed:")
o = input("What operation do you want:")
if o == "+":
  print("Answer:" , int(x) + int(y))
elif o == "-":
  print("Answer:" , int(x) - int(y))
elif o == "*":
  print("Answer:" , int(x) * int(y))
elif o == "/":
  print("Answer:" , int(x) / int(y))
elif o == "^":
  print("Answer:" , int(x) ** int(y))
else:
  print("Invalid Input")