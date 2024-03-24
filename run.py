from os import system, name  # import of os module
import random  # for the use of randomising answers.
from questions import questions # importing the questions from questions.py file for declutter.

qq = questions
finished = []


# indexes the questions from the questions file.
total = len(qq)
indexes = ['A', 'B', 'C', 'D']
score = 0 
q_num = 0
def clear():
    """
    function to clear 
    """
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

