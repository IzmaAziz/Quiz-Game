from Question import Question
    
class QuestionDB:
    def __init__(self):
        self.loadQuestionList()
    def addQuestion(self):
        q=Question()
        x=input('\nEnter question:')
        q.setQuestion(x)
        x1=input('Enter option 1:')
        x2=input('Enter option 2:')
        x3=input('Enter option 3:')
        q.setOptions(x1,x2,x3)
        while True:
            try:
                x=int(input('Enter answer:(1,2 or 3)'))
                if 0>x>3:
                    raise ValueError 
            except ValueError:
                print('Enter a valid option number!')
            else:
                q.setAnswer(x)
                self.questionList.append(q)
                break
    def removeQuestion(self):
        try:
            ID=int(input('Enter QID to be removed:'))
            if ID>len(self.questionList):
                raise ValueError
        except ValueError:
            print('Invalid QID!!')
            return
        self.questionList.pop(int(ID)-1)
    def saveQuestionList(self):
        f=open('QuestionsDB.txt','w')
        for question in self.questionList:
            f.write(str(question)+'\n')
        f.close()
    def loadQuestionList(self):
        self.questionList=[]
        try:
            f=open('QuestionsDB.txt','r')
        except:
            return
        for line in f:
            question=eval(line)
            q=Question()
            q.setQuestion(question[0])
            q.setOptions(question[1][0],question[1][1],question[1][2])
            q.setAnswer(question[2])
            self.questionList.append(q)
        f.close()
    def printQuestionList(self):
        ID=1
        for question in self.questionList:
            print('QID:',ID)
            question.printQuestionWithAnswer()
            ID+=1
                
##a=QuestionDB()
####a.addQuestion()
####a.saveQuestionList()
####a.loadQuestionList()
##a.printQuestionList()
##a.removeQuestion()
##a.printQuestionList()
            
