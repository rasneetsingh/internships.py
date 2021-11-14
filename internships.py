from tkinter import *
from tkinter import ttk, messagebox
import pymysql


class InternshipApp():
    '''
    It include variables and title for the project, establish a size for the window using the geometry function, and  will create the GUI for the project.
    '''

    def __init__(self, root):
        self.root = root
        self.root.title("Internship Tracking Database")
        self.root.geometry("1370x700")

        title = Label(self.root, text="Internship Tracking Database", bd=9, relief=GROOVE, font=(
            "times new roman", 30, "bold"), bg="medium purple", fg="white")
        title.pack(side=TOP, fill=X)

    #Allvariables
        self.Company_Name_var = StringVar()
        self.Job_Posting_var = StringVar()
        self.Recruiter_Contact_var = StringVar()
        self.Sponsorship_var = StringVar()
        self.Apply_var = StringVar()
        self.Interview_var = StringVar()
        self.Offer_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        '''
        It creates  the frame that's on the left side of database where user enter the information)
        '''

        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="medium purple")
        Manage_Frame.place(x=20, y=100, width=450, height=585)

        m_title = Label(Manage_Frame, text="Manage Application",
                        bg="yellow", fg="black", font=("times new roman", 28, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_name = Label(Manage_Frame, text="Company Name", bg="medium purple",
                         fg="white", font=("times new roman", 14, "bold"))
        lbl_name.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        txt_name = Entry(Manage_Frame, textvariable=self.Company_Name_var, font=(
            "times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_posting = Label(Manage_Frame, text="Job Posting", bg="medium purple",
                            fg="white", font=("times new roman", 14, "bold"))
        lbl_posting.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_posting = Entry(Manage_Frame, textvariable=self.Job_Posting_var, font=(
            "times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_posting.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_contact = Label(Manage_Frame, text="Recruiter Contact",
                            bg="medium purple", fg="white", font=("times new roman", 14, "bold"))
        lbl_contact.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_contact = Entry(Manage_Frame, textvariable=self.Recruiter_Contact_var,  font=(
            "times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_sponsorship = Label(Manage_Frame, text="Sponsorship",
                                bg="medium purple", fg="white", font=("times new roman", 14, "bold"))
        lbl_sponsorship.grid(row=4, column=0, pady=10, padx=20, sticky="w")
        combo_sponsorship = ttk.Combobox(Manage_Frame, textvariable=self.Sponsorship_var, font=(
            "times new roman", 13, "bold"), state='readonly')
        combo_sponsorship['values'] = ("Yes", "No")
        combo_sponsorship.grid(row=4, column=1, padx=20, pady=10)

        lbl_apply = Label(Manage_Frame, text="Apply", bg="medium purple",
                          fg="white", font=("times new roman", 14, "bold"))
        lbl_apply.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        combo_apply = ttk.Combobox(Manage_Frame, textvariable=self.Apply_var, font=(
            "times new roman", 13, "bold"), state='readonly')
        combo_apply['values'] = ("Yes", "No")
        combo_apply.grid(row=5, column=1, padx=20, pady=10)

        lbl_interview = Label(Manage_Frame, text="Interview", bg="medium purple",
                              fg="white", font=("times new roman", 14, "bold"))
        lbl_interview.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        combo_interview = ttk.Combobox(Manage_Frame, textvariable=self.Interview_var, font=(
            "times new roman", 13, "bold"), state='readonly')
        combo_interview['values'] = ("Yes", "No")
        combo_interview.grid(row=7, column=1, padx=20, pady=10)

        lbl_offer = Label(Manage_Frame, text="Offer", bg="medium purple",
                          fg="white", font=("times new roman", 14, "bold"))
        lbl_offer.grid(row=8, column=0, pady=10, padx=20, sticky="w")
        txt_offer = Entry(Manage_Frame, textvariable=self.Offer_var, font=(
            "times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_offer.grid(row=8, column=1, pady=10, padx=20, sticky="w")

        # buttonframe(Frame at the bottom on the left)
        btn_frame = Frame(Manage_Frame, bd=3, relief=RIDGE, bg="black")
        btn_frame.place(x=5, y=500, width=420)

        Addbtn = Button(btn_frame, text="Add", width=10, command=self.add_internships).grid(row=0, column=0, padx=10,
                                                                                            pady=10)
        updatebtn = Button(btn_frame, text="Update", width=10, command=self.update_data).grid(
            row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_frame, text="Delete", width=10, command=self.delete_data).grid(
            row=0, column=2, padx=10, pady=10)
        clearbtn = Button(btn_frame, text="Clear", width=10, command=self.clear).grid(
            row=0, column=3, padx=10, pady=10)

        # DetailsFrame
        details_Frame = Frame(
            self.root, bd=4, relief=RIDGE, bg="medium purple")
        details_Frame.place(x=500, y=100, width=880, height=585)

        lbl_search = Label(details_Frame, text="Search By", bg="medium purple",
                           fg="white", font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")
        combo_search = ttk.Combobox(details_Frame, textvariable=self.search_by, font=(
            "times new roman", 13, "bold"), width=10, state='readonly')
        combo_search['values'] = ("Sponsorship", "Interview", "Offer")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_search = Entry(details_Frame, textvariable=self.search_txt, font=(
            "times new roman", 10, "bold"), width=20, bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(details_Frame, text="Search", width=10, pady=5,
                           command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(details_Frame, text="Show All", width=10, pady=5,
                            command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)

        # Table Frame
        Table_Frame = Frame(details_Frame, bd=4,
                            relief=RIDGE, bg="medium purple")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        self.InternshipApp_table = ttk.Treeview(Table_Frame, column=(
            "Company Name", "Job Posting", "Recruiter Contact", "Sponsorship", "Apply", "Interview", "Offer"), xscrollcommand=scroll_y, yscrollcommand=scroll_x)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config()
        scroll_y.config()

        self.InternshipApp_table.heading("Company Name", text="Company Name")
        self.InternshipApp_table.heading("Job Posting", text="Job Posting")
        self.InternshipApp_table.heading(
            "Recruiter Contact", text="Recruiter Contact")
        self.InternshipApp_table.heading("Sponsorship", text="Sponsorship")
        self.InternshipApp_table.heading("Apply", text="Apply")
        self.InternshipApp_table.heading("Interview", text="Interview")
        self.InternshipApp_table.heading("Offer", text="Offer")

        self.InternshipApp_table['show'] = 'headings'
        self.InternshipApp_table.column("Company Name", width=100)
        self.InternshipApp_table.column("Job Posting", width=100)
        self.InternshipApp_table.column("Recruiter Contact", width=100)
        self.InternshipApp_table.column("Sponsorship", width=100)
        self.InternshipApp_table.column("Apply", width=100)

        self.InternshipApp_table.column("Interview", width=100)
        self.InternshipApp_table.column("Offer", width=100)
        self.InternshipApp_table.pack(fill=BOTH, expand=1)
        self.InternshipApp_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_internships(self):
        if self.Company_Name_var.get() == "" or self.Job_Posting_var.get() == "":
            messagebox.showerror("Error", "All Fields are required to fill")
        else:
            con = pymysql.connect(
                host="localhost", user="admin", password="dhoni", database="tasktracker")
            cur = con.cursor()
            print("connect")

            cur.execute("insert into internship values(%s, %s,%s, %s,%s, %s,%s)", (self.Company_Name_var.get(),
                                                                                   self.Job_Posting_var.get(),
                                                                                   self.Recruiter_Contact_var.get(),
                                                                                   self.Sponsorship_var.get(),
                                                                                   self.Apply_var.get(),
                                                                                   self.Interview_var.get(),
                                                                                   self.Offer_var.get(),))

            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Record has been inserted")

    '''
    It  creates connectivity between sql and GUI and  will fetch our data from the database and show it in our GUI created.
    '''

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="admin",
                              password="dhoni", database="tasktracker")
        cur = con.cursor()
        cur.execute("select * from internship")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.InternshipApp_table.delete(
                *self.InternshipApp_table.get_children())
            for row in rows:
                self.InternshipApp_table.insert('', END, values=row)
            con.commit()
        con.close()

    '''
    It creates cursor in the GUI to allow users to show movable indicator on computer screen.
    '''

    def get_cursor(self, ev):
        cursor_row = self.InternshipApp_table.focus()
        contents = self.InternshipApp_table.item(cursor_row)
        row = contents['values']
        self.Company_Name_var.set(row[0])
        self.Job_Posting_var.set(row[1])
        self.Recruiter_Contact_var.set(row[2])
        self.Sponsorship_var.set(row[3])
        self.Apply_var.set(row[4])
        self.Interview_var.set(row[5])
        self.Offer_var.set(row[6])

    '''
    It helps us clear the entry while entering the fields on the left table of database. 
    '''

    def clear(self):
        self.Company_Name_var.set("")
        self.Job_Posting_var.set(""),
        self.Recruiter_Contact_var.set(""),
        self.Sponsorship_var.set(""),
        self.Apply_var.set(""),
        self.Interview_var.set(""),
        self.Offer_var.set("")

    '''
    It  allows us to update data of already existing entry.
    '''

    def update_data(self):
        con = pymysql.connect(host="localhost", user="admin",
                              password="dhoni", database="tasktracker")
        cur = con.cursor()

        cur.execute("update internship set  JobPosting=%s,RecruiterContact=%s,sponsorship=%s, apply=%s, interview=%s,offer=%s where CompanyName=%s", (
            self.Job_Posting_var.get(),
            self.Recruiter_Contact_var.get(),
            self.Sponsorship_var.get(),
            self.Apply_var.get(),
            self.Interview_var.get(),
            self.Offer_var.get(),
            self.Company_Name_var.get()
        ))

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Success", "Record has been inserted")

    '''
    It allows us to delete the selected row of entry.
    '''

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="admin",
                              password="dhoni", database="tasktracker")
        cur = con.cursor()
        cur.execute("delete from internship where CompanyName=%s",
                    self.Company_Name_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="admin",
                              password="dhoni", database="tasktracker")
        cur = con.cursor()
        cur.execute("select * from internship where " +
                    str(self.search_by.get()) + " Like '%" + str(self.search_txt.get())+"%';")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.InternshipApp_table.delete(
                *self.InternshipApp_table.get_children())
            for row in rows:
                self.InternshipApp_table.insert('', END, values=row)
            con.commit()
        con.close()


class InternshipApp():
    pass
    root = Tk()
    obj = InternshipApp(root)
    root.mainloop()