from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image,ImageEnhance,ImageFilter
import random
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


def blur():
    img=Image.open(file_name)
    img.thumbnail((1000,600))
    img10=img.filter(ImageFilter.BoxBlur(5))
    img11=ImageTk.PhotoImage(img10)
    pic_canvas.create_image(500,300,image=img11,anchor=CENTER)
    pic_canvas.image=img11

def emboss():
    img=Image.open(file_name)
    img.thumbnail((1000,600))
    img12=img.filter(ImageFilter.EMBOSS)
    img13=ImageTk.PhotoImage(img12)
    pic_canvas.create_image(500,300,image=img13,anchor=CENTER)
    pic_canvas.image=img13

def smooth():
    img=Image.open(file_name)
    img.thumbnail((1000,600))
    img14=img.filter(ImageFilter.SMOOTH)
    img15=ImageTk.PhotoImage(img14)
    pic_canvas.create_image(500,300,image=img15,anchor=CENTER)
    pic_canvas.image=img15

def choose_random():
    r=random.randint(1,3)
    if r==1:
        blur()
    elif r==2:
        emboss()
    elif r==3:
        smooth()

def pak():
    position=(e1.get()).split(",")
    pic_canvas.create_text(int(position[0]),int(position[1]),text=e.get())

def add_text():
    global e,e1,root1,done,position
    root1=Tk()
    root1.geometry("500x100")
    root1.title("Add Text")
    Label(root1,text="Enter Text").pack()

    e=Entry(root1,width=10,bd=3,textvariable=text)
    e.pack()
    
    Label(root1,text="Enter Position X,Y").pack()
    e1=Entry(root1,width=10,bd=3,textvariable=pos)
    e1.pack()
    done=Button(root1,text="Done",command=pak)
    done.pack()


pic_canvas=Canvas(root,width=1000,height=600,bg="pink")
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
r_filter=Button(root,text="Apply Random Filter",font=("Arial Black",10),command=choose_random)
r_filter.place(x=200,y=50)
a_text=Button(root,text="Add Text",font=("Arial Black",10),command=add_text)
a_text.place(x=100,y=100)
text=StringVar()
pos=StringVar()

mainloop()
