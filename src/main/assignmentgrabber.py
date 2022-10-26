import os
import getpass
import re
from re import search
from requests import Session
from bs4 import BeautifulSoup as bs
from string import digits


def pullAssignments(username, password) -> dict:

    with Session() as s:
        site = s.get("https://fultonscienceacademy.radixlms.com/login/")
        bs_content = bs(site.content, "html.parser")
        token = bs_content.find("input", {"name":"logintoken"})["value"]
        login_data = {"username":username,"password":password, "logintoken":token,"anchor":""}
        s.post("https://fultonscienceacademy.radixlms.com/login/index.php",login_data)
        assignment_page = s.get(
      "https://fultonscienceacademy.radixlms.com/blocks/radix_dashboard/upcomingassignments.php")
        assignment_content = bs(assignment_page.content, "html.parser")
        assignments = assignment_content.find_all("td",{"class": "col-md-2"})
        return(assignments)
