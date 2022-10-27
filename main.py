USER_PATH = "CHANGE ME TO THE LOCATION OF YOUR PROJECT FOLDER" #example: USER_PATH = "C:/Users/14704/Desktop/fsaconnect/fsaconnect"
import sys
sys.path.append("{}/src/main".format(USER_PATH))
sys.path.append("{}/src/notion".format(USER_PATH))
sys.path.append("{}/src/discord".format(USER_PATH))
sys.path.append("{}/src/discord".format(USER_PATH))
sys.path.append("{}".format(USER_PATH))
import sys
import threading
import yaml
import sys
from gradegrabber import *
from assignmentgrabber import *
from yaml.loader import *
from barGraph import *


with open('C:/Users/14704/Desktop/fsaconnect/fsaconnect/testconfig.yaml', 'r') as f:
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
    

