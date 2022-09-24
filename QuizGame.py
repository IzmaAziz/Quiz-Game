


#for setting absolute path; QuestionDB module is placed in a sub-folder ‘Quiz Game’
#sys.path.append('C:/Users/maria/AppData/Local/Programs/Python/Python37-32/Quiz Game')
#for setting relative path; QuestionDB module is placed in a sub-folder ‘Quiz Game’

from QuestionDB import QuestionDB
import random
from tkinter import Tk,Label,Button,Radiobutton,Frame,IntVar,StringVar

class GUIQG(Tk):
    
    def __init__(self):
        #setting GUI window        
        super().__init__()
        self.title('Quiz Game')
        self.minsize(550,150)
        
        #making and displaying quiz
        #loading question bank into QBD using QuestionDB class
        self.QDB=QuestionDB()
        #not using Quiz class as it was customized to print output on the shell
        #following methods are redefined in this current class
        #makeQuiz randomly selects 10 questions and
        #place them in the instance variable selectedQuestionsList
        self.makeQuiz()
        #displayQuiz displays the selected questions using GUI
        self.displayQuiz()

        #setting up event listener 
        self.mainloop()

    def displayQuiz(self):
        self.wrongAns=[]
        self.score=0
        for i in range(10):
            #creating frame for one question at a time
            self.createFrame(self.selectedQuestionsList[i],i)#i is the question index
                    
    def createFrame(self,q,i):
        def nextClicked():
            
            if q.checkAnswer(radioSelection.get()):
                self.score+=1
            else:
                self.wrongAns.append(q)
                
            f.destroy()
            wait.set(1)
        def finishClicked():
            nextClicked()
            lResult=Label(self,text='You scored '+str(self.score)+' out of 10')
            lResult.pack()
            for i in self.wrongAns:
               question=i.question[0]
               option=i.question[2]
               answer=i.question[1][option-1]
               lquestion=Label(self,text=str(question)+' Correct answer:'+str(answer))
               lquestion.pack()
                
        f=Frame(self)
        #placing question in a label       
        lQuestion=Label(f,text=q.question[0])
        lQuestion.pack()
        #placing three radio buttons for the options
        radioSelection=StringVar(f,' ') #catches the selection
        rb1=Radiobutton(f,text=q.question[1][0],variable=radioSelection, value='a', )
        rb1.pack()
        rb2=Radiobutton(f,text=q.question[1][1],variable=radioSelection, value='b')
        rb2.pack()
        rb3=Radiobutton(f,text=q.question[1][2],variable=radioSelection, value='c')
        rb3.pack()
        #placing the 'Next' button for first 9 question and 'Finish' for the last one
        if i<9:
            button=Button(f,text='Next',command=nextClicked)
        else:
            button=Button(f,text='Finish',command=finishClicked)

        button.pack()
        f.pack()
        #making the GUI/frame wait for the next button click
        wait=IntVar()
        wait.set(0)
        button.wait_variable(wait)
        
    def makeQuiz(self): #randomly selects 10 questions from the question database
        count=0
        self.selectedQuestionsList=[]
        while True:
            n=random.choice(self.QDB.questionList)
            if n not in self.selectedQuestionsList:
                self.selectedQuestionsList.append(n)
                count+=1
            if count==10:
                break
            
GUIQG()

    


            
