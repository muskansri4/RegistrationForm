import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Muskan@1999",database="guidb"
)

win=tk.Tk()
win.title('CHECK')
"""menubar=tk.Menu(win)
menubar.add_command(label='save')
win.configure(menu=menubar)"""

nb=ttk.Notebook(win)
page1=ttk.Frame(nb)
page2=ttk.Frame(nb)
nb.add(page1,text='HOME')
nb.add(page2,text='HELP')
nb.grid(row='0',column='0')
#nb.pack(expand=True,fill='both')


#labelframe
label=ttk.LabelFrame(page1,text="Please enter the details")
label.grid(row=1,column=0,padx=450)

#details
name=ttk.Label(label,text="Enter your name :")
name.grid(row=0,column=0,sticky=tk.W,padx=8,pady=4)

age=ttk.Label(label,text="Enter your age:")
age.grid(row=1,column=0,sticky=tk.W,padx=8,pady=4)

gender=ttk.Label(label,text="Enter your gender :")
gender.grid(row=2,column=0,sticky=tk.W,padx=8,pady=4)

adhar=ttk.Label(label,text="Enter your adhar card number :")
adhar.grid(row=3,column=0,sticky=tk.W,padx=8,pady=4)


#box
namev=tk.StringVar()
namee=ttk.Entry(label,width=16,textvariable=namev)
namee.grid(row=0,column=1,padx=8,pady=4)
namee.focus()


agev=tk.StringVar()
agee=ttk.Entry(label,width=16,textvariable=agev)
agee.grid(row=1,column=1,padx=8,pady=4)

genderv=tk.StringVar()
gendere=ttk.Combobox(label,width=16,textvariable=genderv,state='readonly')
gendere['values']=('male','female','other')
gendere.grid(row=2,column=1,padx=8,pady=4)
gendere.current(0)

adharv=tk.StringVar()
adhare=ttk.Entry(label,width=16,textvariable=adharv)
adhare.grid(row=3,column=1,padx=8,pady=4)

#radiobutton
nation=tk.StringVar()
radiobuttn1=ttk.Radiobutton(label,text='INDIAN',value='indian',variable=nation)
radiobuttn1.grid(row=4,column=0)

radiobuttn2=ttk.Radiobutton(label,text='non indian',value='non indian',variable=nation)
radiobuttn2.grid(row=4,column=1)
 
#checkbutton
checkbtnv=tk.IntVar()
checkbtn=ttk.Checkbutton(label,text='i declare that information are correct',variable=checkbtnv)
checkbtn.grid(row=5,columnspan=3)

#newpage
new=ttk.Label(page2,text="Enter your name :")
new.grid(row=0,column=1,padx=8,pady=4)
#def action
"""def action():
    username=namev.get()
    userage=agev.get()
    usergender=genderv.get()
    usernation=nation.get()
    userdeclare=checkbtnv.get()
    if userdeclare==0:
        userdeclaration='no'
    else:
           userdeclaration='yes'
    
    with open('file7.txt','a') as f:
        f.write(f'{username},{userage},{usergender},{usernation},{userdeclaration}\n')
    namee.delete(0,tk.END) 
    agee.delete(0,tk.END)    
    gendere.delete(0,tk.END) 
    namee.configure(foreground='Blue')
    agee.configure(foreground='Blue')
    gendere.configure(foreground='Blue')
    submit.configure(foreground='Blue')"""
#wite to csv file
def action():
    username=namev.get()
    userage=agev.get()
    usergender=genderv.get()
    usernation=nation.get()
    userdeclare=checkbtnv.get()
    useradhar=adharv.get()
    if userdeclare==0:
        userdeclaration='no'
    else:
           userdeclaration='yes' 
    with open('file8.csv','a',newline="") as f:
        dict_writer=DictWriter(f,fieldnames=['usernamee','useragee','usergenderr','usernationn','userdeclarationn','useradharr'])
        if os.stat('file8.csv').st_size==0:
            
           dict_writer.writeheader()
        dict_writer.writerow({
                'usernamee':username,
                'useragee':userage,
                'usergenderr':usergender,
                'usernationn':usernation,
                'userdeclarationn':userdeclaration,
                'useradharr':useradhar
                })
    
    namee.delete(0,tk.END) 
    agee.delete(0,tk.END)    
    gendere.delete(0,tk.END) 
    namee.configure(foreground='Blue')
    agee.configure(foreground='Blue')
    gendere.configure(foreground='Blue')
    submit.configure(foreground='Blue')
    
    
    




def action():
    mycursor = mydb.cursor()

    sql = "INSERT INTO customers4 (NAME,AGE,GENDER,NATION,DECLARATION,ADHAR) VALUES (%s,%s,%s,%s,%s,%s)"
 
    t=namev.get()
 
    s=agev.get()
    u=genderv.get()
    v=nation.get()
    w=checkbtnv.get()
    x=adharv.get()
    
    val = (t,s,u,v,w,x)
    mycursor.execute(sql, val)

    mydb.commit()

    mycursor.execute("SELECT * FROM customers")

    myresult = mycursor.fetchall()

    for x in myresult:
       print(x)
#submitbutton
submit=tk.Button(label,text='submit',command=action)
submit.grid(row=6,column=0)

win.mainloop() 