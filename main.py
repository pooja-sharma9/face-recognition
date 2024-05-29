import tkinter
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from face_recognition import Face_Recognition
from attendance import Attendance
import os
from datetime import datetime
from time import strftime
from info import Info
from helpsupport import Helpsupport
from train import train_classifier

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recogonition System")

# This part is image labels setting start 
        # first header image  
        img=Image.open("C:/face_recognition system/image_data/image43.jpg")
        img=img.resize((1366,115),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=115)

        #===================time================================
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(f_lb1,font=("verdana",15,"bold"),bg="blue",fg="snow")
        lbl.place(x=1200,y=20,width=155,height=50)
        time()


        # logo image
        img1=Image.open("C:/face_recognition system/image_data/image36.jpg")
        img1=img1.resize((140,100),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

         # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg1)
        f_lb1.place(x=6,y=6,width=140,height=100)

        # backgorund image 
        bg1=Image.open("C:/face_recognition system/image_data/bg.png")
        bg1=bg1.resize((1366,768),Image.Resampling.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=115,width=1366,height=768)


        #title section
        title_lbl = Label(bg_img,text="Attendance Managment System Using Facial Recognition",font=("verdana",30,"bold"),bg="darkgreen",fg="white")
        title_lbl.place(x=0,y=0,width=1366,height=50)

        # image bg
        bg2=Image.open("C:/face_recognition system/image_data/image6.png")
        bg2=bg2.resize((260,520),Image.Resampling.LANCZOS)
        self.photobg2=ImageTk.PhotoImage(bg2)

        # set image as lable
        bg_img1 = Label(bg_img,image=self.photobg2)
        bg_img1.place(x=2,y=54,width=260,height=520)


        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open("C:/face_recognition system/image_data/image18.jpg.jfif")
        std_img_btn=std_img_btn.resize((160,160),Image.Resampling.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,image=self.std_img1,command=self.student_pannels,cursor="hand2")
        std_b1.place(x=350,y=100,width=160,height=160)

        std_b1_1 = Button(bg_img,command=self.student_pannels,text="Student Pannel",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=350,y=260,width=160,height=35)

        # Detect Face  button 2
        det_img_btn=Image.open("c:/face_recognition system/image_data/det1.jpg")
        det_img_btn=det_img_btn.resize((160,160),Image.Resampling.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.face_rec,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=560,y=100,width=160,height=160)

        det_b1_1 = Button(bg_img,command=self.face_rec,text="Face Detector",cursor="hand2",font=("tahoma",15,"bold"),bg="snow",fg="navyblue")
        det_b1_1.place(x=560,y=260,width=160,height=35)

         # Attendance System  button 3
        att_img_btn=Image.open("C:/face_recognition system/image_data/images25.jfif")
        att_img_btn=att_img_btn.resize((160,160),Image.Resampling.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.attendance_pannel,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=770,y=100,width=160,height=160)

        att_b1_1 = Button(bg_img,command=self.attendance_pannel,text="Attendance",cursor="hand2",font=("tahoma",15,"bold"),bg="snow",fg="navyblue")
        att_b1_1.place(x=770,y=260,width=160,height=35)

         # Help  Support  button
        hlp_img_btn=Image.open("C:/face_recognition system/image_data/hlp.jpg")
        hlp_img_btn=hlp_img_btn.resize((160,160),Image.Resampling.LANCZOS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.help_pannel,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=980,y=100,width=160,height=160)

        hlp_b1_1 = Button(bg_img,command=self.help_pannel,text="Help Support",cursor="hand2",font=("tahoma",15,"bold"),bg="snow",fg="navyblue")
        hlp_b1_1.place(x=980,y=260,width=160,height=35)

        # Top 4 buttons end.......
        # ---------------------------------------------------------------------------------------------------------------------------
        # Start below buttons.........
         # Train   button 5
        tra_img_btn=Image.open("C:/face_recognition system/image_data/tra1.jpg")
        tra_img_btn=tra_img_btn.resize((160,160),Image.Resampling.LANCZOS)
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,command=self.train_pannels,image=self.tra_img1,cursor="hand2",)
        tra_b1.place(x=350,y=330,width=160,height=160)

        tra_b1_1 = Button(bg_img,command=self.train_pannels,text="Data Train",cursor="hand2",font=("tahoma",15,"bold"),bg="snow",fg="navyblue")
        tra_b1_1.place(x=350,y=490,width=160,height=35)

        # Photo   button 6
        pho_img_btn=Image.open("C:/face_recognition system/image_data/image21.jpg")
        pho_img_btn=pho_img_btn.resize((160,160),Image.Resampling.LANCZOS)
        self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img,command=self.open_img,image=self.pho_img1,cursor="hand2",)
        pho_b1.place(x=560,y=330,width=160,height=160)

        pho_b1_1 = Button(bg_img,command=self.open_img,text="Photos",cursor="hand2",font=("tahoma",15,"bold"),bg="snow",fg="navyblue")
        pho_b1_1.place(x=560,y=490,width=160,height=35)

        # Info   button 7
        info_img_btn=Image.open("C:/face_recognition system/image_data/dev.jpg")
        info_img_btn=info_img_btn.resize((160,160),Image.Resampling.LANCZOS)
        self.info_img1=ImageTk.PhotoImage(info_img_btn)

        info_b1 = Button(bg_img,command=self.info_pannel,image=self.info_img1,cursor="hand2",)
        info_b1.place(x=770,y=330,width=160,height=160)

        info_b1_1 = Button(bg_img,command=self.info_pannel,text="Information",cursor="hand2",font=("tahoma",15,"bold"),bg="snow",fg="navyblue")
        info_b1_1.place(x=770,y=490,width=160,height=35)

        # exit   button 8
        exi_img_btn=Image.open("C:/face_recognition system/image_data/images27.jfif")
        exi_img_btn=exi_img_btn.resize((160,160),Image.Resampling.LANCZOS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,command=self.iExit,image=self.exi_img1,cursor="hand2",)
        exi_b1.place(x=980,y=330,width=160,height=160)

        exi_b1_1 = Button(bg_img,command=self.iExit,text="Exit",cursor="hand2",font=("tahoma",15,"bold"),bg="snow",fg="navyblue")
        exi_b1_1.place(x=980,y=490,width=160,height=35)

    # ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("C:/face_recognition system/data_img")
    #=============================Functions Button=======================================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=(train_classifier(self))

    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def info_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Info(self.new_window)

    def help_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpsupport(self.new_window)

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition System","Do you want to exit?",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()