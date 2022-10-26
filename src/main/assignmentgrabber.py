import os
import getpass
import re
from re import search
from requests import Session
from bs4 import BeautifulSoup as bs
from string import digits


def pullAssignments() -> dict:

    with Session() as s:
        assignment_page = s.get(
            "https://fultonscienceacademy.radixlms.com/blocks/radix_dashboard/upcomingassignments.php")
        assignment_content = bs(assignment_page.content, "html.parser")
        assignments = assignment_content.find_all("tr")
