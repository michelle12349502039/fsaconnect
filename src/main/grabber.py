import os
import getpass
import re
from re import search
from requests import Session
from bs4 import BeautifulSoup as bs
from string import digits
import numpy as np
import matplotlib.pyplot as plt
from soupsieve import select




def pullGrades(username: str, password: str) -> dict:
    """
      Pull the grades for the given username and password.

      :param username: username of user to pull from
      :param password: password of user to pull from
      :return: dictionary of grades where the key is string course and the value is float grade
      """

    # print("logging in..")
    with Session() as s:
        site = s.get("https://fultonscienceacademy.radixlms.com/login/")
        bs_content = bs(site.content, "html.parser")
        token = bs_content.find("input", {"name": "logintoken"})["value"]
        login_data = {
            "username": username,
            "password": password,
            "logintoken": token,
            "anchor": ""
        }
        s.post("https://fultonscienceacademy.radixlms.com/login/index.php",
               login_data)
        grade_page = s.get(
            "https://fultonscienceacademy.radixlms.com/grade/report/overview/")
        grade_content = bs(grade_page.content, "html.parser")
        grades = grade_content.find_all("tr",
                                        id=lambda x: x and x.startswith('grade-'))

    # print("grabbing grades")

    gradesDict = {}

    for i in grades:
        if search("%", i.text.strip()):
            text = i.text.strip()

            in1 = (text.rfind("(") + 1)
            in2 = (text.rfind(")") - 3)

            if text[text.rfind("(") + 1:text.rfind(")") - 3].isnumeric() or search(
                    ".", text[text.rfind("(") + 1:text.rfind(")") - 3]):
                substring = text[in1:in2]

                gradesDict[text.translate({ord(k): None
                                           for k in digits}).replace("(", "").replace(
                    ".", "").replace("%", "").replace(
                                               ")", "").replace("  ",
                                                                "")] = float(substring)
    return gradesDict


# creating the dataset
def barGraph(usern, passw):
  data = pullGrades(usern, passw)
  courses = list(data.keys())
  values = list(data.values())
  fig = plt.figure(figsize = (16, 5))
# creating the bar plot
  plt.bar(courses, values, color ='maroon',
        width = 0.4)
  plt.xlabel("Courses")
  plt.ylabel("Grade")
  plt.title(usern)
  plt.savefig('graph.png')




def pullAssignments(username, password) -> dict:

    with Session() as s:
        site = s.get("https://fultonscienceacademy.radixlms.com/login/")
        bs_content = bs(site.content, "html.parser")
        token = bs_content.find("input", {"name": "logintoken"})["value"]
        login_data = {"username": username, "password": password,
                      "logintoken": token, "anchor": ""}
        s.post("https://fultonscienceacademy.radixlms.com/login/index.php", login_data)
        assignment_page = s.get(
            "https://fultonscienceacademy.radixlms.com/blocks/radix_dashboard/upcomingassignments.php")
        assignment_content = bs(assignment_page.content, "html.parser")
        name = assignment_content.find_all("a", href=lambda href: href and "mod/assign" in href)
        duedate = assignment_content.find_all(lambda tag: 'data-text' in tag.attrs)
        nameList=[]
        dateList=[]
        for i in name:
          nameList.append(i.text.strip())
        for i in duedate:
          dateList.append(i.text.strip())
        assignmentList=dict(zip(nameList, dateList))
        return assignmentList
        

  

