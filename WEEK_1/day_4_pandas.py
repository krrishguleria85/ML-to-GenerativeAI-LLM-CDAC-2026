#PANDAS
#data life cycle architecture: data ingestion(fetch the data using built in data and in kaggle) -> data inspection -> cleaning -> analysis -> output
# the whole above data cycle is the data preprocessing and it is the input for machine learning models to use it and learn from it to give user insights

#df.head, tail -> show first 5 data of the data frame
#data.describe() -> shows statistical summary of numerical columns
#data.info() -> shows the index, name, memory locations

#web scraping , b and w box

import pandas as pd
import numpy as np

print("Pandas version: ",pd.__version__)

print("Pandas Imported successfully!!")
print(" ")

#series
print("=================")
students = pd.Series(["Riya","Rahul","Rohan"])
print(students)

marks=pd.Series([85,90,78,95])
print(marks)


print("=================")
print("Creating the dataframes-->")
print(" ")

students_df=pd.DataFrame({
  "Name":["Rahul","Aman","Riya","Krrish","Aman Verma", "Ayush Patial","Sehaj Kaur","Tarushi Bahl","Ayachi","Pranav"],
  "Age":[21,22,20,20,21,22,22,21,20,21],
  "Marks":[85,90,95,95,85,80,75,58,98,84]
})
print(students_df)
print(" ")

print("1. D types: ", students_df.dtypes)
print("2. Shape of data frame: ",students_df.shape)
print("3. Columns: ", students_df.columns)
print("4. Index: ", students_df.index)
print(" ")

print("head-->")
print("1.head: ",students_df.head(8))
print("2. tail :", students_df.tail(8))


print("-----------")
print("3. shape: ", students_df.shape) #tells the rows and columns of data
print(" ")

print("-----------")
print("4. info function: ", students_df.info)
print(" ")

print("-----------")
print("5. selecting multiple columns")
print(students_df[["Name","Marks"]])
print(" ")

print("------------")
print("6. selecting rows using loc")
print(" ")
print(students_df.loc[0])
print(" ")
print(students_df.loc[1])
print(" ")
print(students_df.loc[:,["Name","Marks"]])
print(" ")
print(students_df.loc[0:1])
print(" ")
print(students_df.loc[0:2, ["Name"]])
print(" ")

print("------------")
print("7. selecting rows using iloc")
print(" ")
print(students_df.iloc[0])
print(" ")
print(students_df.iloc[1])
print(" ")
print(students_df.iloc[:, 0])
print(" ")
print(students_df.iloc[:,1])
print(" ")
print(students_df.iloc[0:2])
print(" ")
print(students_df.iloc[0:2, 0:2])
print(" ")

print("------------")
print("8. Value Counts")
country_series = pd.Series([
  "India","India","USA","India","UK","USA"
])
print(country_series.value_counts())
print(country_series.value_counts().sort_index())
print(" ")

print("------------")
print("9. Unique Values")
cities = pd.Series([
  "Mohali","Delhi","Mohali","Chandigarh"
])
print(cities)
print(cities.unique())
print(cities.nunique())
print(" ")


print("------------")
print("10. handling of missing values")
df = pd.DataFrame({
  "Name": ["Rahul","Aman",None,"Riya"],
  "Marks":[85,np.nan,90,95]
})
print(df)
print(" ")
print(pd.isnull(df))
print(" ")
print(pd.notnull(df))
print(" ")


print("------------Ctd to 10.--")
print("11. DROP NA()")
print(df.dropna())
print(" ")
#-> drop columns having null values
print(df.dropna(axis=1))
print(" ")


print("------------")
print("12. FILL NA()")
print(df.fillna("Unknown"))
print(df["Marks"].fillna(df["Marks"].mean()))
df["Marks"]=df["Marks"].fillna(df["Marks"].mean())
print(" ")
print(df)
print(" ")


print("------------")
print("13. Renaming columns")

df = pd.DataFrame({
    "Student_name": ["Rahul", "Aman", "Rohan"],
    "Student_Marks": [85, 75, 62]
})
print(df)

df = df.rename(columns={
    "Student_name": "Name",
    "Student_Marks": "Marks"
})
print(df)
print(" ")


print("------------")
print("14. set index")
stu=pd.DataFrame({
  "roll":[101,102,103],
  "Name":["Rahul","Aman","Mohit"]
})
print(stu)

stu_d=stu.set_index("roll")
print(stu_d)
print(" ")


print("------------")
print("15. GroupBY()")
stu_details=pd.DataFrame({
  "Course":[
    "Python",
    "Python",
    "AI",
    "AI",
    "ML"
  ],
  "Marks":[
    85,
    90,
    95,
    80,
    88
  ]
})
print("\n",stu_details)
print(stu_details.groupby("Course")["Marks"].mean())
print("")
print(stu_details.groupby("Course")["Marks"].max())
print(" ")



print("------------")
print("16. Correlation")
data = pd.DataFrame({
  "Study_hrs":[1,2,3,4,5],
  "Marks":[40,55,70,85,95]
})
print("")
print(data)
print("")
print(data.corr())
print(" ")


print("===============================")
import matplotlib.pyplot as plt
#matplotlib is a library and contains various modules which includes pyplot as a library


print("------------")
print("17. Histogram")
marks=pd.Series([
  85,90,95,78,88,92,75
])
print(marks)
marks.plot.hist()
plt.show()
print("")


print("------------")
print("18. Bar plot")
courses=pd.Series({
  "Python":50,
  "AI":40,
  "ML":30
})
print(courses)
courses.plot.bar()
plt.show()
print(" ")



