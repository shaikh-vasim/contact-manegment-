from tkinter import *
from tkinter import ttk
import pymysql
import tkinter.messagebox as tmsg


class student:

    def __init__(self, root):
        self.root = root
        self.root.title("Contact _manegment_System")
        self.root.geometry("1010x700+180+0")
        self.root.maxsize(1010, 700)
        self.root.minsize(1010, 700)

        self.root.wm_iconbitmap("./contact_people.ico")

        # All variable
        self.Roll_No_var = StringVar()
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Gender_var = StringVar()
        self.Contact_var = StringVar()
        self.dob_var = StringVar()

        self.search_by = StringVar()
        self.search_text = StringVar()
        self.search_text2 = StringVar()

        Frem_title = Label(self.root, text="Contact Manegment System", font=(
            "times new roman", "40", "bold"), bg="green", fg="white", bd=10, relief=SUNKEN).pack(side=TOP, fill=X)

        ###################### ---manneg fram---####################################
        M_fram = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        M_fram.place(x=16, y=100, width=390, height=575)

        m_title = Label(M_fram, text="Manege Contact", font=(
            "time new roman", "25", "bold"), bg="crimson", fg="white").grid(row=0, columnspan=2, pady=10)

        roll = Label(M_fram, text="Sr No.", font=("time new roman", "18", "bold"),
                     bg="crimson", fg="white").grid(row=1, column=0, pady=10, sticky=W)
        textroll = Entry(M_fram, textvar=self.Roll_No_var, font=("time new roman", "15", "bold"),
                         bg="white", bd=4, relief=GROOVE).grid(row=1, column=1, pady=10, sticky="w")

        Name = Label(M_fram, text="Name", font=("time new roman", "18", "bold"),
                     bg="crimson", fg="white").grid(row=2, column=0, pady=10, sticky=W)
        textname = Entry(M_fram, textvar=self.Name_var, font=("time new roman", "15", "bold"),
                         bg="white", bd=4, relief=GROOVE).grid(row=2, column=1, pady=10, sticky="w")

        Email = Label(M_fram, text="Email.", font=("time new roman", "18", "bold"),
                      bg="crimson", fg="white").grid(row=3, column=0, pady=10, sticky=W)
        textemail = Entry(M_fram, textvar=self.Email_var, font=("time new roman", "15", "bold"),
                          bg="white", bd=4, relief=GROOVE).grid(row=3, column=1, pady=10, sticky="w")

        Gender = Label(M_fram, text="Gender", font=("time new roman", "18", "bold"),
                       bg="crimson", fg="white").grid(row=4, column=0, pady=10, sticky=W)
        comdo_box = ttk.Combobox(M_fram, textvar=self.Gender_var, font=(
            "time new roman", "14", "bold"), state="readonly")
        comdo_box["values"] = ("Male", "Female", "Other")
        comdo_box.grid(row=4, column=1, pady=10, sticky=W)

        Contact = Label(M_fram, text="Contact", font=("time new roman", "18", "bold"),
                        bg="crimson", fg="white").grid(row=5, column=0, pady=10, sticky=W)
        textcontact = Entry(M_fram, textvar=self.Contact_var, font=("time new roman", "15", "bold"),
                            bg="white", bd=4, relief=GROOVE).grid(row=5, column=1, pady=10, sticky="w")

        dob = Label(M_fram, text="D.O.B", font=("time new roman", "18", "bold"),
                    bg="crimson", fg="white").grid(row=6, column=0, pady=10, sticky=W)
        textdob = Entry(M_fram, textvar=self.dob_var, font=("time new roman", "15", "bold"),
                        bg="white", bd=4, relief=GROOVE).grid(row=6, column=1, pady=10, sticky="w")

        address = Label(M_fram, text="Address", font=("time new roman", "18", "bold"),
                        bg="crimson", fg="white",).grid(row=7, column=0, pady=10, sticky=W)
        self.text_Address = Text(M_fram, height=4, width=28, font=(
            "time new roman", "11", "bold"))
        self.text_Address.grid(row=7, column=1, sticky="w")

        ##################Buttanfrem==========######

        B_fram = Frame(M_fram, bd=4, relief=RIDGE, bg="crimson")
        B_fram.place(x=10, y=500, width=370)

        addButoon = Button(B_fram, text="Add", width=8, font="10", command=self.add_students).grid(
            row=0, column=0, sticky="w", padx=4, pady=4)
        updateButoon = Button(B_fram, text="Update", width=8, font="10", command=self.update).grid(
            row=0, column=1, sticky="w", padx=4, pady=4)
        deleteButoon = Button(B_fram, text="Delete", width=8, font="10", command=self.delete).grid(
            row=0, column=2, sticky="w", padx=4, pady=4)
        clearButoon = Button(B_fram, text="Clear", width=8, font="10", command=self.clear).grid(
            row=0, column=3, sticky="w", padx=3, pady=4)

        ##################Buttanfrem==========#####33############################################

        ###################### ---manneg fram---####################################

        D_fram = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        D_fram.place(x=430, y=100, width=570, height=575)
        #
        search = Label(D_fram, text="Search By", font=("time new roman", "13", "bold"), bg="crimson",
                       fg="white", textvar=self.search_by).grid(row=0, column=0, padx=5, pady=10, sticky=W)
        comdo_box = ttk.Combobox(D_fram, font=(
            "time new roman", "10"), state="readonly", width=13)
        comdo_box["values"] = ("Sr_no.")
        comdo_box.grid(row=0, column=1, pady=10, sticky=W)
        search2 = Label(D_fram, text="Search By", font=("time new roman", "13", "bold"), bg="crimson",
                        fg="white", textvar=self.search_by).grid(row=0, column=0, padx=5, pady=10, sticky=W)
        comdo_box2 = ttk.Combobox(D_fram, font=(
            "time new roman", "10"), state="readonly", width=13)
        comdo_box2["values"] = ("Name")
        comdo_box2.grid(row=1, column=1, pady=10, sticky=W)

        textsearch = Entry(D_fram, font=("time new roman", "12"), bg="white", bd=4, relief=GROOVE,
                           width=15, textvar=self.search_text).grid(row=0, column=3, padx=10, sticky="w")
        searchButoon = Button(D_fram, text="Search", width=8, font="4",
                              command=self.search_data_roll_no).grid(row=0, column=4, sticky="w", padx=5)
        showallButoon = Button(D_fram, text="Show All", width=8, font="4", command=self.fetch_data).grid(
            row=0, column=5, sticky="w", padx=5, pady=10)

        textsearch1 = Entry(D_fram, font=("time new roman", "12"), bg="white", bd=4, relief=GROOVE,
                            width=15, textvar=self.search_text2).grid(row=1, column=3, padx=10, sticky="w")
        searchButoon1 = Button(D_fram, text="Search", width=8, font="4",
                               command=self.search_data_name).grid(row=1, column=4, sticky="w", padx=5)

        ###################### ---manneg fram---####################################

        ###################### --Table fram---####################################

        T_fram = Frame(D_fram, bd=4, relief=RIDGE, bg="crimson")
        T_fram.place(x=10, y=90, width=543, height=455)

        scroll_x = Scrollbar(T_fram, orient=HORIZONTAL)
        scroll_y = Scrollbar(T_fram, orient=VERTICAL)
        self.Student_table = ttk.Treeview(T_fram, columns=(
            "roll", "name", "email", "gender", "contact", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.configure(command=self.Student_table.xview)
        scroll_y.configure(command=self.Student_table.yview)
        self.Student_table.heading("roll", text="Sr no.")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="D.O.B")
        self.Student_table.heading("address", text="Address")
        self.Student_table["show"] = "headings"
        self.Student_table.column("roll", width=120)
        self.Student_table.column("name", width=120)
        self.Student_table.column("email", width=120)
        self.Student_table.column("gender", width=120)
        self.Student_table.column("contact", width=120)
        self.Student_table.column("dob", width=120)
        self.Student_table.column("address", width=170)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_students(self):
        if self.Roll_No_var.get() == "" or self.Name_var.get() == "" or self.Email_var.get() == "" or self.Gender_var.get() == "" or self.Contact_var.get() == "" or self.dob_var.get() == "":
            tmsg.showinfo("Error", "All Filds are required ..!!!")

        else:

            con = pymysql.connect(
                host="localhost", user="root", password="", database="std")
            cur = con.cursor()
            cur.execute("insert into Students values(%s,%s,%s,%s,%s,%s,%s)", (self.Roll_No_var.get(),
                                                                              self.Name_var.get(),
                                                                              self.Email_var.get(),
                                                                              self.Gender_var.get(),
                                                                              self.Contact_var.get(),
                                                                              self.dob_var.get(),
                                                                              self.text_Address.get(
                                                                                  '1.0', END)
                                                                              ))

            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            tmsg.showinfo("Error", "Values Add")

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root",
                              password="", database="std")
        cur = con.cursor()
        cur.execute("select * from Students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert("", END, values=row)
                con.commit()
            con.close()

    def clear(self):

        self.Roll_No_var.set(""),
        self.Name_var.set(""),
        self.Email_var.set(""),
        self.Gender_var.set(""),
        self.Contact_var.set(""),
        self.dob_var.set(""),
        self.text_Address.delete('1.0', END)

    def get_cursor(self, ev):
        cursor_row = self.Student_table.focus()
        content = self.Student_table.item(cursor_row)
        row = content["values"]
        # print(row)
        self.Roll_No_var.set(row[0]),
        self.Name_var.set(row[1]),
        self.Email_var.set(row[2]),
        self.Gender_var.set(row[3]),
        self.Contact_var.set(row[4]),
        self.dob_var.set(row[5]),
        self.text_Address.delete('1.0', END),
        self.text_Address.insert(END, row[6])

    def update(self):
        if self.Roll_No_var.get() == "" or self.Name_var.get() == "" or self.Email_var.get() == "" or self.Gender_var.get() == "" or self.Contact_var.get() == "" or self.dob_var.get() == "":
            tmsg.showinfo("Error", " Updata any values ..!!!")
        else:
            con = pymysql.connect(
                host="localhost", user="root", password="", database="std")
            cur = con.cursor()
            cur.execute("update Students set Name=%s,Email=%s,Gender=%s,Contact=%s,dob=%s,Address=%s where roll_no=%s", (

                self.Name_var.get(),
                self.Email_var.get(),
                self.Gender_var.get(),
                self.Contact_var.get(),
                self.dob_var.get(),
                self.text_Address.get('1.0', END),
                self.Roll_No_var.get(),

            ))

            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            tmsg.showinfo("Done", "ok updata All required")

    def delete(self):
        if self.Roll_No_var.get() == "" or self.Name_var.get() == "" or self.Email_var.get() == "" or self.Gender_var.get() == "" or self.Contact_var.get() == "" or self.dob_var.get() == "":
            tmsg.showinfo("Error", " Select any values")
        else:
            tmsg.showinfo("Done", "ok delete")
            con = pymysql.connect(
                host="localhost", user="root", password="", database="std")
            cur = con.cursor()
            cur.execute("delete from Students where roll_no=%s",
                        self.Roll_No_var.get())
            con.commit()
            con.close()
            self.fetch_data()
            self.clear()

    def search_data_roll_no(self):
        if self.Roll_No_var.get() == "":
            tmsg.showinfo("Error", " Enter the sr_no")

        else:
            con = pymysql.connect(
                host="localhost", user="root", password="", database="std")
            sql_query = "select * from students where  roll_no =%s"
            vals = (self.search_text.get())
            cur = con.cursor()
            cur.execute(sql_query, vals)
            rows = cur.fetchall()
            if len(rows) != 0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert("", END, values=row)
                    con.commit()
                con.close()
                tmsg.showinfo("ok", " values are Show ")

    def search_data_name(self):
        if self.Name_var.get() == "":
            tmsg.showinfo("Error", " Enter the Name")
        else:
            con = pymysql.connect(
                host="localhost", user="root", password="", database="std")
            sql_query = "select * from students where Name =%s "

            vals = (self.search_text2.get())
            cur = con.cursor()
            cur.execute(sql_query, vals)
            rows = cur.fetchall()
            if len(rows) != 0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert("", END, values=row)
                    con.commit()
                    tmsg.showinfo("ok", " values are Show ")
                con.close()


############################### --Table fram---####################################
root = Tk()
ob = student(root)
root.mainloop()
