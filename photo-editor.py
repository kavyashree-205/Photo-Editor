from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image,ImageEnhance
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
    global rot_val,file_name
    rot_val =rot_val+1
    img=Image.open(file_name)
    img.thumbnail((1000,600))
    angle=rot_val*90
    img2=img.rotate(angle)
    img3=ImageTk.PhotoImage(img2)
    pic_canvas.create_image(500,300,image=img3,anchor=CENTER)
    pic_canvas.image=img3

    

def flip():
    global flip_flag,file_name
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




def tint(event):
    global file_name
    val=tint_scale.get()
    for i in range(0,val+1):
        img=Image.open(file_name)
        img.thumbnail((1000,600))
        img_tint=ImageEnhance.Color(img)
        img6=img_tint.enhance(i)
        img7=ImageTk.PhotoImage(img6)
        pic_canvas.create_image(500,300,image=img7,anchor=CENTER)
        pic_canvas.image=img7


def contrast(event):
    val1=contrast_scale.get()
    for i in range(0,val1+1):
        img=Image.open(file_name)
        img.thumbnail((1000,600))
        img_contrast=ImageEnhance.Contrast(img)
        img8=img_contrast.enhance(i)
        img9=ImageTk.PhotoImage(img8)
        pic_canvas.create_image(500,300,image=img9,anchor=CENTER)
        pic_canvas.image=img9
    

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
Label(root,text="tint",font=("Arial Black",10)).place(x=700,y=20)
tint_val=IntVar()
tint_scale=Scale(root,from_=0,to=10,variable=tint_val,orient=HORIZONTAL,troughcolor="black",length=200,command=tint)
tint_scale.place(x=750,y=5)
Label(root,text="Contrast",font=("Arial Black",10)).place(x=900,y=20)
contrast_val=IntVar()
contrast_scale=Scale(root,from_=0,to=10,variable=contrast_val,orient=HORIZONTAL,troughcolor="black",length=200,command=contrast)
contrast_scale.place(x=1000,y=5)

mainloop()
