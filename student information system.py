from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import pymysql

dbc=pymysql.connect(host='localhost',user='root',passwd='',db='shyam')

c=dbc.cursor()

c.execute('select * from sis')

data=c.fetchall()

win = Tk()
win.title('ENTER STUDENT INFORMATION')
win.geometry('600x600')
win.config(bg='blue')

def register():
     
     first = e1.get()
     last = e2.get()
     dob = str(e3.get())
     father = e4.get()
     com = str(course.get())
     gender = var_chk.get()
     email = e5.get()
     cellnum = e6.get()
     fullname=first + last
         
     if gender == 1:
          gender='Male'
     else:
          gender ='Female'
          
     result = str('Full Name:'+first+last+'\n'+'DOB:'+dob+'\n'+'Father Name:'+father+'\n'+'Course:'+com+'\n'+'Gender:'+str(gender)+'\n'+'email:'+email+'\n'+'cellnumber:'+cellnum)
     newwindow=Toplevel(win)
     newwindow.geometry('1090x1200')
     newwindow.config(bg='green')
     newwindow.title('STUDENT INFORMATION')
     messagebox.showinfo('DATABASE', 'DATABASE WAS SUCCESSFULLY CREATED')
     l=Label(newwindow,text='FULL NAME',fg='yellow',bg='green',font=('calibri Bold',20))
     l.place(x=10,y=20)

     
#text box
     
     text = Text(newwindow,height=7,width=30)
     text.place(x=600,y=300)
     text.insert(0.0,result)
     
     kv="INSERT INTO sis(fullname,gender,DateOfBirth,fathername,selectedCourse,email,cellnumber)VALUES(%s,%s,%s,%s,%s,%s,%s)"
     val=(fullname,gender,dob,father,com,email,cellnum)
     c.execute(kv,val)
     
     dbc.commit()
     dbc.rollback()
     dbc.close()
     
def clear():
     e1.delete(first=0,last=100000)
     e2.delete(first=0,last=100000)
     e3.delete(first=0,last=100000)
     e4.delete(first=0,last=100000)
     e5.delete(first=0,last=100000)
     e6.delete(first=0,last=100000)
     course.delete(first=0,last=100000)
     text.delete(0.0,END)
     var_chk.set(0)

def show():
      
     for i in data:
       print('+++++++++++++++++++++++++++++++++++')
       print(i)
     
def cancel():
     win.destroy()
     

#labels
first_name = Label(win,text='First Name')
first_name.grid(row=0,column=0)
last_name = Label(win,text='Last Name')
last_name.grid(row=1,column=0)
roll = Label(win,text='DOB')
roll.grid(row=2,column=0)
father_name = Label(win,text='Father Name')
father_name.grid(row=3,column=0)
gender = Label(win,text='email')
gender.grid(row=4,column=0)
gender = Label(win,text='cellnumber')
gender.grid(row=5,column=0)
select_course = Label(win,text='Select course')
select_course.grid(row=6,column=0)
gender = Label(win,text='Select gender')
gender.grid(row=7,column=0)



#Combo box
course = Combobox(win)
course['values']= ('Data Science','Cloud Computing','Internet of things ','Artificial Intelligence','Ethical hacking')
course.current(None) 
course.grid(row=6,column=1)


#entry
e1 = Entry(win)
e1.grid(row=0,column=1)
e2 = Entry(win)
e2.grid(row=1,column=1)
e3 = Entry(win)
e3.grid(row=2,column=1)
e4 = Entry(win)
e4.grid(row=3,column=1)
e5 = Entry(win)
e5.grid(row=4,column=1)
e6 = Entry(win)
e6.grid(row=5,column=1)

#Radio button
var_chk = IntVar()
radio1 = Radiobutton(win,text='Male',variable=var_chk,value=1)
radio1.grid(row=7,column=1)
radio2 = Radiobutton(win,text='Female',variable=var_chk,value=2)
radio2.grid(row=7,column=2)



#Buttons
b1 = Button(win,text='Register',command=register)
b1.grid(row=14,column=1)
b2 = Button(win,text='Exit',command=cancel)
b2.grid(row=14,column=2)
b3 = Button(win,text='Clear',command=clear)
b3.grid(row=14,column=3)
b4 = Button(win,text='print database',command=show)
b4.grid(row=14,column=4)




win.mainloop()

