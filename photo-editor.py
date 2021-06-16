from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os



root=Tk()
screen_w=root.winfo_screenwidth()
screen_h=root.winfo_screenheight()
root.geometry("%dx%d" %(screen_w,screen_h))
root.title("Photo-Editor")


def select_file():
    global file_name,img
    file_name=filedialog.askopenfilename(initialdir=os.getcwd())
    img=Image.open(file_name)
    img.thumbnail((1000,600))
    img1=ImageTk.PhotoImage(img)
    pic_canvas.create_image(500,300,image=img1,anchor=CENTER)
    pic_canvas.image=img1

def rotate():
    global rot_val
    rot_val =rot_val+1
    img=Image.open(file_name)
    img.thumbnail((1000,600))
    angle=rot_val*90
    img2=img.rotate(angle)
    img3=ImageTk.PhotoImage(img2)
    pic_canvas.create_image(500,300,image=img3,anchor=CENTER)
    pic_canvas.image=img3

def flip():
    global flip_flag
    flip_flag=flip_flag+1
    img=Image.open(file_name)
    img.thumbnail((1000,600))
    if flip_flag%2 != 0:
        img4=img.transpose(Image.FLIP_LEFT_RIGHT)
    else:
        img4=img

    img5=ImageTk.PhotoImage(img4)
    pic_canvas.create_image(500,300,image=img5,anchor=CENTER)
    pic_canvas.image=img5
    
    
    

    
    
    


pic_canvas=Canvas(root,width=1000,height=600,bg="black")
pic_canvas.place(x=screen_w-1000,y=50)
insert=Button(root,text="Select Image",font=("Arial Black",10),command=lambda:select_file())
insert.place(x=screen_w-500,y=680)
save=Button(root,text="Save",font=("Arial Black",10))
save.place(x=screen_w-700,y=680)
rot_val=0
rotate_btn=Button(root,text="Rotate",font=("Arial Black",10),command=lambda:rotate())
rotate_btn.place(x=500,y=20)
flip_flag=1
flip_btn=Button(root,text="Flip",font=("Arial Black",10),command=lambda:flip())
flip_btn.place(x=600,y=20)
mainloop()
