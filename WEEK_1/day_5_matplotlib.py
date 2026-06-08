#MATPLOTLIB
#it includes various plots to visualise the data like seaborn, heatmap etc...


import matplotlib.pyplot as plt
import numpy as np

print("------------")
print("Matplotlib Imported successfully!!")


print("------------")
print("1. Basic line plot")
x = [1,2,3,4,5]
y = [10,20,30,40,50]
plt.plot(x,y)
plt.show()
print("Line plot shown success!!")
print(" ")
#print("Line chart Example: ")
#subjects=["Compiler","ML","AI","EWM"]
#marks=[85,95,75,85,25]
#plt.plot([subjects,marks])
#plt.show()
#print(" ")


print("------------")
print("2. Multiple line plots: ")
x = [1,2,3,4,5]
y1 =[20,40,60,80,100]
y2=[30,50,70,90,110]
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()
print("Multiple Line plot shown success!!")
print(" ")



print("------------")
print("3. Customised line plot: ")
x= [10,20,30,40,50]
y=[15,25,35,45,55]
plt.plot(
  x,y,color="blue",linestyle="--"
)
plt.show()
print("Customised Line plot success!!")
print(" ")



print("------------")
print("4. Scatter Plot: ")
x=[15,35,55,75,95]
y=[5,25,35,55,75]
plt.scatter(x,y)
plt.show()
print("Scatter Plot success!!")
print(" ")
study_hour=[1,2,3,4,5]
marks=[55,75,85,45,95]
plt.scatter(study_hour, marks)
plt.show()
print(" ")



print("------------")
print("5. Customised Scatter Plot: ")
x=[10,20,30,40,50]
y=[25,45,65,85,105]
plt.scatter(
  x,y,c="red",s=100
)
plt.show()
print("Customised Scatter plot success!")
print(" ")


print("------------")
print("6. Bar Chart: ")
courses=["Python","AI","ML","DT"]
boys=[50,40,30,25]
girls=[40,20,15,15]
plt.bar(courses, boys)
plt.bar(
  courses, girls, bottom=boys
)
plt.show()
print("Bar Chart Success!!")
print(" ")



print("------------")
print("7. Histogram: ")
marks=[
  85,90,88,94,72,
  60,70,75,80,95,
  84,78,90,87,82
]
plt.hist(marks)
plt.show()
print("Histogram Success!!")
print(" ")

scores=np.random.randint(40,100,100)
plt.hist(scores)
plt.show()
print(" ")



print("------------")
print("8. Customised Histogram: ")
data=np.random.randn(1000)
plt.hist(data,bins=30,color="orange")
plt.show()
print(" ")



print("------------")
print("9. Area Plot: ")
x=[1,2,3,4,5]
lower=[10,20,30,40,50]
upper=[15,25,35,45,55]
plt.fill_between(x,y1=lower, y2=upper)
plt.show()



print("------------")
print("10. Pie Chart:  ")
sizes=[25,45,65,55,85,95]
labels=["Python","AI","ML","FLAT","Compiler","C++"]
plt.pie(sizes,labels=labels, autopct="%1.1f%%")
plt.show()
print(" ")


#go to google colab for visualising!!!!!