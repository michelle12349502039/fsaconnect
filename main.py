import threading
import yaml
import sys
sys.path.append("./")
sys.path.append("./src/main")
sys.path.append("./src/notion")
sys.path.append("./src/discord")
from gradegrabber import *
from assignmentgrabber import *
from yaml.loader import *
from barGraph import *


with open('testconfig.yaml', 'r') as f:
    data = yaml.load(f, Loader=SafeLoader)
    fcdata = data['FSACONNECT']
    username = fcdata['Username']
    password = fcdata['Password']
    

#constantly check for grade updates
def updater():
    threading.Timer(15.0, updater).start()
    grades = pullGrades(username, password)
    print(grades)
    upcoming = pullAssignments(username, password)
    print(upcoming)

while True:
    updater()
    barGraph(username, password)
    

