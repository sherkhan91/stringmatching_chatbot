from tkinter import *

root = Tk()
root.geometry("500x600")
root.title("SOCRAI chatbot")
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

global stored_score


question_list=[]
# questions
d1 = 'Who is the founder of Pakistan?\n'
d2 = 'what is the complete name of Pakistan?\n'
d3 = 'what do giraffes eat?\n'
question_list.append(d1)
question_list.append(d2)
question_list.append(d3)

answer_list=[]
#Answers
a1='quaid e azam muhammad ali jinnah'
a2='islamic republic of pakistan'
a3='grass'

answer_list.append(a1)
answer_list.append(a2)
answer_list.append(a3)


label = Label(root,text= "Welcome to SOCRAI question answer chatbot", relief=RAISED, font="Times 16 bold")
label.pack(padx=100,pady=100)

text = StringVar()
text.set("Who is the founder of Pakistan ?")
question_label = Label(root,textvariable=text,font="Times 16 bold" )
question_label.pack()

answer_space = Entry(root, width="50")
answer_space.pack()
answer_space.insert(0,"")
answer_space.focus_set()

question_iter = iter(question_list)
answer_iter = iter(answer_list)


def jaccard_similarity(s1, s2):
    return len(s1.intersection(s2)) / len(s1.union(s2))

score_list = []

next_question = next(question_iter)
text.set(next_question)

def submitBtn():

    answer_by_user = answer_space.get()
    # print("answer space",answer_by_user)
    user_answer = answer_by_user
    try:
        actual_answer = next(answer_iter)
        print("user answer: ", user_answer)
        print("actual answer: ", actual_answer)
        s1 = pre_process(user_answer)
        s2 = pre_process(actual_answer)
        s1 = set(s1)
        s2 = set(s2)
        a = jaccard_similarity(s1, s2)
        print(int(round(a * 100)))
        score_list.append(int(round(a * 100)))
        answer_space.delete(0, END)
    except:
        pass


    try:
        next_question = next(question_iter)
        text.set(next_question)
    except:
        text.set("No more question")
        final_score = 0
        for x in score_list:
            final_score+=x
        final_score = final_score/(len(question_list)+1)
        final_score_label = Label(root,text= "Accumulative Score: "+str(final_score),font="times 22 bold")
        final_score_label.pack()
        print("hey endddd")
        button.configure(state='disabled')
        if final_score < 60:
            level_report= Label(root, text="Sorry,you are fail please try again to pass the level" , font="times 22 bold")
            level_report.pack()
        else:
            level_report = Label(root, text='Congrats,you are passed and now promoted to level 2', font="times 22 bold")
            level_report.pack()



button =  Button(root,text="Submit", command=submitBtn,font="Times 16 bold")
button.pack()

close_button = Button(root, text="Close", command=quit,font="Times 16 bold")
close_button.pack()




root.mainloop()