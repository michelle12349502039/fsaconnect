import os
import getpass
import re
from re import search
from requests import Session
from bs4 import BeautifulSoup as bs
from string import digits

from soupsieve import select


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
        


          



