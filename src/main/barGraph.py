import gradegrabber
import numpy as np
import matplotlib.pyplot as plt
 
username = "mk0207.fsa"
password = "Mk020772"

# creating the dataset
data = gradegrabber.pullGrades(username, password)
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (16, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='maroon',
        width = 0.4)
 
plt.xlabel("Courses")
plt.ylabel("Grade")
plt.title(username)
plt.show()