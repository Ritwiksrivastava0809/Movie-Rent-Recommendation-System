from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
from register import register
from main1 import movierentsystem
import mysql.connector as connection

def main() :
    win = Tk()
    app = login_window(win)
    win.mainloop()

class login_window :
    
    def __init__(self,root) :
    
        self.root = root
        self.root.title("LOGIN")
        self.root.geometry("1550x800+0+0")    
        self.root.resizable(0, 0)
        self.root.state('zoomed')
        self.root.title('Login Page')

# ========================================================================
# ============================background image============================
# ========================================================================
                
        self.bg = ImageTk.PhotoImage(file = r"C:\c++\My codes\python\project\movie rent system\photos\3658600.jpg")
        
        lblbg = Label(self.root,image=self.bg)
        lblbg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame = Frame(self.root,bg = 'light pink')
        frame.place(x=450,y=130,width=370,height=450)
        
#     # ========================================================================
#     # ========================================================================
#     # ========================================================================
            
        img1 = Image.open(r"C:\c++\My codes\python\project\movie rent system\photos\hyy.png")
        img1 = img1.resize((100,100) , Image.ANTIALIAS) #high level ki image ko level mein convert krta
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        lblimg1 = Label(image=self.photoimg1,bg='light pink',borderwidth=0,)
        lblimg1.place(x=580,y=135,width=110,height=100)
        
        get_str = Label(frame, text="WELCOME" , font = ('goudy old style',20,'bold'),fg='blue',bg='light pink')
        get_str.place(x=108,y=105)
        
#     # ====================================================================================
#     # ======================== Sign In label =============================================
#     # ====================================================================================

        usernamelbl = Label(frame,text='USERNAME', font = ('goudy old style',14,'bold'),fg='blue',bg='light pink')
        usernamelbl.place(x=50,y=165)
        
        self.txtusr = ttk.Entry(frame, font = ('goudy old style',14,'bold'))
        self.txtusr.place(x = 40 , y = 190 ,width= 270)
    

        passwordlbl = Label(frame,text='PASSWORD', font = ('goudy old style',14,'bold'),fg='blue',bg='light pink')
        passwordlbl.place(x=50,y=230)
        
        self.txtpassword = ttk.Entry(frame, font = ('goudy old style',14,'bold'))
        self.txtpassword.place(x = 40 , y = 260 ,width= 270)            
        
#     # ====================================================================================
#     # ======================== ICON IMAGES =============================================
#     # ====================================================================================        
        
        img2= Image.open(r"C:\c++\My codes\python\project\movie rent system\photos\username_icon.png")
        img2 = img2.resize((25,25) , Image.ANTIALIAS) #high level ki image ko level mein convert krta
        self.photoimg2 = ImageTk.PhotoImage(img2)
        
        lblimg2 = Label(image=self.photoimg2,bg='light pink',borderwidth=0,)
        lblimg2.place(x=470,y=295,width=25,height=25)        
        
        img3= Image.open(r"C:\c++\My codes\python\project\movie rent system\photos\password_icon.png")
        img3 = img3.resize((25,25) , Image.ANTIALIAS) #high level ki image ko level mein convert krta
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        lblimg3 = Label(image=self.photoimg3,bg='light pink',borderwidth=0,)
        lblimg3.place(x=470,y=365,width=25,height=25)        

#     # ========================================================================
#     # ============================login button================================
#     # ========================================================================        
        
        loginbtn = Button(frame ,command=self.login, bd =3 ,relief=RIDGE,fg='white',bg='maroon',
                        text= 'LOGIN' , font = ('goudy old style',14,'bold'),
                        activeforeground='white',
                        activebackground='maroon')
        loginbtn.place(x=110,y=310,width=120,height=25)
        
        registerbtn = Button(frame ,command=self.register_window, borderwidth=0 ,relief=RIDGE,fg='blue',bg='light pink',
                        text= 'New User Register' , font = ('goudy old style',12,'bold'),
                        activeforeground='blue',
                        activebackground='light pink')
        registerbtn.place(x=20,y=350,width=160)
        
        forgotpasswordbtn = Button(frame , borderwidth=0 ,relief=RIDGE,fg='blue',bg='light pink',
                        text= 'Forget Password' , font = ('goudy old style',12,'bold'),
                        activeforeground='blue',
                        activebackground='light pink')
        forgotpasswordbtn.place(x=12,y=380,width=160)
    
    def register_window (self) :
        self.new_window = Toplevel(self.root)
        self.app = register(self.new_window)
        # print('register page')
        
            
    def login(self) :
        if self.txtusr.get() == '' or self.txtpassword.get() == '' :
            messagebox.showerror('Error','all feilds required !')
        elif self.txtusr.get() == 'ritwik' and self.txtpassword.get() == 'srivastava' :
            messagebox.showinfo('Success','Welcome to my store')
        else :
            conn = connection.connect(host = "localhost",
                                                                user = "root",
                                                                passwd = "qwervbnm5",
                                                                database = "movie_rent")
            curr = conn.cursor()
            
            curr.execute('Select * from user_data where email =  %s and passsword = %s',(
                                                                                        self.txtusr.get(),
                                                                                        self.txtpassword.get()
                                                                                    )) 
            
            row = curr.fetchone()
            if row == None :
                messagebox.showerror('Error','Ivalid Username & Password')
            else :
                open_main = messagebox.askyesno("YesNo",'Acess Only Admin')
                if open_main > 0 :
                    self.new_window = Toplevel(self.root)
                    self.app = movierentsystem(self.new_window)
                else :
                    if not open_main :
                        return
            
            conn.commit()
            conn.close()                    
        
        
if __name__ == "__main__":
    main()
                
        
