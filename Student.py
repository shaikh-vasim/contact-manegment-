from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


class student:

    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")
        self.root.geometry("1350x700+0+0")
        self.root.maxsize(1350, 700)
        self.root.minsize(1350, 700)
        self.root.wm_iconbitmap("contact_people.ico")
        title = Label(self.root, text="Contact Manegment System", font=("times new roman", "40", "bold"),
                      bg="green", fg="white", bd=10, relief=SUNKEN)
        title.pack(side=TOP, fill=X)

        # ========== All variables ===========
        self.Roll_No_var = StringVar()
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Gender_var = StringVar()
        self.Contact_var = StringVar()
        self.dob_var = StringVar()

        self.Search_by = StringVar()
        self.Search_txt = StringVar()
        # ============= Manage frame ===============

        Manage_frame = Frame(self.root, bd=4, relief=RIDGE, bg="blue")
        Manage_frame.place(x=20, y=100, width=450, height=580)

        m_title = Label(Manage_frame, text="Manage Contact", bg="blue",
                        fg="white", font=("times new roman", "25", "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll = Label(Manage_frame, text="Sr No.", bg="blue",
                         fg="white", font=("times new roman", "20", "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="W")

        txt_Roll = Entry(Manage_frame, textvariable=self.Roll_No_var, font=(
            "times new roman", "15", "bold"), bd=5, relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10, padx=10, sticky="W")

        lbl_name = Label(Manage_frame, text="Name", bg="blue",
                         fg="white", font=("times new roman", "20", "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="W")

        txt_name = Entry(Manage_frame, textvariable=self.Name_var, font=(
            "times new roman", "15", "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=10, sticky="W")

        lbl_email = Label(Manage_frame, text="Email", bg="blue",
                          fg="white", font=("times new roman", "20", "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="W")

        txt_email = Entry(Manage_frame, textvariable=self.Email_var, font=(
            "times new roman", "15", "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=10, sticky="W")

        lbl_gender = Label(Manage_frame, text="Gender", bg="blue",
                           fg="white", font=("times new roman", "20", "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="W")

        combo_gender = ttk.Combobox(Manage_frame, textvariable=self.Gender_var, font=(
            "times new roman", "14", "bold"), state='readonly')
        combo_gender["values"] = ("male", "female", "other")
        combo_gender.grid(row=4, column=1, padx=10, pady=10)

        lbl_contact = Label(Manage_frame, text="Contact", bg="blue",
                            fg="white", font=("times new roman", "20", "bold"))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="W")

        txt_contact = Entry(Manage_frame, textvariable=self.Contact_var, font=(
            "times new roman", "15", "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=10, sticky="W")

        lbl_dob = Label(Manage_frame, text="D.O.B", bg="blue",
                        fg="white", font=("times new roman", "20", "bold"))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="W")

        txt_dob = Entry(Manage_frame, textvariable=self.dob_var, font=(
            "times new roman", "15", "bold"), bd=5, relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=10, padx=10, sticky="W")

        lbl_Address = Label(Manage_frame, text="Address", bg="blue",
                            fg="white", font=("times new roman", "20", "bold"))
        lbl_Address.grid(row=7, column=0, pady=10, padx=20, sticky="W")

        self.txt_Address = Text(Manage_frame, width=30,
                                height=3, font=("", 10))
        self.txt_Address.grid(row=7, column=1, padx=10, pady=10, sticky="W")

        # ============Button frame====================

        btn_frame = Frame(Manage_frame, bd=4, relief=RIDGE, bg="blue")
        btn_frame.place(x=15, y=500, width=410)

        addbtn = Button(btn_frame, text="Add", width=10, command=self.add_students).grid(
            row=0, column=0, padx=10, pady=10)
        updatebtn = Button(btn_frame, text="Update", width=10, command=self.update_data).grid(
            row=0, column=1, padx=10, pady=10)
        delatebtn = Button(btn_frame, text="Delete", width=10, command=self.delete_data).grid(
            row=0, column=2, padx=10, pady=10)
        clearbtn = Button(btn_frame, text="Clear", width=10, command=self.clear).grid(
            row=0, column=3, padx=10, pady=10)

        # ============= Detail frame ===============
        Detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg="yellow")
        Detail_frame.place(x=500, y=100, width=900, height=580)

        lbl_search = Label(Detail_frame, text="Search By", bg="yellow",
                           fg="blue", font=("times new roman", "20", "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="W")

        combo_search = ttk.Combobox(Detail_frame, width=12, textvariable=self.Search_by, font=(
            "times new roman", "13", "bold"), state='readonly')
        combo_search["values"] = ("Name", "Contact")
        combo_search.grid(row=0, column=1, padx=8, pady=12)

        txt_search = Entry(Detail_frame, width=20, textvariable=self.Search_txt,  font=(
            "times new roman", "10", "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=10, sticky="W")

        searchbtn = Button(Detail_frame, text="Search", width=10, pady=5, command=self.Search_data).grid(
            row=0, column=3, padx=10, pady=10)
        showallbtn = Button(Detail_frame, text="Show All", width=10, pady=5, command=self.fetch_data).grid(
            row=0, column=4, padx=10, pady=10)

        #
        # #=============table frame=======================
        #

        T_fram = Frame(Detail_frame, bd=4, relief=RIDGE, bg="blue")
        T_fram.place(x=10, y=90, width=815, height=455)

        scroll_x = Scrollbar(T_fram, orient=HORIZONTAL)
        scroll_y = Scrollbar(T_fram, orient=VERTICAL)
        self.Student_table = ttk.Treeview(T_fram, columns=(
            "roll", "name", "email", "gender", "contact", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.configure(command=self.Student_table.xview)
        scroll_y.configure(command=self.Student_table.yview)

        self.Student_table.heading("roll", text="Sr No.")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="D.O.B")
        self.Student_table.heading("address", text="Address")
        self.Student_table["show"] = "headings"
        self.Student_table.column("roll", width=100)
        self.Student_table.column("name", width=170)
        self.Student_table.column("email", width=190)
        self.Student_table.column("gender", width=120)
        self.Student_table.column("contact", width=150)
        self.Student_table.column("dob", width=120)
        self.Student_table.column("address", width=170)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_students(self):
        if self.Roll_No_var.get() == "" or self.Name_var.get() == "" or self.Email_var.get() == "" or self.Gender_var.get() == "" or self.Contact_var.get() == "" or self.dob_var.get() == "":
            messagebox.showinfo("Error", "All Filds are required ..!!!")

        else:
            con = pymysql.connect(host="localhost", user="root",
                                  password="", database="std")
            cur = con.cursor()
            cur.execute("insert into Students values(%s,%s,%s,%s,%s,%s,%s)", (self.Roll_No_var.get(),
                                                                              self.Name_var.get(),
                                                                              self.Email_var.get(),
                                                                              self.Gender_var.get(),
                                                                              self.Contact_var.get(),
                                                                              self.dob_var.get(),
                                                                              self.txt_Address.get(
                '1.0', END)

            ))

            con.commit()
            self.clear()
            self.fetch_data()
            con.close()
            messagebox.showinfo("Success", "Record has been inserted")

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
        self.Roll_No_var.set("")
        self.Roll_No_var.set("")
        self.Name_var.set("")
        self.Email_var.set("")
        self.Gender_var.set("")
        self.Contact_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete("1.0", END)

    def get_cursor(self, ev):
        cursor_row = self.Student_table.focus()
        content = self.Student_table.item(cursor_row)
        row = content['values']

        self.Roll_No_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Gender_var.set(row[3])
        self.Contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert(END, row[6])

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root",
                              password="", database="std")
        cur = con.cursor()
        cur.execute("update Students set Name=%s,Email=%s,Gender=%s,Contact=%s,dob=%s,Address=%s where Roll_No=%s ", (
            self.Name_var.get(),
            self.Email_var.get(),
            self.Gender_var.get(),
            self.Contact_var.get(),
            self.dob_var.get(),
            self.txt_Address.get('1.0', END),
            self.Roll_No_var.get()

        ))

        con.commit()
        self.clear()
        self.fetch_data()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root",
                              password="", database="std")

        cur = con.cursor()
        cur.execute("delete from Students where roll_no=%s",
                    self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def Search_data(self):
        con = pymysql.connect(host="localhost", user="root",
                              password="", database="std")
        cur = con.cursor()
        cur.execute("select * from Students where " + str(self.Search_by.get()
                                                          ) + " LIKE '%" + str(self.Search_txt.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert("", END, values=row)
                con.commit()
            con.close()


root = Tk()
ob = student(root)
root.mainloop()
