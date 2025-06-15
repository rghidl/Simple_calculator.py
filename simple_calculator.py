

while True: 
  try:
    pick_func=int(input("Pick a function: \n 1-multiply \n 2-divide \n 3-add \n 4-subtract "))
   
    if pick_func not in [1,2,3,4]:
       print("❌invalid function number try again.")
       continue

    num1=int(input(" Pick the first number:"))
    num2=int(input(" Pick the second number:"))

   

    if pick_func ==1:
      print(num1*num2)

    elif pick_func==2:
      print(num1 / num2)

    elif pick_func==3:
      print(num1+num2) 

    elif pick_func==4 :
      print(num1-num2)
     
    break

  except ZeroDivisionError:
    print("❌ You can't divide by zero!")
  except ValueError:
    print("❌ Invalid input, please enter numbers only.")
  else:
    print("Operation successful ✅. ")
