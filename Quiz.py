from QuestionDB import QuestionDB
import random

class Quiz:
    totalPlayers=0
    average=0
    def __init__(self):
        self.QDB=QuestionDB()
        Quiz.totalPlayers+=1
        self.makeQuiz()
        self.takeQuiz()
        self.printScore()
    def makeQuiz(self): #randomly selects 5 questions for the question database
        count=0
        self.selectedQuestionsList=[]
        while True:
            n=random.choice(self.QDB.questionList)
            if n not in self.selectedQuestionsList:
                self.selectedQuestionsList.append(n)
                count+=1
            if count==5:
                break
    def takeQuiz(self):
        count=1
        self.score=0
        for question in  self.selectedQuestionsList:
            print('Question #',count,':',end='')
            question.printQuestion()
            answer=input('Enter answer (a, b or c): ')
            if question.checkAnswer(answer):
                self.score+=1
            count+=1
        Quiz.average=Quiz.average+self.score/2
    def printScore(self):
        print('\n')
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('Your score is:',self.score)
        if self.score==5:
            print('WOW...YOU KMOW IT ALL...WELL DONE!!!')
        elif self.score>Quiz.average:
            print ('Your performance was above average!!')
        elif self.score<Quiz.average:
            print ('You need to improve your GK')
        else:
            print('Your performance was average')
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    def printQuestionList(self): #prints selested question list
        ID=1
        for question in self.selectedQuestionsList:
            print('QID:',ID)
            question.printQuestionWithAnswer()
            ID+=1        

##a=Quiz()
##a.makeQuiz()
##a.takeQuiz()
##a.printScore()
