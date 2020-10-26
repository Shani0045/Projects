from tkinter import*
import pandas as pd
import numpy as np
from tkinter import ttk
from sklearn.feature_extraction.text import TfidfVectorizer
from tkinter import messagebox
from PIL import Image,ImageTk
from nltk.tokenize import RegexpTokenizer

from tensorflow.keras.models import load_model
from sklearn.externals import joblib

tfidf=joblib.load("tfidf.pkl")
model=load_model("email.h5")

rt=RegexpTokenizer('\w+')
def cleanText(s):
    w=rt.tokenize(s)
    return ' '.join(w)


root=Tk()
root.geometry("850x730")

def predict():
    text1=text.get('1.0','end-1c')
    t1=cleanText(text1)
    test=np.array(tfidf.transform([t1]).toarray())
    result=model.predict_classes(test)
    s=pd.Series(result.flatten())
    pr=s.map({0:"Ham",1:"Spam"})
    var.set(f'Message will be {pr[0]}')
def clear():
    text.delete('1.0',END)
    var.set('')
    

f=Frame(root,relief=RIDGE,bd=6,bg='steel blue')
f.place(x=0,y=0,width=850,height=130)
l=Label(f,text='Email Message Classification',font=("Times",40,'bold'),fg='white',bg='steel blue')
l.place(x=150,y=15)

load=Image.open("email.png")
res=load.resize((110,110))
img=ImageTk.PhotoImage(res)
label5=Label(f,image=img,bg='steel blue')
label5.place(x=30,y=3)

frame=Frame(root,relief=GROOVE,bd=5,bg='steel blue')
frame.place(x=0,y=131,width=850,height=460)

l=Label(frame,text='Type Message',font=("ariel",22,'bold'),fg='white',bg='steel blue')
l.place(x=30,y=30)

text=Text(frame,font=("ariel",16),fg='black',bg='white',relief=GROOVE,bd=2)
text.place(x=260,y=30,width=550,height=300)

btn1=Button(frame,text="Predict",font=("ariel",17),command=predict)
btn1.place(x=260,y=350)

btn2=Button(frame,text="Clear",font=("ariel",17),width=7,command=clear)
btn2.place(x=400,y=350)

btn3=Button(frame,text="Exit",font=("ariel",17),width=6)
btn3.place(x=540,y=350)

frame1=Frame(root,relief=GROOVE,bd=5,bg='steel blue')
frame1.place(x=0,y=591,width=850,height=135)
# l1=Label(frame1)
# l1.place(x=60,y=20)
var=StringVar()
m=Message(frame1,font=('ariel',25,'bold'),textvariable=var,width=800,bg='steel blue',fg='white')
m.place(x=2,y=1,width=815,height=120)

root.mainloop()
