from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
# Aarsh Saxena 21bec001

class Qr_Generator:
    def __init__(self,root): 
        self.root=root      #defining size of window
        self.root.geometry("900x500+280+120")
        self.root.title("Developed by Aarsh Saxena")
        self.root.resizable(False,False)

        # title of application 
        # # Aarsh Saxena 21bec001
        title=Label(self.root, text="QR Code Generator",font=("times new roman",40),bg="#053246",fg="white").place(x=0,y=0,relwidth=1)

        # QR Details
        details_frame=Frame(self.root,bd=2,relief=RIDGE, bg="white")
        details_frame.place(width=500,height=380,x=50,y=100)
        
        details_title=Label(details_frame, text="QR Code Generator",font=("times new roman",20),bg="#033246",fg="white").place(x=0,y=0,relwidth=1)
        
        # Aarsh Saxena 21bec001
        #variables
        self.var_filename=StringVar()
        self.var_heading=StringVar()
        self.var_content=StringVar()
        self.var_size=StringVar()

        # Aarsh Saxena 21bec001
        #input details
        qr_filename=Label(details_frame, text="File Name:",font=("times new roman",15,"bold"),bg="white").place(x=20,y=60)
        qr_heading=Label(details_frame, text="Title:",font=("times new roman",15,"bold"),bg="white").place(x=20,y=100)
        qr_content=Label(details_frame, text="Content:",font=("times new roman",15,"bold"),bg="white").place(x=20,y=140)
        qr_size=Label(details_frame, text="QR Size:",font=("times new roman",15,"bold"),bg="white").place(x=20,y=180)

        # input fields for inputs
        in_filename=Entry(details_frame, textvariable=self.var_filename ,font=("times new roman",15),bg="light yellow",).place(x=200,y=60)
        in_heading=Entry(details_frame,textvariable=self.var_heading ,font=("times new roman",15),bg="light yellow",).place(x=200,y=100)
        in_content=Entry(details_frame,textvariable=self.var_content ,font=("times new roman",15),bg="light yellow",).place(x=200,y=140)
        in_size=Entry(details_frame,textvariable=self.var_size ,font=("times new roman",15),bg="light yellow",).place(x=200,y=180)

        #buttons
        btn_generate=Button(details_frame, text="Generate",command=self.generate,font=("times new roman",17),bg="green",fg="white").place(x=20,y=250,width=180,height=40)
        btn_clear=Button(details_frame, text="Clear",command=self.clear,font=("times new roman",17),bg="green",fg="white").place(x=225,y=250,width=180,height=40)

        #messages
        self.msg=''
        self.lbl_msg=Label(details_frame, text=self.msg,font=("times new roman",15,),bg="white",fg="green")
        self.lbl_msg.place(x=0,y=310,relwidth=1)

        #qr code window
        # QR Details
        qr_frame=Frame(self.root,bd=2,relief=RIDGE, bg="white")
        qr_frame.place(width=280,height=380,x=570,y=100)

        qr_title=Label(qr_frame, text="QR Sample",font=("times new roman",20),bg="#033246",fg="white").place(x=0,y=0,relwidth=1)

        self.qr_code=Label(qr_frame,text="No QR \nAvailable",font=("times new roman",15),bg="white",bd=1,relief=RIDGE)
        self.qr_code.place(x=42,y=100,width=180,height=180)
        self.qr_code.place(x=42,y=100,width=180,height=180)


        # Aarsh Saxena 21bec001
    # clear button functions
    def clear(self):
        self.var_filename.set('')
        self.var_heading.set('')
        self.var_content.set('')
        self.var_size.set('')

        #clearing any message
        self.msg=''
        self.lbl_msg.config(text=self.msg)

        # clearing qr image
        self.qr_code.config(image='')


    #generate button functions
    def generate(self):
        #checking if null values
        if(self.var_filename.get()=='' or self.var_content.get()=='' or self.var_heading.get()=='' or self.var_size.get()==''):
            self.msg='All Fields Are Required.'
            self.lbl_msg.config(text=self.msg,fg="red")

        #checking if size has numeric value
        elif (self.var_size.get()).isnumeric()==False:
            self.lbl_msg.config(text="Size Must Be Integer.",fg="red")

        #executing the code
        else:
            file_name=str(self.var_filename.get())
            content=(f"\t\t\t{self.var_heading.get()}\n\n{self.var_content.get()}")
            # print(content)
            im_size=int(self.var_size.get())

            qr_img=qrcode.QRCode(version=1, box_size=im_size, border=int(im_size/10))
            qr_img.add_data(content)
            qr_img.make(fit=True)
            qr_img=qr_img.make_image(fill_color="black",back_color="white")
            file_name=str(self.var_filename.get())+'.png'
            # print(file_name)
            qr_img.save(file_name)

            #qr image
            qr_img=resizeimage.resize_cover(qr_img,[180,180])
            self.im=ImageTk.PhotoImage(qr_img)
            self.qr_code.config(image=self.im)

            
            #message
            self.msg="QR Image Saved Successfully."
            self.lbl_msg.config(text=self.msg,fg="green")

# main function
root=Tk()
obj=Qr_Generator(root)
root.mainloop()
# Aarsh Saxena 21bec001