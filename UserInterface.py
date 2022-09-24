from QuestionDB import QuestionDB
from Quiz import Quiz
import sys

class UserInterface:
    def __init__(self):
        while True:
            UserInterface.displayMainMenu()
            choice=input('Enter option number:')
            if choice=='1':
                UserInterface.editQuiz()
            elif choice=='2':
                Quiz()
            else:
                break

    def displayMainMenu():
        print('\n')
        print('***************************')
        print('1. Edit question database')
        print('2. Take quiz')
        print('Press anyother key to exit')
        print('***************************')

    def displayEditMenu():
        print('\n')
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print('1. List questions')
        print('2. Add question')
        print('3. Remove question')
        print('4. Save changes')
        print('5. Go back to the main menu')
        print('Press any other key to exit')
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

    def editQuiz():
        QDB=QuestionDB()
        while True:
            UserInterface.displayEditMenu()
            choice=input('Enter option number:')
            if choice=='1':
                QDB.printQuestionList()
            elif choice=='2':
                QDB.addQuestion()
            elif choice=='3':
                QDB.removeQuestion()
            elif choice=='4':
                QDB.saveQuestionList()
                print('Changes Saved successfully!!')
            elif choice=='5':
                break
            else:
                sys.exit()



    


            
