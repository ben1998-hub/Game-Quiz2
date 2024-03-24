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
def check_answer(answers, correct, response):
   
    """
    Function with if else statment to check
    if answer is correct or not according to the indexes

    """

    global score
    global q_num

    clear()

    pickedindex = indexes.index(response)
    correctindex = answers.index(correct)

    if pickedindex == correctindex:
        clear()
        print("Correct!")
        score += 1
    else:
        print("Answer was incorrect")

    input("Press enter to continue\n")

    q_num += 1

    completed_question = qq.pop(0)
    finished.append(completed_question)


def give_question(ques):


    """
    prints current score.
    it shuffles the answers randomly with random module
    checks if user has put in correct letter
    if not print choice of correct answers(indexes)
    user input but pressing enter take user to next question
    """
    global score  # for score to work globally throughout the code
    clear()

    print(f'Score: {score}\n')

    print(f'Question {q_num + 1}')

    question = ques["question"]

    answers = ques["answer"]
    random.shuffle(answers)

    correct = ques["correct_answer"]

    print(question)

