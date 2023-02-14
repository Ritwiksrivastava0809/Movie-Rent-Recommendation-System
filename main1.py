from cProfile import label
from tkinter import *
from tkinter import ttk
import random
import pandas as pd
from recomender1 import recomender_system 
import datetime
import time
from tkinter import messagebox
import mysql.connector as connection

class movierentsystem : 
    
    def __init__(self, root):
        # this part creates the window of application from tkinter
        self.root = root
        self.root.title("MOVIE RENT SYSTEM")
        self.root.geometry("1550x800+0+0")
        self.root.resizable(0, 0)
        self.root.state('zoomed')
        self.root.title('OVIE RENT SYSTEM')        

    # this part is used to make title of the page
        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="MOVIE RENT SYSTEM",
                        fg="white", bg="maroon", font=("goudy old style", 40, "bold"), padx=2, pady=6)
        # to show title we have to pack the tilte
        lbltitle.pack(side=TOP, fill=X)    
        
    #==============================VARIABLES=============================
        self.movie = StringVar()
        self.custid_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.movieid_var = StringVar()
        self.movietiltle_var = StringVar()
        self.director_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.duedate_var = StringVar()
        self.daysonbook_var = StringVar()
        self.latereturnfine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.finallprice_var = StringVar()  
    # ===============================FRAMES==============================

        frame = Frame(self.root, bd=12, relief=RIDGE,
                    padx=20, bg="tan1")
        frame.place(x=0, y=110, width=1280, height=330)

    # ==========================DATA FRAME LEFT=============================

        Dataframeleft = LabelFrame(frame, text="Membership Information",
                                fg="maroon", bg="tan1", font=("goudy old style", 12, "bold"), bd=8)
        Dataframeleft.place(x=0, y=2, width=700, height=300)
        lblmember = Label(Dataframeleft,text="Movie",  font=("deja vu serif", 10, "bold"),
                        bg="tan1", padx=2, pady=5)
        lblmember.grid(row=0, column=0, sticky=W)
        txtmovie = Entry(Dataframeleft,textvariable=self.movie,font=("deja vu serif", 10, "bold"), width=29)
        txtmovie.grid(row=0, column=1)
        
          
        
        btnsearch = Button(Dataframeleft ,command= txtmovie.get(),text = 'search movies' , bg = 'coral3' , fg= 'white',
                        relief=RAISED,font=("times new india",10,"bold"),width=10,height=0,padx=2,pady=6)
        btnsearch.grid(row=0,column=2) 
        
        
        lblbookid = Label(Dataframeleft, text="Movie Id:",  font=("deja vu serif", 10, "bold"),
                        bg="tan1", padx=2, pady=5)
        lblbookid.grid(row=1, column=0, sticky=W)
        txtbookid = Entry(Dataframeleft,textvariable=self.movieid_var, font=("deja vu serif", 10, "bold"), width=29)
        txtbookid.grid(row=1, column=1)
    
        

        lblTitle = Label(Dataframeleft, text="ID NO.",  font=("deja vu serif", 10, "bold"),
                        bg="tan1", padx=2, pady=5)
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle = Entry(Dataframeleft,textvariable=self.custid_var,font=("deja vu serif", 10, "bold"), width=29)
        txtTitle.grid(row=2, column=1)

        lblfirstname = Label(Dataframeleft, text="FirstName",  font=("deja vu serif", 10, "bold"),
                            bg="tan1", padx=2, pady=5)
        lblfirstname.grid(row=3, column=0, sticky=W)
        txtfirstname = Entry(Dataframeleft, textvariable=self.firstname_var,font=(
            "deja vu serif", 10, "bold"), width=29)
        txtfirstname.grid(row=3, column=1)

        lbllastname = Label(Dataframeleft, text="Lastname",  font=("deja vu serif", 10, "bold"),
                            bg="tan1", padx=2, pady=5)
        lbllastname.grid(row=4, column=0, sticky=W)
        txtlastname = Entry(Dataframeleft,textvariable=self.lastname_var,font=(
            "deja vu serif", 10, "bold"), width=29)
        txtlastname.grid(row=4, column=1)

        lbladdress1 = Label(Dataframeleft, text="Address 1",  font=("deja vu serif", 10, "bold"),
                            bg="tan1", padx=2, pady=5)
        lbladdress1.grid(row=5, column=0, sticky=W)
        txtaddress1 = Entry(Dataframeleft, font=(
            "deja vu serif", 10, "bold"), width=29,textvariable=self.address1_var)
        txtaddress1.grid(row=5, column=1)

        lbladdress2 = Label(Dataframeleft, text="Address 2",  font=("deja vu serif", 10, "bold"),
                            bg="tan1", padx=2, pady=5)
        lbladdress2.grid(row=6, column=0, sticky=W)
        txtaddress2 = Entry(Dataframeleft, font=(
            "deja vu serif", 10, "bold"), width=29,textvariable=self.address2_var)
        txtaddress2.grid(row=6, column=1)

        lblpostcode = Label(Dataframeleft, text="Post Code",  font=("deja vu serif", 10, "bold"),
                            bg="tan1", padx=2, pady=5)
        lblpostcode.grid(row=7, column=0, sticky=W)
        txtpostcode = Entry(Dataframeleft, font=(
            "deja vu serif", 10, "bold"), width=29,textvariable=self.postcode_var)
        txtpostcode.grid(row=7, column=1)

        lblmobile = Label(Dataframeleft, text="Mobile No.",  font=("deja vu serif", 10, "bold"),
                        bg="tan1", padx=2, pady=5)
        lblmobile.grid(row=8, column=0, sticky=W)
        txtmobile = Entry(Dataframeleft, font=("deja vu serif", 10, "bold"),textvariable=self.mobile_var,width=29)
        txtmobile.grid(row=8, column=1)


        lblbooktitle = Label(Dataframeleft, text="Movie Title:",  font=("deja vu serif", 10, "bold"),
                    bg="tan1", padx=2, pady=5)
        lblbooktitle.grid(row=1, column=2, sticky=W)
        txtbooktitle = Entry(Dataframeleft, textvariable=self.movietiltle_var,font=("deja vu serif", 10, "bold"), width=29)
        txtbooktitle.grid(row=1, column=3)

        lblauthorname = Label(Dataframeleft, text="Director Name:",  font=("deja vu serif", 10, "bold"),
                        bg="tan1", padx=2, pady=5)
        lblauthorname.grid(row=2, column=2, sticky=W)
        txtAuthorname= Entry(Dataframeleft,textvariable=self.director_var, font=("deja vu serif", 10, "bold"), width=29)
        txtAuthorname.grid(row=2, column=3)

        lbldateborrowed= Label(Dataframeleft, text="Date Borrowed:",  font=("deja vu serif", 10, "bold"),
                            bg="tan1", padx=2, pady=5)
        lbldateborrowed.grid(row=3, column=2, sticky=W)
        txtdatebarrowed = Entry(Dataframeleft,textvariable=self.dateborrowed_var,font=(
            "deja vu serif", 10, "bold"), width=29)
        txtdatebarrowed.grid(row=3, column=3)

        lblDuedate = Label(Dataframeleft, text="Due Date:",  font=("deja vu serif", 10, "bold"),
                            bg="tan1", padx=2, pady=5)
        lblDuedate.grid(row=4, column=2, sticky=W)
        txtduedate = Entry(Dataframeleft,textvariable=self.duedate_var,font=(
            "deja vu serif", 10, "bold"), width=29)
        txtduedate.grid(row=4, column=3)

        lbldaysonbook = Label(Dataframeleft, text="Days on Book:",  font=("deja vu serif", 10, "bold"),
                            bg="tan1", padx=2, pady=5)
        lbldaysonbook.grid(row=5, column=2, sticky=W)
        txtdaysonbook = Entry(Dataframeleft,textvariable=self.daysonbook_var,font=(
            "deja vu serif", 10, "bold"), width=29)
        txtdaysonbook.grid(row=5, column=3)

        lbllatereturn = Label(Dataframeleft, text="Late Return Fine:",  font=("deja vu serif", 10, "bold"),
                            bg="tan1", padx=2, pady=5)
        lbllatereturn.grid(row=6, column=2, sticky=W)
        txtlatereturn = Entry(Dataframeleft,textvariable=self.latereturnfine_var,font=(
            "deja vu serif", 10, "bold"), width=29)
        txtlatereturn.grid(row=6, column=3)

        lbldateoverdue = Label(Dataframeleft, text="Date Over Due:",  font=("deja vu serif", 10, "bold"),
                            bg="tan1", padx=2, pady=5)
        lbldateoverdue.grid(row=7, column=2, sticky=W)
        txtdateoverdue = Entry(Dataframeleft,textvariable=self.dateoverdue_var,font=(
            "deja vu serif", 10, "bold"), width=29)
        txtdateoverdue.grid(row=7, column=3)

        lblactualprice = Label(Dataframeleft, text="Actual Price:",  font=("deja vu serif", 10, "bold"),
                        bg="tan1", padx=2, pady=5)
        lblactualprice.grid(row=8, column=2, sticky=W)
        txtactualprice = Entry(Dataframeleft,textvariable=self.finallprice_var,font=("deja vu serif", 10, "bold"), width=29)
        txtactualprice.grid(row=8, column=3)   

   # =========================BUTTON FRAMES===========================

        Buttonframe = Frame(self.root, bg="coral3", bd=10, relief=RIDGE)
        Buttonframe.place(x=0, y=440, width=1280, height=60)
        
        btnadddata = Button(Buttonframe,command=self.iadddata,text="Add Data",bg="coral3",
                            fg="white",relief=RIDGE,font=("times new india",13,"bold"),width=20,height=0,padx=2,pady=6)
        btnadddata.grid(row=0,column=0)
  
        btnshowdata = Button(Buttonframe,command=self.SHOW_DATA,text="ShowData",bg="coral3"
                            ,fg="white",relief=RIDGE,font=("times new india",13,"bold"),width=20,height=0,padx=2,pady=6)
        btnshowdata.grid(row=0,column=1)
        
        
        btnupdate = Button(Buttonframe,command=self.update_data,text="Update Data",bg="coral3",
                            fg="white",relief=RIDGE,font=("times new india",13,"bold"),width=20,height=0,padx=2,pady=6)
        btnupdate.grid(row=0,column=3)
                
        
        btndelete = Button(Buttonframe,command=self.delete_data,text="Delete",bg="coral3",
                            fg="white",relief=RIDGE,font=("times new india",13,"bold"),width=19,height=0,padx=2,pady=6)
        btndelete.grid(row=0,column=4)
        
        
        btnclear = Button(Buttonframe,command=self.iclear,text="Reset",bg="coral3",fg="white",
                            relief=RIDGE,font=("times new india",13,"bold"),width=20,height=0,padx=2,pady=6)
        btnclear.grid(row=0,column=5)
        
        
        btnexit = Button(Buttonframe,command=self.iExit,text="Exit",bg="coral3",fg="white",
                            relief=RIDGE,font=("times new india",13,"bold"),width=20,height=0,padx=2,pady=6)
        btnexit.grid(row=0,column=6) 

        
        def search():
            
            listmovies = []

            x = txtmovie.get()
            msr = recomender_system()
            
            temp = msr.recomend(x)
            
            for i in range(len(temp)):
                listmovies.append(temp[i]) 
            print("values:: ", listmovies) 
            
            df = pd.read_csv('C:\c++\My codes\python\project\movie rent system\data\movies.csv')
            df2 = df[df['original_title'].isin(listmovies)]
            
            def selectbook(event="") :
                values = str(list_box.get(list_box.curselection()))
                x= values
                z = df2.index[df2['original_title']==x].tolist()
                a = int(z[0])                
                id = df2._get_value(a,'id')
                self.movieid_var.set(id)
                self.movietiltle_var.set(values)
                z = df2.index[df2['original_title']==x].tolist()
                a = int(z[0])
                director = df2._get_value(a,'director')
                self.director_var.set(director)
        
                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                                
                self.dateborrowed_var.set(d1)
                self.duedate_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs 50")
                self.dateoverdue_var.set("no")
                self.finallprice_var.set("Rs 750")                
                
                
            
            list_box = Listbox(Dataframeright,font=("deja vu serif", 10, "bold"),width=20,height=15) 
            list_box.bind("<<ListboxSelect>>",selectbook)
            list_box.grid(row=0,column=0,padx=4)
            listscrollbar.config(command=list_box.yview)
        
            for item in listmovies :
                list_box.insert(END,item)  
            
            
        
                                        
        btnsearch = Button(Dataframeleft ,command=search,text = 'search movies' , bg = 'coral3' , fg= 'white',
                        relief=RAISED,font=("times new india",10,"bold"),width=10,height=0,padx=2,pady=6)
        btnsearch.grid(row=0,column=2) 
        
    
    # =========================DETAILS FRAMES===========================

        Detailsframe = Frame(self.root, bd=10, bg="coral3", relief=RIDGE)
        Detailsframe.place(x=0, y=500, width=1280, height=190)
        
        table_frame = Frame(Detailsframe,bd=6,relief=RIDGE,bg="coral3")
        table_frame.place(x=0,y=2,width=1260,height=165)
        
        scroll_x = ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.movie_data = ttk.Treeview(Detailsframe,columns=("id_no","fname","lname","add1","add2",
                                                            "post_code","mobile_no","movie_id","movie_title","director","date_borrowed","due_date","days","fine",
                                                            "date_overdue","final_price"),
                                                            xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.movie_data.xview)
        scroll_y.config(command=self.movie_data.yview)

        self.movie_data.heading("id_no", text="ID NO")        
        self.movie_data.heading("fname", text="First Name")
        self.movie_data.heading("lname", text="Last Name")
        self.movie_data.heading("add1", text="Address 1")
        self.movie_data.heading("add2", text="Address 2")
        self.movie_data.heading("post_code", text="Post Id.")
        self.movie_data.heading("mobile_no", text="Mobile")
        self.movie_data.heading("movie_id", text="Movie Id.")
        self.movie_data.heading("movie_title", text="MOvie Title")
        self.movie_data.heading("director", text="Director")
        self.movie_data.heading("date_borrowed", text="Date Borrowed")
        self.movie_data.heading("due_date", text="Date Due")
        self.movie_data.heading("days", text="Days")
        self.movie_data.heading("fine", text="Late Return Fine")
        self.movie_data.heading("date_overdue", text="Date Overdue ")
        self.movie_data.heading("final_price", text="Final Price")
        
        self.movie_data["show"] = "headings"
        self.movie_data.pack(fill=BOTH,expand=1)
        

        self.movie_data.column("id_no", width=100)        
        self.movie_data.column("fname", width=100)
        self.movie_data.column("lname", width=100)
        self.movie_data.column("add1", width=100)
        self.movie_data.column("add2", width =100)
        self.movie_data.column("post_code", width=100)
        self.movie_data.column("mobile_no", width=100)
        self.movie_data.column("movie_id", width=100)
        self.movie_data.column("movie_title",width=100)
        self.movie_data.column("director", width=100)
        self.movie_data.column("date_borrowed", width=100)
        self.movie_data.column("due_date", width=100)
        self.movie_data.column("days", width=100)
        self.movie_data.column("fine", width=100)
        self.movie_data.column("date_overdue", width=100)
        self.movie_data.column("final_price", width=100)
        
        self.movie_data.bind("<ButtonRelease-1>",self.get_cursor) 
        self.show_data()

    # ==========================DATA FRAME RIGHT =============================    

        Dataframeright = LabelFrame(frame, text="Recomended Movies", fg="maroon", bg="coral3", font=(
            "goudy old style", 12, "bold"), bd=8)
        Dataframeright.place(x=705, y=2, width=522, height=300)
    
        self.txtbox = Text(Dataframeright,font=("deja vu serif", 10, "bold"),width=46,height=15,padx=5,pady=5)
        self.txtbox.grid(row=0,column=3)
        listscrollbar = Scrollbar(Dataframeright)
        listscrollbar.grid(row=0,column=1,sticky="ns")

    #=========================FUNCTIONALITY DECLARATION=====================
        
    def iadddata(self) :
        if  self.custid_var.get() == "" or self.movieid_var.get() == "" :
            messagebox.showerror("Error","All feilds are required")
        else :
            conn = connection.connect(host = "localhost",
                                                        user = "root",
                                                        passwd = "qwervbnm5",
                                                        database = "movie_rent")
            
            my_cursor = conn.cursor()
            query = "INSERT INTO movie_data values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (
                    self.custid_var.get(),
                    self.firstname_var.get(),
                    self.lastname_var.get(),
                    self.address1_var.get(),
                    self.address2_var.get(),
                    self.postcode_var.get(),
                    self.mobile_var.get(),
                    self.movieid_var.get(),
                    self.movietiltle_var.get(),
                    self.director_var.get(),
                    self.dateborrowed_var.get(),
                    self.duedate_var.get(),
                    self.daysonbook_var.get(),
                    self.latereturnfine_var.get(),
                    self.dateoverdue_var.get(),
                    self.finallprice_var.get()
                    )
            my_cursor.execute(query, val)   
            conn .commit()
            self.show_data()
            conn.close()
            messagebox.showinfo("SUCCESS","Record has been inserted")
            
    def show_data(self) :
    
            conn = connection.connect(host = "localhost",
                                                        user = "root",
                                                        passwd = "qwervbnm5",
                                                        database = "movie_rent")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM  movie_data")
            rows = my_cursor.fetchall()
            if len(rows) != 0 :
                self.movie_data.delete(*self.movie_data.get_children())
                for i in rows :
                    self.movie_data.insert("",END,values=i)
                conn.commit()
            conn.close()    

    def delete_data(self) :
            if  self.custid_var.get() == "" or self.movieid_var.get() == "" :
                messagebox.showerror("Error","All feilds are required")
            else :    
                    conn = connection.connect(host = "localhost",
                                                                user = "root",
                                                                passwd = "qwervbnm5",
                                                                database = "movie_rent")
                    
                    my_cursor = conn.cursor()
                    query = "DELETE FROM movie_data where id_no = %s"
                    value = (self.custid_var.get(),)
                    my_cursor.execute(query,value)            
                    conn.commit()
                    self.show_data()
                    conn.close()   
                    messagebox.showinfo("Delete","Entry has been deleted successfully")   
                    
                                
    def get_cursor(self,event = "") :
            cursor_row = self.movie_data.focus()
            content = self.movie_data.item(cursor_row)
            row = content["values"]       
            self.custid_var.set(row[0])
            self.firstname_var.set(row[1])
            self.lastname_var.set( row[2])
            self.address1_var.set( row[3])
            self.address2_var.set(row[4] )
            self.postcode_var.set( row[5])
            self.mobile_var.set(row[6])
            self.movieid_var.set(row[7])
            self.movietiltle_var.set(row[8])
            self.director_var.set(row[9])
            self.dateborrowed_var.set(row[10])
            self.duedate_var.set(row[11])
            self.daysonbook_var.set(row[12])
            self.latereturnfine_var.set(row[13])
            self.dateoverdue_var.set(row[14])
            self.finallprice_var.set(row[15])
    
    def SHOW_DATA(self) :
        self.txtbox.insert(END,"ID_NO :: \t\t\t" + self.custid_var.get() + "\n" )     
        self.txtbox.insert(END,"Fisrt Name :: \t\t\t" + self.firstname_var.get() + "\n" )  
        self.txtbox.insert(END,"Last Name :: \t\t\t" + self.lastname_var.get() + "\n" )
        self.txtbox.insert(END,"Address 1 :: \t\t\t" + self.address1_var.get() + "\n" )                    
        self.txtbox.insert(END,"Address 2 :: \t\t\t" + self.address2_var.get() + "\n" )
        self.txtbox.insert(END,"Post code :: \t\t\t" + self.postcode_var.get() + "\n" )
        self.txtbox.insert(END,"Mobile :: \t\t\t" + self.mobile_var.get() + "\n" )
        self.txtbox.insert(END,"Movie Id :: \t\t\t" + self.movieid_var.get() + "\n" )
        self.txtbox.insert(END,"Movie Title :: \t\t\t" + self.movietiltle_var.get() + "\n" )
        self.txtbox.insert(END,"Director :: \t\t\t" + self.director_var.get() + "\n" )
        self.txtbox.insert(END,"Date Borrowed :: \t\t\t" + self.dateborrowed_var.get() + "\n" )
        self.txtbox.insert(END,"Due Date :: \t\t\t" + self.duedate_var.get() + "\n" )
        self.txtbox.insert(END,"Days :: \t\t\t" + self.daysonbook_var.get() + "\n" )
        self.txtbox.insert(END,"Late return fine :: \t\t\t" + self.latereturnfine_var.get() + "\n" )
        self.txtbox.insert(END,"Over Duedate:: \t\t\t" + self.dateoverdue_var.get() + "\n" )
        self.txtbox.insert(END,"Final Price :: \t\t\t" + self.finallprice_var.get() + "\n" )    


    def iclear(self) :
        self.custid_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.postcode_var.set("")
        self.mobile_var.set("")
        self.movieid_var.set("")
        self.movietiltle_var.set("")
        self.dateborrowed_var.set("")
        self.duedate_var.set("") 
        self.director_var.set("")
        self.latereturnfine_var.set("")  
        self.daysonbook_var.set("")
        self.dateoverdue_var.set("")   
        self.finallprice_var.set("")     
        self.txtbox.delete("1.0",END)  

    def update_data(self) :
            conn = connection.connect(host = "localhost",
                                                        user = "root",
                                                        passwd = "qwervbnm5",
                                                        database = "movie_rent")
            
            my_cursor = conn.cursor()
            my_cursor.execute(
                                            "UPDATE movie_data set movie_title =%s, fname = %s, lname =%s, add1 = %s, add2 = %s, post_code = %s, mobile_no = %s where id_no = %s",
                                                (   self.movietiltle_var.get()
                                                    ,self.firstname_var.get()
                                                    ,self.lastname_var.get()
                                                    ,self.address1_var.get()
                                                    ,self.address2_var.get()
                                                    ,self.postcode_var.get()
                                                    ,self.mobile_var.get()
                                                    ,self.custid_var.get()
                                                )
                                            )
                        
            conn.commit()
            conn.close()
            self.show_data()
            messagebox.showinfo("SUCCESS","Record has been updated successfully")  
    
    def iExit(self) :
        iExit = messagebox.askyesno("Movie Rent System","Confirm you want to exit")
        if  iExit >0 :
            root.destroy()
            return  
        
if __name__ == "__main__":
    # name = input("enter movie name :")
    root = Tk()
    ob = movierentsystem(root)
    root.mainloop()
        