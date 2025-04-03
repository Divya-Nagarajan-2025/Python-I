import streamlit as s
s.title("Simple Calculator Site")
choice= s.radio("Select the operation that has to be performed:",["add","sub","mul","div","exit"])
if choice == "exit":
  s.write ("Exit")
else:
 x=s.number_input("Enter the first number")
 y=s.number_input("Enter the second number")
 if choice == "add":
  s.write(f"the result of addition is {x+y}")
 elif choice == "sub":
  s.write(f"the result of subtraction is {x-y}")
 elif choice == "mul":
  s.write(f"the result of mullication is {x*y}")
 elif choice == "div":
  if y==0:
   s.write ("cannot divide by zero")
  else:
   s.write(f"the result of division is {div(x,y)}")
  
