
import yaml
import threading
import sys

# example: USER_PATH = "C:/Users/14704/Desktop/fsaconnect/fsaconnect"
USER_PATH = "C:/Users/14704\Desktop/fsa connect/fsaconnect/"
sys.path.append("{}/src/main".format(USER_PATH))
sys.path.append("{}/src/notion".format(USER_PATH))
sys.path.append("{}/src/discord".format(USER_PATH))
sys.path.append("{}/src/discord".format(USER_PATH))
sys.path.append("{}".format(USER_PATH))
from grabber import *

with open('C:/Users/14704\Desktop/fsa connect/fsaconnect/testconfig.yaml', 'r') as f:
    data = yaml.load(f, Loader=yaml.SafeLoader)
    fcdata = data['FSACONNECT']
    username = fcdata['Username']
    password = fcdata['Password']


# constantly check for grade updates
def updater():
    threading.Timer(15.0, updater).start()
    grades = pullGrades(username, password)
    print(grades)
    upcoming = pullAssignments(username, password)
    print(upcoming)


while True:
    barGraph(username, password)
    updater()
    
