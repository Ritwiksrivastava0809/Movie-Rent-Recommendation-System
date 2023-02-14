from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
import mysql.connector as connection

class register :

        def __init__(self,root) :
                
                self.root = root
                self.root.title("REGISTER")
                self.root.geometry("1550x800+0+0")    
                self.root.resizable(0, 0)
                self.root.state('zoomed')
                self.root.title('Regitration Page')

        #===============================================Variables==================================================== 
                
                self.var_fname = StringVar()
                self.var_lastname = StringVar()
                self.var_contact = StringVar()
                self.var_email = StringVar()
                self.var_security = StringVar()
                self.var_security_A = StringVar()
                self.var_pass = StringVar()
                self.var_confirm_pass = StringVar()
                
        #===============================================background Image==================================================== 

                self.bg = ImageTk.PhotoImage(file = r"C:\c++\My codes\python\project\movie rent system\photos\wp4770509-avengers-poster-wallpapers.jpg")
                lblbg = Label(self.root,image=self.bg)
                lblbg.place(x=0,y=0,relwidth=1,relheight=1)

        #===============================================Left Image==================================================== 

                self.bg1 = ImageTk.PhotoImage(file = r"C:\c++\My codes\python\project\movie rent system\photos\peakpx.jpg")
                lblleft = Label(self.root,image=self.bg1)
                lblleft.place(x=50,y=80,width=400,height=500)               

                frame = Frame(self.root,bg = 'lemon chiffon')
                frame.place(x=455,y=80,width=800,height=500)
                
                register_lbl = Label(frame,font = ('Georgia' , 18 , 'bold'),
                        fg = 'dark green', bg = 'lemon chiffon', text='REGISTER HERE')
                register_lbl.place(x = 20 , y = 20)
                
        #     # ===================================================================================================
        #     # ======================================Labels and Entry=============================================
        #     # ===================================================================================================        
                
                fname = Label(frame , text= 'First Name',font = ('Georgia' , 14,'bold'),
                        fg = 'black', bg = 'lemon chiffon')
                fname.place(x = 30 , y = 100)    
                
                self.fname_txt = ttk.Entry(frame,textvariable=self.var_fname,font = ('Georgia' , 10 ),background = 'lemon chiffon')
                self.fname_txt.place(x=30,y=130,width=250)
                
                
                lname = Label(frame , text= 'Last Name',font = ('Georgia' , 14,'bold'),
                        fg = 'black', bg = 'lemon chiffon')
                lname.place(x = 350 , y = 100)    
                
                self.lname_txt = ttk.Entry(frame,textvariable=self.var_lastname,font = ('Georgia' , 10 ),background = 'lemon chiffon')
                self.lname_txt.place(x=350,y=130,width=250)  
                
                
                contact= Label(frame , text= 'Contact No',font = ('Georgia' , 14,'bold'),
                        fg = 'black', bg = 'lemon chiffon')
                contact.place(x = 30 , y = 170)    
                
                self.contact_txt = ttk.Entry(frame,textvariable=self.var_contact,font = ('Georgia' , 10 ),background = 'lemon chiffon')
                self.contact_txt.place(x=30,y=200,width=250)
                
                
                email= Label(frame , text= 'Email ID',font = ('Georgia' , 14,'bold'),
                        fg = 'black', bg = 'lemon chiffon')
                email.place(x = 350 , y = 170)    
                
                self.email_txt = ttk.Entry(frame,font = ('Georgia' , 10 ),textvariable=self.var_email,background = 'lemon chiffon')
                self.email_txt.place(x=350,y=200,width=250)
                
                
                security= Label(frame , text= 'Select Security Question',font = ('Georgia' , 14,'bold'),
                        fg = 'black', bg = 'lemon chiffon')
                security.place(x = 30 , y = 240)    
                
                self.combo_security = ttk.Combobox(frame,textvariable=self.var_security
                                                ,font = ('Georgia' , 10 ),state='readonly',
                                                background = 'lemon chiffon')
                self.combo_security['values'] = ('Select',
                                                'Your birth place',
                                                'Your pet name',
                                                'Your girlfriend name')
                self.combo_security.place(x=30,y=272,width=250)
                self.combo_security.current(0)
                
                
                security_A = Label(frame , text= 'Security Answer',font = ('Georgia' , 14,'bold'),
                        fg = 'black', bg = 'lemon chiffon')
                security_A.place(x=350,y=240)
                
                self.security_txt = ttk.Entry(frame,textvariable=self.var_security_A,font = ('Georgia' , 10 ),background = 'lemon chiffon')
                self.security_txt.place(x=350,y=272,width=250)
                
                
                password= Label(frame ,text= 'Password',font = ('Georgia' , 14,'bold'),
                        fg = 'black', bg = 'lemon chiffon')
                password.place(x = 30 , y = 310)    
                
                self.password_txt = ttk.Entry(frame,textvariable=self.var_pass,font = ('Georgia' , 10 ),background = 'lemon chiffon')
                self.password_txt.place(x=30,y=350,width=250)
                
                
                confirm_password= Label(frame , text= 'Confirm Password',font = ('Georgia' , 14,'bold'),
                        fg = 'black', bg = 'lemon chiffon')
                confirm_password.place(x = 350 , y = 310)    
                
                self.confirm_password_txt = ttk.Entry(frame,textvariable=self.var_confirm_pass,font = ('Georgia' , 10 ),background = 'lemon chiffon')
                self.confirm_password_txt.place(x=350,y=350,width=250)
                
                self.var_check = IntVar()
                checkbtn = Checkbutton(frame ,text = 'I Agree The Terms & Condition',font = ('Georgia' , 10,'bold')
                                ,bg='lemon chiffon',onvalue=1,offvalue=0)
                checkbtn.place(x=30 ,y = 390)
                
        #     # ===================================================================================================
        #     # ======================================BUTTON=======================================================
        #     # ===================================================================================================    

                img = Image.open(r"C:\c++\My codes\python\project\movie rent system\photos\regbtn1.jpg")
                img = img.resize((150,50),Image.ANTIALIAS)
                self.photoimage = ImageTk.PhotoImage(img)
                registerbtn = Button(frame,command=self.register_data,image=self.photoimage,borderwidth=0,cursor='hand2',bg='lemon chiffon',
                                activebackground='lemon chiffon')
                registerbtn.place(x=20,y=430,width=200)
                
                img1 = Image.open(r"C:\c++\My codes\python\project\movie rent system\photos\sign in.jpg")
                img1 = img1.resize((200,40),Image.ANTIALIAS)
                self.photoimage1 = ImageTk.PhotoImage(img1)
                loginbtn = Button(frame,image=self.photoimage1,borderwidth=0,cursor='hand2',bg='lemon chiffon',
                                activebackground='lemon chiffon')
                loginbtn.place(x=330,y=430,width=200)
                
        #     # =================================================================================================================
        #     # ======================================Function Declaration=======================================================
        #     # =================================================================================================================   

        def  register_data (self) :
        
                if self.var_fname.get() == '' or self.var_email.get() == '' or self.var_security.get() == 'Select' :
                        messagebox.showerror('Error','All fields are required')
        
                elif self.var_pass.get()  != self.var_confirm_pass.get()  :
                        messagebox.showerror('Error','password and confirm password must be same')
                
                # elif self.var_check.get() == 0 :
                #         messagebox.showerror('Error','Please agree our terms and condition')
                
                else :
                        conn = connection.connect(host = "localhost",
                                                                user = "root",
                                                                passwd = "qwervbnm5",
                                                                database = "movie_rent")
                        curr = conn.cursor()
                        querry = ('select * from user_data where email = %s')
                        value = (self.var_email.get(),)
                        curr.execute(querry,value)
                        row = curr.fetchone()
                        
                        if row != None :
                                messagebox.showerror('Error','user already exist please try another email')
                        
                        else:
                                curr.execute('insert into user_data values(%s,%s,%s,%s,%s,%s,%s)',
                                                                                                (self.var_fname.get(),
                                                                                                self.var_lastname.get(),
                                                                                                self.var_contact.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_security.get(),
                                                                                                self.var_security_A.get(),
                                                                                                self.var_pass.get()))
                                conn.commit()
                                conn.close()
                                messagebox.showinfo('Success',"User registered successfully")
                                
                                
                        
                        



if __name__ == "__main__":
        root = Tk()
        ob = register(root)
        root.mainloop()
                
                