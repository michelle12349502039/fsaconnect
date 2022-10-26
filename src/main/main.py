import threading
import yaml
from grabber import *
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


while True:
    gradeUpdater()
