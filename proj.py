from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

class Login:
   def __init__(self,root):
      self.root=root
      self.root.title("Login and registration")
      self.root.geometry("1250x700")
      self.root.resizable(False,False)
      self.loginform()

   def loginform(self):
      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=700,width=1250)
      self.img=ImageTk.PhotoImage(file="background.png")
      img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1250,height=700)
      frame_input=Frame(self.root,bg='white')
      frame_input.place(x=420,y=130,height=450,width=350)

      label1=Label(frame_input,text="Login Here",font=('impact',32,'bold'),fg="black",bg='white')
      label1.place(x=75,y=20)

      label2=Label(frame_input,text="Username",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
      label2.place(x=30,y=95)

      self.email_txt=Entry(frame_input,font=("times new roman",15,"bold"), bg='lightgray')
      self.email_txt.place(x=30,y=145,width=270,height=35)

      label3=Label(frame_input,text="Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
      label3.place(x=30,y=195)

      self.password=Entry(frame_input,font=("times new roman",15,"bold"), bg='lightgray')
      self.password.place(x=30,y=245,width=270,height=35)
   
      btn1=Button(frame_input,text="forgot password?",command=self.forget_password_window,cursor="hand2",
                  font=('calibri',10),bg='white',fg='black',bd=0)
      btn1.place(x=125,y=305)

      btn2=Button(frame_input,text="Login",command=self.login,
                  font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
      btn2.place(x=90,y=340)

      btn3=Button(frame_input,command=self.Register,text="Not Registered?register"
                  ,cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)

      btn3.place(x=110,y=390)

   def login(self):

      if self.email_txt.get()=="" or self.password.get()=="":
         messagebox.showerror("Error","All fields are required",parent=self.root)

      else:
         try:
            con=pymysql.connect(host='localhost',user='root',password='root',database='mydatabase')
            cur=con.cursor()
            cur.execute('select * from register where emailid=%s and password=%s'
                        ,(self.email_txt.get(),self.password.get()))
            row=cur.fetchone()

            if row==None:
               messagebox.showerror('Error','Invalid Username And Password',parent=self.root)
               self.logclear()
               self.email_txt.focus()

            else:

               self.appscreen()
               con.close()

         except Exception as es:

            messagebox.showerror('Error',f'Error Due to : {str(es)}' ,parent=self.root)
         

   def Register(self):

      Frame_login1=Frame(self.root,bg="white")
      Frame_login1.place(x=0,y=0,height=700,width=1250)
      self.img=ImageTk.PhotoImage(file="background.png")
      img=Label(Frame_login1,image=self.img).place(x=0,y=0,width=1250,height=700)
      frame_input2=Frame(self.root,bg='white')
      frame_input2.place(x=320,y=130,height=450,width=630)
      
      label1=Label(frame_input2,text="Register Here",font=('impact',32,'bold'), fg="black",bg='white')
      label1.place(x=45,y=20)
      
      label2=Label(frame_input2,text="Username",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
      label2.place(x=30,y=95)

      self.entry=Entry(frame_input2,font=("times new roman",15,"bold"),  bg='lightgray')
      self.entry.place(x=30,y=145,width=270,height=35)
      
      label3=Label(frame_input2,text="Password",font=("Goudy old style",20,"bold"), fg='orangered',bg='white')
      label3.place(x=30,y=195)

      self.entry2=Entry(frame_input2,font=("times new roman",15,"bold"), bg='lightgray')
      self.entry2.place(x=30,y=245,width=270,height=35)
      
      label4=Label(frame_input2,text="Email-id",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
      label4.place(x=330,y=95)

      self.entry3=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')
      self.entry3.place(x=330,y=145,width=270,height=35)

      label5=Label(frame_input2,text="Confirm Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
      label5.place(x=330,y=195)
      self.entry4=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')
      self.entry4.place(x=330,y=245,width=270,height=35)

      btn2=Button(frame_input2,command=self.register,text="Register"
                  ,cursor="hand2",font=("times new roman",15),fg="white", bg="orangered",bd=0,width=15,height=1)

      btn2.place(x=220,y=340)

      btn3=Button(frame_input2,command=self.loginform,

                  text="Already Registered?Login",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)

      btn3.place(x=240,y=390)
   

   def register(self):

      if self.entry.get()==""or self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()=="":
         messagebox.showerror("Error","All Fields Are Required",parent=self.root)

      elif self.entry2.get()!=self.entry4.get():
         messagebox.showerror("Error","Password and Confirm Password Should Be Same" ,parent=self.root)

      else:
         try:

            con=pymysql.connect(host="localhost",user="root",password="root", database="mydatabase")
            cur=con.cursor()
            cur.execute("select * from register where emailid=%s",self.entry3.get())
            row=cur.fetchone()

            if row!=None:
               messagebox.showerror("Error","User already Exist,Please try with another Email" ,parent=self.root)
               self.regclear()
               self.entry.focus()

            else:

               cur.execute("insert into register values(%s,%s,%s,%s)"
                           ,(self.entry.get(),self.entry3.get(),self.entry2.get(),self.entry4.get()))
               con.commit()
               con.close()
               messagebox.showinfo("Success","Register Succesfull",parent=self.root)
               self.regclear()

         except Exception as es:
            messagebox.showerror("Error",f"Error due to:{str(es)}" ,parent=self.root)

   def forget_password(self):
      if self.txt_new_pass.get()=="" or self.txt_con_pass.get()=="":
         messagebox.showerror("Error","All fields required",parent=self.root2)
      elif self.txt_new_pass.get()!=self.txt_con_pass.get():
         messagebox.showerror("Error","New Password and Re-type Password Should Be Same" ,parent=self.root2)
      else:
         try:
            con=pymysql.connect(host='localhost',user='root',password='root',database='mydatabase')
            cur=con.cursor()
            cur.execute('update register set password=%s,confirm_password=%s where emailid=%s ',(self.txt_new_pass.get(),self.txt_new_pass.get(),self.email_txt.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success","Your password has reset successfully",parent=self.root2)
               
         except Exception as es:
            messagebox.showerror('Error',f'Error Due to : {str(es)}' ,parent=self.root)

   def forget_password_window(self):
      if self.email_txt.get()=="":
         messagebox.showerror("Error","Please enter email to reset your password",parent=self.root)
      else:
         try:

            con=pymysql.connect(host='localhost',user='root',password='root',database='mydatabase')
            cur=con.cursor()
            cur.execute('select * from register where emailid=%s',self.email_txt.get())
            row=cur.fetchone()

            if row==None:

               messagebox.showerror('Error','Please enter valid email address to reset your password',parent=self.root)

            else:
               #con.close()
               self.root2=Toplevel()
               self.root2.title("Forget Password")
               self.root2.geometry("350x350+100+50")
               self.root2.config(bg="white")
               self.root2.focus_force()
               self.root2.grab_set()

               t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"))
               new_password=Label(self.root2,text="Create New password",font=("times new roman",15,"bold"),bg="white")
               new_password.place(x=80,y=70)
               self.txt_new_pass=Entry(self.root2,font=("times new roman",15),bg="lightgray")
               self.txt_new_pass.place(x=80,y=100,width=190)   

               con_password=Label(self.root2,text="Re-type New password",font=("times new roman",15,"bold"),bg="white")
               con_password.place(x=80,y=140)
               self.txt_con_pass=Entry(self.root2,font=("times new roman",15),bg="lightgray")
               self.txt_con_pass.place(x=80,y=170,width=190)  

               btn_change_password=Button(self.root2,text="Reset",command=self.forget_password,bg="green",fg="white",font=("times new roman",15,"bold"))
               btn_change_password.place(x=140,y=250)
            
         except Exception as es:
            messagebox.showerror('Error',f'Error Due to : {str(es)}' ,parent=self.root)
         

   def appscreen(self):
      Frame_login=Frame(self.root,bg="white")

      Frame_login.place(x=0,y=0,height=700,width=1250)

      label1=Label(Frame_login,text="Hi! Welcome To my page"
                   ,font=('times new roman',32,'bold'),fg="black",bg='white')
      label1.place(x=375,y=100)

      label2=Label(Frame_login,text="Have a nice day...!!!"
                   ,font=('times new roman',32,'bold'),fg="black",bg='white')
      label2.place(x=450,y=160)

      btn2=Button(Frame_login,text="Logout",command=self.loginform,cursor="hand2",
                  font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)

      btn2.place(x=1000,y=10)
      self.img=ImageTk.PhotoImage(file="smily.jfif")
      img=Label(Frame_login,image=self.img)
      img.place(x=440,y=230)

   def regclear(self):
      self.entry.delete(0,END)
      self.entry2.delete(0,END)
      self.entry3.delete(0,END)
      self.entry4.delete(0,END)
      
   def logclear(self):
      self.email_txt.delete(0,END)
      self.password.delete(0,END)

root=Tk()
ob=Login(root)
root.mainloop()
