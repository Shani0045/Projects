import cv2 
from tkinter import*
from tkinter import ttk
import os
from tkinter import messagebox
from tkinter.filedialog import askdirectory,askopenfile
root=Tk()
root.title("Shani")
root.config(bg="powder blue")
root.geometry("900x670")
root.resizable(0,0)

#f=Frame(root,bd=15,relief=RIDGE,pady=5,bg="powder blue")
#f.pack(side=TOP)

label=Label(root,text="Image Extraction Tool",font=("helvetica",35,"bold"),fg="black",bg="powder blue",justify=CENTER)
label.pack()

x=StringVar()
varb1=IntVar()
varb2=IntVar()
var2=IntVar()
var3=StringVar()
def opens():
    file=askdirectory()
    x.set(f"{file}/")
def opens1():
    file=askdirectory()
    var3.set(f"{file}/")

def show1():
    file1=askopenfile()
    
    

def show():
    try:
        v,v=varb1.get(),varb2.get()
        a=x.get()
        x.set("")
        v2=var2.get()
        var2.set("")
        v3=var3.get()
        var3.set("")
        imgs=os.listdir(a)
        clf=cv2.CascadeClassifier('f:/opencv/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')    
        for img in imgs:
            gray=cv2.imread(a +img,v)
            faces=clf.detectMultiScale(gray)
            if(len(faces)==v2):
                cv2.imwrite(f"{v3}{img}",gray)
            
        messagebox.showinfo("Info","Image Successfully Extract ")
    
            
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        messagebox.showerror("Error","There is a Error in Path")
    
l1=Label(root,text="SOURCE",font=("helvetica",23,"bold"),fg="black",bg="powder blue")
l1.place(x=80,y=130)

e1=Entry(root,textvariable=x,font=("helvetica",19),bd=4,width=25)

e1.place(x=270,y=130)

bt=Button(root,text="open",font=("helvitica",14),command=opens)
bt.place(x=635,y=130)

l2=Label(root,text="SELECT",font=("helvetica ",23,"bold"),fg="black",bg="powder blue")
l2.place(x=80,y=230)

checkbtn1=Checkbutton(root,text="Color",variable=varb2,font=("helvetica",18),bg="powder blue")
checkbtn1.place(x=330,y=230)

checkbtn2=Checkbutton(root,text="GrayScale",variable=varb1,font=("helvetica ",18),bg="powder blue")
checkbtn2.place(x=500,y=230)

l3=Label(root,text="FACE NO ABOVE",font=("helvetica",23,"bold"),fg="black",bg="powder blue")
l3.place(x=80,y=325)

e3=Entry(root,textvariable=var2,font=("helvetica ",19),bd=4,width=10)

e3.place(x=360,y=325)

l4=Label(root,text="DESTINATION",font=("helvetica ",23,"bold"),fg="black",bg="powder blue")

l4.place(x=80,y=420)

e4=Entry(root,textvariable=var3,font=("helvetica",19),bd=4,width=23)
e4.place(x=320,y=420)

bt1=Button(root,text="open",font=("helvitica",14),command=opens1)
bt1.place(x=660,y=420)

btn2=Button(root,text="Extract Image",bg="green",fg="white",font=("helvitica",18),command=show)
btn2.place(x=80,y=535)


btn1=Button(root,text="Show",bg="yellow4",fg="white",font=("helvitica",18),command=show1)
btn1.place(x=320,y=535)

btn2=Button(root,text="Quit",font=("helvitica",18),bg="red",fg="white",command=root.destroy)
btn2.place(x=460,y=535)

root.mainloop()
