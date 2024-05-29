from tkinter import*
from PIL import Image,ImageTk

class Helpsupport:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x700+0+0")
        self.root.title("Help Panel")

        # backgorund image 
        bg=Image.open("C:/face_recognition system/image_data/bg4.png")
        bg=bg.resize((1366,700),Image.Resampling.LANCZOS)
        self.photobg=ImageTk.PhotoImage(bg)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg)
        bg_img.place(x=0,y=0,width=1366,height=700)

        #title section
        title_lb1 = Label(bg_img,text="Help Pannel",font=("verdana",30,"bold"),bg="lightgreen",fg="red")
        title_lb1.place(x=0,y=0,width=1366,height=45)
        
        # image bg
        bg2=Image.open("C:/face_recognition system/image_data/hlp.jpg")
        bg2=bg2.resize((400,510),Image.Resampling.LANCZOS)
        self.photobg2=ImageTk.PhotoImage(bg2)

        # set image as lable
        bg_img1 = Label(bg_img,image=self.photobg2)
        bg_img1.place(x=20,y=70,width=500,height=600)

        info= Label(bg_img,text="Contact Us:",font=("verdana",15),bg="blue",fg="white")
        info.place(x=600,y=100,width=500,height=40)

        # email image
        image3=Image.open("C:/face_recognition system/image_data/gmail.png")
        image3=image3.resize((160,160),Image.Resampling.LANCZOS)
        self.photobg4=ImageTk.PhotoImage(image3)

        # set image as lable
        img3 = Label(bg_img,image=self.photobg4)
        img3.place(x=600,y=200,width=160,height=160)

        #email
        info= Label(bg_img,text="ggi2021.1494@gmail.com\n ggi2021.2465@ggi.ac.in\n ggi2021.2056@ggi.ac.in\n ggi2021.1043@ggi.ac.in",font=("verdana",15),bg="lightblue",fg="black")
        info.place(x=780,y=228,width=500,height=110)

if __name__ == "__main__":
    root=Tk()
    obj=Helpsupport(root)
    root.mainloop()