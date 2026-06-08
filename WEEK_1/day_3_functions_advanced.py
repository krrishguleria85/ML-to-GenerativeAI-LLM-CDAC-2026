#functions and exception handling
#functions are reusable block of code that perform tge specific task which started by the term 'def' in python
#benefits: code readability, code usability, easy maintenance, and code adaptability 

#basic func ex..
def greet():
  print("Hello World!!")
greet()

#func to diplay student info..
def student():
  print("Student Name: Krrish")
  print("Course: Python, C++")
student()

print("-------------")
#calling functions
def greet_user():
  print("Hello User!!")

greet_user()

greet_user()
greet_user()
greet_user()

print("===========")
#function arg
def greet_user1(name):
  print("Hello", name)

greet_user1("Aman")
greet_user1("Rahul")


print("===========")
#parameters: variables that are passed withn function argument

def add(a,b):
  print (a+b)
add(10,20)

#return : sends a value back from a function
def add1(a,b):
  return a+b
result = add1(50,50)
print(result)


#banking example

def cal_balance(curr_bal,deposit):
  return curr_bal + deposit
result = cal_balance(15000, 5000)
print("New Balance: ",result)


print("=============")
print("Type of arguments")
#Arguments are the values passed to function when they are called.

#python supports:
#1. Positional Arguments
#2. keyword arguments
#3. Default arguments
#4. Variable-length arguments
#5. *args
#6. **kwargs

#example of Positional arguments
print("1. Positional Args Ex..")
print("Ex1...")
def student_info(name,age):
  print("Name: ", name)
  print("Age: ", age)
student_info("Aman", 21)
print(" ")

print("2. Keyword Args Ex..")
print("Ex1...")
def student_info(name,age):
  print(name)
  print(age)
student_info(name="Aman",age = 21)
print(" ")

print("3. Default Args Ex..")
print("Ex1...They are used when no args is provided.....")
def greet(name="Guest"):
  print("Welcome",name)
greet()
print(" ")

print("4. Variable-Length Args Ex..")
print("Ex1...(It allow passing multiple values to the function)")
def display_numbers(*numbers):
  print(numbers)
display_numbers(10,20)

display_numbers(10,20,30,40,50)
print(" ")


print("5. *Args Ex..")
print("Ex1...")
def add_no(*args):
  print(args)
add_no(10,20)

add_no(1,2,3,4,5,6)
print(" ")


print("6. **kwargs..")
print("Ex1...(keyword arguments collects all arguments values into dictonary)")
def stu_details(**kwargs):
  print(kwargs)

stu_details(name= "Rahul", age = 21, course = "Btech CSE")
print(" ")


print("Misc...Accessing dict. values")
def employee_details(**kwargs):
  for key,value in kwargs.items():
    print(key,":",value)
employee_details(name="Rahul", age = 21, dept="Web Develop..", salary= 25000)
print(" ")

print("================ Advanced Functions ================")
print("1. Lambda Function...")
#lambda function are small anonymous functions and the syntax is: lambda arguments : expression
print("Ex1: ")
square= lambda x :x*x
print(square(5))
print("Ex 2: ")
#addition
add= lambda a,b: a+b
print(add(10,20))
print("Ex 3: ")
#multiplication
multiply = lambda a,b:a*b
print(multiply(10,20))

print(" ")
print("2. Recursive Function..")
#recursive functions are the function which calls itself
print("Ex 1: Factorial Example..")

def factorial(n):
  if n==1:
    return 1
  return n*factorial(n-1)
print(factorial(5))
print(" ")


print("...Variable Scope...")
#scope determines where the variables are determined and to be accessed
#global, local scope
#non local, global keyword
print("1. local scope: variables created inside the function and they are accessed within the function")
print("2. global scope: variables created outside the function and they are accessed that function")
print("3. non- local keyword variable: it is used inside nested functions and it allows the modification of var from enclosing function")
def outer():
  count =10
  def inner():
    nonlocal count
    count+=5
    print("Inner Inner: ", count)
  inner()
  print("Inside Outer: ",count)
outer()
print(" ")

print("4. Global keyword: it allows changing of global variable inside the function..")
counter=0
def increment():
  global counter
  counter+=1
increment()
print(counter)
print(" ")
