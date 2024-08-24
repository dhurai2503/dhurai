from tkinter import *
top=Tk()
top.geometry("1400x800")
top.title("dhuraisamy")
top.config(bg="brown")

welcome=Label(top,text="Wellcome our page",font=('TimesNewRoman',25,'italic'),fg="white",bg="brown")
welcome.place (x=550,y=75)

def Login():
    K=Frame(top,height=700,width=400,bg="")
    K.pack(fill=X)
    K.config(bg="brown")
    
    lab=Label(K,text="Login page",font=('TimesNewRoman',35,'italic'),fg="white",bg="brown")
    lab.place (x=600,y=75)
    
    name=Label(K,text="Username  ",font=('TimesNewRoman',20,'italic'),fg="white",bg="brown")
    name.place (x=350,y=200)
    nam=Label(K,text="Password  ", font=('TimesNewRoman',20,'italic'),fg="white",bg="brown")
    nam.place (x=350,y=250)

    BOX=Entry(K,text=" ",font=('TimesNewRoman',20,'italic'),fg="black")
    BOX.place (x=600,y=200,width=200,height=25)
    BO=Entry(K,text=" ",font=('TimesNewRoman',20,'italic'),fg="black")
    BO.place (x=600,y=250,width=200,height=25)
    
    but=Button(K,text="Login",font=('TimesNewRoman',20,'italic'),fg="white",bg="sky blue")
    but.place(x=600,y=450,width=200,height=30)
    m=Label(K,text="Don't have account?",font=('TimesNewRoman',20,'italic'),fg="white",bg="brown")
    m.place (x=350,y=550)
    bu=Button(K,text="Sign in",font=('TimesNewRoman',20,'italic'),fg="black",bg="orange")
    bu.place(x=650,y=550,width=200,height=30)
    
but=Button(top,text="GET STARTED",font=('TimesNewRoman',25,'italic'),fg="black",activebackground="orange",activeforeground="black",command=Login)
but.place(x=550,y=600,width=300,height=40)

top.mainloop()
