import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog


#Global variable for importCsv Function 
mydata=[]
class Attendance:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Attendance Pannel")

        #-----------Variables-------------------
        self.var_course=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()

        # This part is image labels setting start 
        # first header image  
        img=Image.open("C:/face_recognition system/image_data/image45.jpg")
        img=img.resize((1366,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open("C:/face_recognition system/image_data/image45.jpg")
        bg1=bg1.resize((1366,569),Image.Resampling.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=569)


        #title section
        title_lb1 = Label(bg_img,text="Welcome to Attendance Pannel",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        #========================Section Creating==================================

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=4,y=55,width=1355,height=510)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=10,width=660,height=480)

        # ==================================Text boxes and Combo Boxes====================

        #Student Roll
        student_roll_label = Label(left_frame,text="Roll-No:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_roll_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        student_roll_entry = ttk.Entry(left_frame,textvariable=self.var_roll,width=15,font=("verdana",12,"bold"))
        student_roll_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Studnet Name
        student_name_label = Label(left_frame,text="Std-Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(left_frame,textvariable=self.var_name,width=15,font=("verdana",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #Department
        dep_label = Label(left_frame,text="Department:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        dep_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        dep_entry = ttk.Entry(left_frame,textvariable=self.var_dep,width=15,font=("verdana",12,"bold"))
        dep_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #Date 
        date_label = Label(left_frame,text="Date:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        date_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        date_entry = ttk.Entry(left_frame,textvariable=self.var_date,width=15,font=("verdana",12,"bold"))
        date_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #time
        time_label = Label(left_frame,text="Time:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        time_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        time_entry = ttk.Entry(left_frame,textvariable=self.var_time,width=15,font=("verdana",12,"bold"))
        time_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        studentId_label = Label(left_frame,text="Course:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        studentId_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        studentId_entry = ttk.Entry(left_frame,textvariable=self.var_course,width=15,font=("verdana",12,"bold"))
        studentId_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        #Attendance
        student_attend_label = Label(left_frame,text="Attend-status:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_attend_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        attend_combo=ttk.Combobox(left_frame,textvariable=self.var_attend,width=13,font=("verdana",12,"bold"),state="readonly")
        attend_combo["values"]=("Status","Present","Absent")
        attend_combo.current(0)
        attend_combo.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        # =========================button section========================

        #Button Frame
        btn_frame = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=87,y=370,width=466,height=60)

        #Improt button
        import_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        import_btn.grid(row=0,column=0,padx=6,pady=10,sticky=W)

        #Exprot button
        export_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        export_btn.grid(row=0,column=1,padx=6,pady=8,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)

        # Right section=======================================================

        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=680,y=10,width=660,height=480)

        # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=90,width=635,height=360)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport = ttk.Treeview(table_frame,column=("Roll_No","Name","Department","Time","Date","Course","Attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        
        self.attendanceReport.heading("Roll_No",text="Roll-No")
        self.attendanceReport.heading("Name",text="Std-Name")
        self.attendanceReport.heading("Department",text="Department")
        self.attendanceReport.heading("Time",text="Time")
        self.attendanceReport.heading("Date",text="Date")
        self.attendanceReport.heading("Course",text="Course")
        self.attendanceReport.heading("Attend",text="Attend-status")
        self.attendanceReport["show"]="headings"


        # Set Width of Colums 
        
        self.attendanceReport.column("Roll_No",width=100)
        self.attendanceReport.column("Name",width=100)
        self.attendanceReport.column("Department",width=100)
        self.attendanceReport.column("Time",width=100)
        self.attendanceReport.column("Date",width=100)
        self.attendanceReport.column("Course",width=100)
        self.attendanceReport.column("Attend",width=100)
        
        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor)

    # =========================Fetch Data Import data ===============

    def fetchData(self,rows):
        self.attendanceReport.delete(*self.attendanceReport.get_children())
        for i in rows:
            self.attendanceReport.insert("",END,values=i)
        
        

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)

    #==================Experot CSV=============
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfuly","Export Data Successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 

        #=============Cursur Function for CSV========================

    def get_cursor(self,event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        data = content["values"]

        self.var_roll.set(data[0]),
        self.var_name.set(data[1]),
        self.var_dep.set(data[2]),
        self.var_time.set(data[3]),
        self.var_date.set(data[4]),
        self.var_course.set(data[5]),
        self.var_attend.set(data[6])  

    #============================Reset Data======================
    def reset_data(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_course.set("")
        self.var_attend.set("Status")





if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
