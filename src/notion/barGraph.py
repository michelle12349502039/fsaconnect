import gradegrabber
import numpy as np
import matplotlib.pyplot as plt


# creating the dataset
def barGraph(usern, passw):
  data = gradegrabber.pullGrades(usern, passw)
  courses = list(data.keys())
  values = list(data.values())
  fig = plt.figure(figsize = (16, 5))
# creating the bar plot
  plt.bar(courses, values, color ='maroon',
        width = 0.4)
  plt.xlabel("Courses")
  plt.ylabel("Grade")
  plt.title(usern)
  plt.show()