import threading
import yaml
from gradegrabber import *
from assignmentgrabber import *
from yaml.loader import *


with open('fsaconnect/testconfig.yaml', 'r') as f:
    data = yaml.load(f, Loader=SafeLoader)
    fcdata = data['FSACONNECT']
    username = fcdata['Username']
    password = fcdata['Password']

#constantly check for grade updates
def gradeUpdater():
    threading.Timer(15.0, gradeUpdater).start()
    grades = pullGrades(username, password)
    print(grades)

def assignmentUpdater():
    threading.Timer(15.0, gradeUpdater).start()
    upcoming = pullAssignments(username, password)
    print(upcoming)

while True:
    gradeUpdater()
    assignmentUpdater()
