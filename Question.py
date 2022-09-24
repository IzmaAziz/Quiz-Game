class Question:
    def __init__(self):
        self.question=[None,[],None]
    def setQuestion(self,qs):
        self.question[0]=qs
    def setOptions(self,op1,op2,op3):
        self.question[1].append(op1)
        self.question[1].append(op2)
        self.question[1].append(op3)
    def setAnswer(self,n): #enter 1, 2, or 3
        self.question[2]=n #setting index number of correct option
    def printQuestion(self):
        print(self.question[0])
        print('a.',self.question[1][0])
        print('b.',self.question[1][1])
        print('c.',self.question[1][2])
    def printCorrectAnswer(self):
        print('Correct answer is',self.question[2])
    def printQuestionWithAnswer(self):
        print(self.question[0])
        print('a.',self.question[1][0])
        print('b.',self.question[1][1])
        print('c.',self.question[1][2])
        print('Correct answer is',self.question[1][self.question[2]-1])
    def checkAnswer(self, ans):
        key={'a':1,'b':2,'c':3}
        if self.question[2]==key[ans]:
            return True
        return False
    def __str__(self):
        return str(self.question)

##q1=Question()
##q1.setQuestion('Which of the following is not a programming language?')
##q1.setOptions('Ruby', 'Python','Linux')
##q1.setAnswer(3)
##q1.printQuestion()
##answer=input('Enter answer:')
##print(q1.checkAnswer(answer))
