import os
import getpass
import re
from re import search
from requests import Session
from bs4 import BeautifulSoup as bs
from string import digits

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
        token = bs_content.find("input", {"name":"logintoken"})["value"]
        login_data = {"username":username,"password":password, "logintoken":token,"anchor":""}
        s.post("https://fultonscienceacademy.radixlms.com/login/index.php",login_data)
        grade_page = s.get("https://fultonscienceacademy.radixlms.com/grade/report/overview/")
        grade_content = bs(grade_page.content, "html.parser")
        grades = grade_content.find_all("tr", id=lambda x: x and x.startswith('grade-'))

    # print("grabbing grades")

    gradesDict = {}

    for i in grades:
        if search("%", i.text.strip()):
            text = i.text.strip()
        
            in1 = (text.rfind("(") +1)
            in2 = (text.rfind(")")-3)

            if text[text.rfind("(")+1:text.rfind(")")-3].isnumeric() or search(".", text[text.rfind("(")+1:text.rfind(")")-3]):
                substring = text[in1:in2]

                gradesDict[text.translate({ord(k): None for k in digits}).replace("(", "").replace(".", "").replace("%","").replace(")","").replace("  ", ": ")] = float(substring)
    return gradesDict
            
    

          
