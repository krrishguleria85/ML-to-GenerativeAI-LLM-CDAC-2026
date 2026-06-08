#continue to day1

#advanced datatype: 
#1. strings -> using str, " ", ' '


#string indexing

#ex = "Python Programming"
#print(ex[0]) #first char
#print(ex[1]) #second char
#print(ex[-2]) #second last char


#string slicing

#print(ex[0:2]) #sliced the index till first char mean 0,1 not 2
#print(ex[0:5])
#print(ex[2:8])
#print(ex[7:18])
#print(ex[7:])
#print(ex[::2])


#string methods

#text= "python ProGramming"
#print(text.lower())
#print(text.upper())
#print(text.title())
#print(text.capitalize())
#print(len(text))

name =" Krrish "
sentence = "I like C++"
print(name.strip())
print(sentence.replace('C++',"Python"))
#count
msg = "Python, Python, I like c++"
print(msg.count("Python"))

#split
msg2="Python,ML,AI"
print("Split:", msg2.split(','))


#f- strings
name = "Krrish"
age = 21
course = "Btech cse"
college_name = "Amity University Punjab"

print(f"Hi, I am {name}, and I am {age} years old, I currently pursuing my {course} at {college_name}")



#string immutability -> elements that are not change within it like tuple and other like list, dict are mutable elemnts
#string methods : list, sets, dic, tuples (imp for interview)

#list-> they are odered, mutable collection of items ate same time, they are mutable in each other
list1 =["Hi","I","am","in CDAC"]
print(list1[1:4])
print(list1[-1])

list2 =[10,20,30,40,50,60,70,80,90,100]
print(list2[0:4])
print(list2[2:8])
print(list2[::5])
print(list2[6::])
print(list2[-1::])

#list methods
#1.append func -> used to join one element to each other
list3 =["Python","ML"]
list3.append("AI")
print(list3)

list3.insert(2,"Data Science")
print(list3)

#3. remove()
list3.remove("AI")
print("remove: ",list3)

#4. pop()
list3.pop()
print("pop: ",list3)

#append and extend means like we having two lists so in append it joins two list one to each other but in extend it takes second list items and join to first list item
list4 = ["Cyber","Cloud"]
list3.append(list4)
print(list3)
list3.extend(list4)
print(list3)


print(list3.clear())

print("--------------------------")
#iterating lists
subjects = ["AI","ML","DS"]
for subject in subjects:
  print(subject)
  
#using index
print("Using non index: ")
for i in range(len(subjects)):
  print(subjects[i])

#using enamurate
print("Using index: ")
for index, subject in enumerate(subjects):
  print(index, subject)
  

print("----------------Tuple-----------------")
#tuple-> they are ordered, collection of items; created using (); immutable data items hold

#tuple packing
stu = ("Krrish",20, "CSE")
print("Tuple packing: ",stu)
#tuple unpacking -> extracting tuples items into assigned variables
stu =("Krrish",20, "CSE")
name , age, course = stu
print("Tuple unpacking: ", stu)


print("Tuple methods---->")
#count, index
no = (10,20,30,40,50,60,70)
print(no.count(10))
print(no.index(50))


print("---------------Sets---------------")
#sets: they are unordered collection of no, unique elements, enclosed in {}
no1 = {10,20,30,40,50}
print(no1)

sub25 = {"Python","ai","ml"}
print(sub25)

#sets methods -> 
#add()
sub25.add("DS")
print(sub25)
#update
sub25.update(["DS","Data Science"])
print(sub25)
#remove
sub25.remove("ai")
print(sub25)
#discard
sub25.discard("ml")
print(sub25)
#pop
sub25.pop()
print(sub25)


#sets operations
print("set opera-->")
set1 ={1,2,3,4}
set2 = {3,4,5,6}
print(set1)
print(set2)
#membership
print(3 in set1)
print(10 in set1)
#length
print(len(set1))
#1.subset
print(f"Subset of (1.2) in {set1} is", {1,2}.issubset(set1))
#2. subset
print(f"Subset of (3,4) in {set2} is ", {3,4}.issubset(set2))
#3. subset (f)
print(f"Subset of (5,6) in {set1} is ", {5,6}.issubset(set1))


print("sets operation --->")
#union and intersection
print("union: ")
python_stu={"AA","BB","CC"}
ai_stu={"BB","CC","CD"}
all_stu = python_stu.union(ai_stu)
print(all_stu)

print("intersection: ")
all_stu1 = python_stu.intersection(ai_stu)
print(all_stu1)

print("Difference: ")
all_stu2 = python_stu.difference(ai_stu)
print(all_stu2)

print("Symmetric Diff")
all_stu3 = python_stu.symmetric_difference(ai_stu)
print(all_stu3)

print("------------------- Dictonary ---------------------------")
student_1 = {
  "name":"Rahul",
  "age":20,
  "course": "python"
}
print(student_1["name"])
print(student_1["age"])
print(student_1["course"])
#using get
print("get(): ")
print(student_1.get("age"))
print(student_1.get("name"))

#dic methods
print("dictonary methods---->")
#keys
print("keys: ", student_1.keys())
#values
print("Values: ", student_1.values())
#update
student_1.update({'course':'java'})
print(student_1)
#copy()
new_stu1 = student_1.copy()
print(new_stu1)
#clear()
temp ={
  'a':1,
  'b':2
}
temp.clear()
print(temp)

print("\n")
print("----------------------Advanced Data Structure-------------------")
#array -> store item/elements of same data type
from array import array
#same as list


#stack -> follow lifo (last in first out)
stack = []
#push op
stack.append("Python")
stack.append("AI")
stack.append("ML")

print("stack is: ",stack)

#pop op.
removed_item = stack.pop()
print("Removed: ", removed_item, stack)

#peek op.
print("Top element: ", stack[-1])

#check stack size
print(len(stack))


#browser history example
history=[]
history.append("Youtube")
history.append("Netflix")
history.append("Gemini")
print(history)
history.pop()
print(history)



#queue
print("-----------Queue------------")
#fifo 
from collections import deque

queue = deque()

#enqueue
queue.append("A")
queue.append("B")
queue.append("C")
print(queue)

#dequeue
served_cus = queue.popleft()
print(served_cus)


#deque -> double ended queue


#heap
print("-----------Heap Basics----------------")
#heap is a speacialised tree like structure, and python provide minheap using heapq module
import heapq

numbers = [30,10,50,20,40]
heapq.heapify(numbers)
print(numbers)