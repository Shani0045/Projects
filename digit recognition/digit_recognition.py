from tkinter import*
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from tkinter import messagebox
# from sklearn.feature_extraction.text import TfidfVectorizer
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageTk


root=Tk()
root.title("Digit recognition")
root.geometry("830x730")


f=Frame(root,relief=RIDGE,bd=6,bg='steel blue')
f.place(x=0,y=0,width=830,height=130)
l=Label(f,text='Digit Recognition System',font=("ariel",40,'bold'),fg='white',bg='steel blue')
l.place(x=110,y=25)


# load=Image.open("digit.png")
# res=load.resize((820,725))
# img=ImageTk.PhotoImage(res)
# label6=Label(f,image=img,bg="black")
# label6.place(x=0,y=0)

#main frame in center
frame=Frame(root,relief=GROOVE,bd=5,bg='steel blue')
frame.place(x=0,y=131,width=830,height=470)

# image frame
frame1=Frame(frame,relief=GROOVE,bd=2)
frame1.place(x=200,y=4,width=430,height=330)

#button frame

frame2=Frame(frame,relief=GROOVE,bd=3,bg='steel blue')
frame2.pack(side=BOTTOM)


#below frame
frame3=Frame(root,relief=GROOVE,bd=5,bg='steel blue')
frame3.place(x=0,y=600,width=830,height=125)

# l=Label(frame,text='Image ',font=("ariel",22,'bold'),fg='white',bg='steel blue')
# l.place(x=50,y=30)
try:
    image=[]
    def upload():
        image.clear()
        file=askopenfilename()
        load=Image.open(file)
        res=load.resize((430,330))
        img=ImageTk.PhotoImage(res)
        label5.config(image=img)
        label5.image=img
        image.append(file)
        
    def clear():
        label5.config(image=None)
        label5.image=None
        la.config(text=" ")
        
        
    def predict():
        a=image[0]
        model=load_model("mnist_cnn.h5")
        img=cv2.imread(a,0)
        img=cv2.resize(img,(28,28))
        img_res=img.reshape(-1,28,28,1)
        img=img_res.astype("float32")
        img_new=img_res/255.0
        s=model.predict_classes(img_new)[0]
        la.config(text=f"Predicted output of the image is : {s}",font=("ariel",25,'bold'),fg="white",bg="steel blue")
        
    def exit():
        if messagebox.askyesno("ask","do you want to quit?"):
            root.destroy()
except:
    messagebox.show("error","there is something wrong")
        
la=Label(frame3,bg="steel blue")
la.place(x=130,y=20)
    
label5=Label(frame1)
label5.place(x=0,y=0)
    
btn0=Button(frame,text="Upload Image Here",font=("ariel",14),command=upload)
btn0.place(x=300,y=340)

btn1=Button(frame2,text="Predict",font=("ariel",20),width=10,command=predict)
btn1.pack(side=LEFT)

btn2=Button(frame2,text="Clear",font=("ariel",20),width=10,command=clear)
btn2.pack(side=LEFT,padx=10)

btn3=Button(frame2,text="Exit",font=("ariel",20),width=10,command=exit)
btn3.pack(side=LEFT)


# var=StringVar()
# m=Message(frame1)
# m.place(x=0,y=0,width=400,height=300)

root.mainloop()
