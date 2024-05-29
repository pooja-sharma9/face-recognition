from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class Info:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x700+0+0")
        self.root.title("Information Panel")

        # backgorund image 
        bg=Image.open("C:/face_recognition system/image_data/image47.jpg")
        bg=bg.resize((1366,700),Image.Resampling.LANCZOS)
        self.photobg=ImageTk.PhotoImage(bg)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg)
        bg_img.place(x=0,y=0,width=1366,height=700)

        #title section
        title_lb1 = Label(bg_img,text="Information Pannel",font=("verdana",30,"bold"),bg="lightgreen",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # image 1
        image1=Image.open("C:/face_recognition system/image_data/Dean_mam.jpg")
        image1=image1.resize((160,160),Image.Resampling.LANCZOS)
        self.photobg2=ImageTk.PhotoImage(image1)

        # set image as lable
        img1 = Label(bg_img,image=self.photobg2)
        img1.place(x=10,y=65,width=160,height=160)

        #image 1 info
        info1 = Label(bg_img,text="Name: Dr Jaspreet Kaur\n Post: Dean\n Phone no: 8727004413",font=("verdana",15),bg="lightblue",fg="black")
        info1.place(x=190,y=85,width=500,height=110)

        # image 2
        image2=Image.open("C:/face_recognition system/image_data/Deputy_dean.jpg")
        image2=image2.resize((160,160),Image.Resampling.LANCZOS)
        self.photobg3=ImageTk.PhotoImage(image2)

        # set image as lable
        img2 = Label(bg_img,image=self.photobg3)
        img2.place(x=10,y=240,width=160,height=160)

        #image 2 info
        info2 = Label(bg_img,text="Name: Dr. Amandeep Singh\n Post: Deputy Dean\n Phone no:9915292267",font=("verdana",15),bg="lightblue",fg="black")
        info2.place(x=190,y=260,width=500,height=110)

        # image 3
        image3=Image.open("C:/face_recognition system/image_data/Jai_parkash.jpg")
        image3=image3.resize((160,160),Image.Resampling.LANCZOS)
        self.photobg4=ImageTk.PhotoImage(image3)

        # set image as lable
        img3 = Label(bg_img,image=self.photobg4)
        img3.place(x=10,y=415,width=160,height=160)

        #image 3 info
        info3 = Label(bg_img,text="Name: Er. Jai Parkash \n Post: HOD\n Phone no: 8427203511",font=("verdana",15),bg="lightblue",fg="black")
        info3.place(x=190,y=435,width=500,height=110)



if __name__ == "__main__":
    root=Tk()
    obj=Info(root)
    root.mainloop()

