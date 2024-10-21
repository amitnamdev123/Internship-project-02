def addstudent():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        try:
            strr = 'insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addedtime,addeddate))
            con.commit()
            res = messagebox.askyesnocancel('Notification','Id {} Name {} Added successfully and to clean the form',format(id,name),parent=addroot)
            if(res==True):
                idval.set(' ')
                nameval.set(' ')
                mobileval.set(' ')
                emailval .set(' ')
                addressval.set(' ')
                genderval.set(' ')
                dobval.set(' ')

        except:
            pass

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Student Management System')
    addroot.config(bg='gold')
    #addroot.iconbitmap('mana.ico')
    addroot.resizable(False,False)
    ##########-------------------------------------------------------------------------Labels
    idlabel = Label(addroot,text='Enter Id :',bg='blue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)
    
    namelabel = Label(addroot,text='Enter Name :',bg='blue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(addroot,text='Enter Mobile :',bg='blue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(addroot,text='Enter Email :',bg='blue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(addroot,text='Enter Address :',bg='blue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(addroot,text='Enter Gender :',bg='blue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)
     
    
    doblabel = Label(addroot,text='Enter D.O.B :',bg='blue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    ############--------------------------------------------------------------------------student entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    
    identry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)
    ###############---------------------------------------------------------button
    submitbtn = Button(addroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='gold',activeforeground='white',
                       bg='red',command=submitadd)
    submitbtn.place(x=150,y=420)

    addroot.mainloop()

def searchstudent():
    def search():
        print('search')
    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('Student Management System')
    searchroot.config(bg='gold')
    #searchroot.iconbitmap('mana.ico')
    searchroot.resizable(False,False)
    #---------------------------------------------------------------Lablels
    idlabel = Label(searchroot,text='Enter Id :',bg='blue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)
    
    namelabel = Label(searchroot,text='Enter Name :',bg='blue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(searchroot,text='Enter Mobile :',bg='blue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(searchroot,text='Enter Email :',bg='blue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(searchroot,text='Enter Address :',bg='blue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(searchroot,text='Enter Gender :',bg='blue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)
     
    doblabel = Label(searchroot,text='Enter D.O.B :',bg='blue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel = Label(searchroot,text='Enter Date :',bg='blue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)

    #----------------------------------------------------------------------------student entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    
    identry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)

    dateentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)
    ###############---------------------------------------------------------button
    submitbtn = Button(searchroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='gold',activeforeground='white',
                       bg='red',command=search)
    submitbtn.place(x=150,y=480)

    searchroot.mainloop()

def deletestudent():
    print('student delete')


def updatestudent():
    def update():
        print('update')
    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x585+220+160')
    updateroot.title('Student Management System')
    updateroot.config(bg='gold')
    #updateroot.iconbitmap('mana.ico')
    updateroot.resizable(False,False)
    #---------------------------------------------------------------Lablels
    idlabel = Label(updateroot,text='Enter Id :',bg='blue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)
    
    namelabel = Label(updateroot,text='Enter Name :',bg='blue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(updateroot,text='Enter Mobile :',bg='blue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(updateroot,text='Enter Email :',bg='blue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(updateroot,text='Enter Address :',bg='blue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(updateroot,text='Enter Gender :',bg='blue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)
     
    doblabel = Label(updateroot,text='Enter D.O.B :',bg='blue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel = Label(updateroot,text='Enter Date :',bg='blue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)

    timelabel = Label(updateroot,text='Enter Time :',bg='blue',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    timelabel.place(x=10,y=490)

    #----------------------------------------------------------------------------student entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()
    
    identry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)

    dateentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)

    timeentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    timeentry.place(x=250,y=490)
    ###############---------------------------------------------------------button
    submitbtn = Button(updateroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='gold',activeforeground='white',
                       bg='red',command=update)
    submitbtn.place(x=160,y=540)

    updateroot.mainloop()

def showstudent():
    print('student show')

def exportstudent():
    print('student export')

def exitstudent():
    res = messagebox.askyesnocancel('Warning','Do you want to exit')
    if(res == True):
        root.destroy()


#########################################################################
def Connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notification','Data is not Defined')
            return
        try:
            strr = 'create database studentmanagementsystem'
            mycursor.execute(strr)
            strr = 'use studentdatamanagementsystem'
            mycursor.execute(strr)
            strr = 'create table studentdata(id int(11),name varchar(20),mobile varchar(10),email varchar(30),address varchar(100),gender varchar(10),dob varchar(40),date varchar(40),time varchar(40))'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Database Created',parent=dbroot)
            
        except:
            strr = 'use studentmanagementsystem'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Connected to Database',parent=dbroot)
        dbroot.destroy

           
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.resizable(False,False)
    dbroot.config(bg='black')
    #____________________________connect
    hostlabel = Label(dbroot,text="Enter Host : ",bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot,text="Enter User : ",bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    userlabel.place(x=10,y=70)

    passwordlabel = Label(dbroot,text="Enter Password : ",bg='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    passwordlabel.place(x=10,y=130)

    #---------------------------------##############################connectdb labels
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot,font=('calibri',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10) 

    userentry = Entry(dbroot,font=('calibri',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=250,y=70) 

    passwordentry = Entry(dbroot,font=('calibri',15,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=250,y=130) 

    ###############################################----------------------------##########buttonconnectdbs
    submitbutton = Button(dbroot,text='Submit',font=('calibri',15,'bold'),width=15,command=submitdb)
    submitbutton.place(x=150,y=190)

    dbroot.mainloop()
###############################################################
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :'+date_string+"\n"+"Time :"+time_string)
    clock.after(200,tick)

###############################################################
import random
colors = ['black','white']
def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(1,IntroLabelColorTick)
def IntroLabelTick():
    global count,text
    if(count>=len(ss)):
        count = -1
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(200,IntroLabelTick)

from tkinter import *
from tkinter import Toplevel,messagebox
from tkinter . ttk import Treeview
from tkinter import ttk
import pymysql 
import time
root = Tk()
root.title('Student Management System')
root.config(bg='skyblue')
root.geometry('1174x700+200+50')
#root.iconbitmap('mana.ico')
root.resizable (False, False)
######################################################### FRAMES

DataEntryFrame = Frame(root, bg='black', relief=GROOVE, borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600) 

frontlabel = Label(DataEntryFrame,text='--------welcome----------',width=30,font=('arial',20,'italic bold'),bg='white')
frontlabel.pack(side=TOP,expand=True)
addbtn = Button(DataEntryFrame,text='1. Add Students',width=16,font=('calibri',15,'bold'),bd=6,bg='gold',activebackground='yellow',relief=RIDGE,
                activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text='2. Search Students',width=16,font=('calibri',15,'bold'),bd=6,bg='gold',activebackground='yellow',relief=RIDGE,
                activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text='3. Delete Students',width=16,font=('calibri',15,'bold'),bd=6,bg='gold',activebackground='yellow',relief=RIDGE,
                activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text='4. Update Students',width=16,font=('calibri',15,'bold'),bd=6,bg='gold',activebackground='yellow',relief=RIDGE,
                activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showallbtn = Button(DataEntryFrame,text='5. Show All',width=16,font=('calibri',15,'bold'),bd=6,bg='gold',activebackground='yellow',relief=RIDGE,
                activeforeground='white',command=showstudent)
showallbtn.pack(side=TOP,expand=True)

exportbtn = Button(DataEntryFrame,text='6. Export Data',width=16,font=('calibri',15,'bold'),bd=6,bg='gold',activebackground='yellow',relief=RIDGE,
                activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text='7. Exit',width=16,font=('calibri',15,'bold'),bd=6,bg='gold',activebackground='yellow',relief=RIDGE,
                activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)


#######################################################################################SHOWFRAMES

ShowDataFrame = Frame(root,bg='white', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=620,height=600)

#######################-------------------------------------------------------SHOW DATAFRAMES

style = ttk.Style()
style.configure('Treeview.Heading',font=('calibri',15,'bold'),foreground='black')
style.configure('Treeview',font=('calibri',15,'bold'),foreground='black',background='white')
scroll_x = Scrollbar(ShowDataFrame,orient='horizontal')
scroll_y = Scrollbar(ShowDataFrame,orient='vertical')
studenttable = Treeview(ShowDataFrame,columns=('ID','Name','Mobile No.','Email','Address','Gender','D.O.B','Date of Entry','Time'),
                        yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('ID',text='ID')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No.',text='Mobile No.')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Date of Entry',text='Date of Entry')
studenttable.heading('Time',text='Time')
studenttable['show'] = 'headings'
studenttable.pack(fill=BOTH,expand=1)

studenttable.column('ID',width=150)
studenttable.column('Name',width=200)
studenttable.column('Mobile No.',width=200)
studenttable.column('Email',width=300)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=150)
studenttable.column('D.O.B',width=150)
studenttable.column('Date of Entry',width=200)
studenttable.column('Time',width=150)

###########################################################

ss= 'Welcome To Student Management System'
count = 0
text=''

#######################################

SliderLabel = Label (root,text=ss, font=('calibri', 30, 'bold'), relief=RIDGE, borderwidth =4,width=35,bg='cyan')
SliderLabel.place(x=200,y=0)
IntroLabelTick(  )
IntroLabelColorTick()

###########################################################

clock = Label(root, font=('times',14,'bold'), relief=RIDGE, borderwidth=4,width=15,bg='lawn green')
clock.place(x=0,y=0)
tick()

#############################################################
connectbutton = Button(root,text='connect to Database',width=20,command=Connectdb)
connectbutton.place(x=980,y=10)
root.mainloop()
