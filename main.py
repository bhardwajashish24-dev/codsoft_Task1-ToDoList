import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import platform
import sqlite3
import os
from datetime import date

class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.buttons = ["Progress Task","Completed","Task History","Create Task"]
        self.title("To Do List")
        self.center_window()
        self.top_panel()
        self.center_panels()
        self.task_panel(1)
        self.TaskButton.config(bg="green")
        

    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.winfo_reqwidth()) // 2
        y = (screen_height - self.winfo_reqheight()) // 2
        self.geometry(f"+{x}+{y}")
        self.maxsize(width=750,height=500)
        self.minsize(width=750,height=500)
        

    def top_panel(self):
        panel = tk.Frame(self,highlightbackground="white", highlightthickness=2)
        panel.grid(row=1,column=1,padx=10,pady=10)
        label = tk.Label(panel,text="To Do List",fg="purple",font= ('Helvetica  35 bold italic'))
        label.grid(row=1,column=0,columnspan=4)

        self.TaskButton = tk.Button(panel, text=self.buttons[0],height=2,width=15,bg="purple",fg="white",font= ('Helvetica 12 bold italic'))
        self.TaskButton.config(command=lambda i=1:self.process(i))
        self.TaskButton.grid(row=2, column=0, padx=10, pady=10)

        self.CompleteButton = tk.Button(panel, text=self.buttons[1],height=2,width=15,bg="purple",fg="white",font= ('Helvetica 12 bold italic'))
        self.CompleteButton.config(command=lambda i=2:self.process(i))
        self.CompleteButton.grid(row=2, column=1, padx=10, pady=10)

        self.TaskHistoryButton = tk.Button(panel, text=self.buttons[2],height=2,width=15,bg="purple",fg="white",font= ('Helvetica 12 bold italic'))
        self.TaskHistoryButton.config(command=lambda i=3:self.process(i))
        self.TaskHistoryButton.grid(row=2, column=2, padx=10, pady=10)

        self.CreateTaskButton = tk.Button(panel, text=self.buttons[3],height=2,width=15,bg="purple",fg="white",font= ('Helvetica 12 bold italic'))
        self.CreateTaskButton.config(command=lambda i=4:self.process(i))
        self.CreateTaskButton.grid(row=2, column=3, padx=10, pady=10)


    def process(self,n):
        if n==1:
            self.center_panel.grid_forget()
            self.center_panels()
            self.task_panel(1)
            self.TaskButton.config(bg="green")
            self.CompleteButton.config(bg="purple")
            self.TaskHistoryButton.config(bg="purple")
            self.CreateTaskButton.config(bg="purple")
        elif n==2:
            self.center_panel.grid_forget()
            self.center_panels()
            self.task_panel(2)
            self.TaskButton.config(bg="purple")
            self.CompleteButton.config(bg="green")
            self.TaskHistoryButton.config(bg="purple")
            self.CreateTaskButton.config(bg="purple")
        elif n==3:
            self.center_panel.grid_forget()
            self.center_panels()
            self.task_panel(3)
            self.TaskButton.config(bg="purple")
            self.CompleteButton.config(bg="purple")
            self.TaskHistoryButton.config(bg="green")
            self.CreateTaskButton.config(bg="purple")
        elif n==4:
            self.center_panel.grid_forget()
            self.center_panels()
            self.create_task_panels()
            self.TaskButton.config(bg="purple")
            self.CompleteButton.config(bg="purple")
            self.TaskHistoryButton.config(bg="purple")
            self.CreateTaskButton.config(bg="green")


    def task_panel(self,n):
        back = BackEnd()
        if n==1:
            data = back.progress_task()
            for row in data:
                panel=tk.Frame(self.process_panel,width=400,height=100,highlightbackground="purple",highlightthickness=2,bg="purple")
                panel.pack(expand=True,fill="both",padx=10,pady=5) 
                
                Headlabel = tk.Label(panel,text="Task "+str(row[1]) + "  -  "+str(row[3]),fg="white",bg="purple",font= ('Helvetica  16 bold italic'))
                Headlabel.grid(row=1,column=2)
                
                radiobtn = tk.Checkbutton(panel,font= ('Helvetica  16 bold italic'),bg="purple",command=lambda i=row[0]: back.check_button(i))
                radiobtn.grid(row=2,column=1)
                
                label = tk.Label(panel,text=str(row[2]),width=45,fg="purple",font= ('Helvetica  16 bold italic'))
                label.grid(row=2,column=2)
                
                photo = tk.PhotoImage(file = 'TrashCan.png') 
                delbtn=tk.Button(panel,text="DEL",width=40,bg="purple",image=photo,fg="white",font= ('Helvetica  10 bold italic'))
                delbtn.config(image=photo,command=  lambda i=row[0]: back.del_button(i,1))
                delbtn.image = photo
                delbtn.grid(row=2,column=3,padx=5,pady=2)
        elif n==2:
            data = back.get_complete_task()
            for row in data:
                panel=tk.Frame(self.process_panel,width=400,height=100,highlightbackground="purple",highlightthickness=2,bg="purple")
                panel.pack(expand=True,fill="both",padx=10,pady=5) 
                
                Headlabel = tk.Label(panel,text="Task "+str(row[1]) + "  -  "+str(row[3]),fg="white",bg="purple",font= ('Helvetica  16 bold italic'))
                Headlabel.pack(expand=True,fill="both")
                
                #radiobtn = tk.Checkbutton(panel,font= ('Helvetica  16 bold italic'),bg="purple",command=lambda i=row[0]: back.check_button(i))
                #radiobtn.grid(row=2,column=1)
                
                label = tk.Label(panel,text=str(row[2]),width=45,fg="purple",font= ('Helvetica  16 bold italic'))
                label.pack(expand=True,fill="both")
                
                #photo = tk.PhotoImage(file = 'TrashCan.png') 
                #delbtn=tk.Button(panel,text="DEL",width=40,bg="purple",image=photo,fg="white",font= ('Helvetica  10 bold italic'))
                #delbtn.config(image=photo,command=  lambda i=row[0]: back.del_button(i))
                #delbtn.image = photo
                #delbtn.grid(row=2,column=3,padx=5,pady=2)
        elif n==3:
            data = back.get_task_history()
            for row in data:
                panel=tk.Frame(self.process_panel,width=400,height=100,highlightbackground="purple",highlightthickness=2,bg="purple")
                panel.pack(expand=True,fill="both",padx=10,pady=5) 
                
                Headlabel = tk.Label(panel,text="Task "+str(row[1]) + "  -  "+str(row[3]),fg="white",bg="purple",font= ('Helvetica  16 bold italic'))
                Headlabel.grid(row=1,column=2)
                
                radiobtn = tk.Checkbutton(panel,font= ('Helvetica  16 bold italic'),bg="purple",command=lambda i=row[0]: back.check_button(i))
                radiobtn.grid(row=2,column=1)
                radiobtn.config(state="disabled")
                if row[4] == 1:
                    radiobtn.select()
                
                label = tk.Label(panel,text=str(row[2]),width=45,fg="purple",font= ('Helvetica  16 bold italic'))
                label.grid(row=2,column=2)
                
                
                photo = tk.PhotoImage(file = 'TrashCan.png') 
                delbtn=tk.Button(panel,text="DEL",width=40,bg="purple",image=photo,fg="white",font= ('Helvetica  10 bold italic'))
                delbtn.config(image=photo,command=  lambda i=row[0]: back.del_button(i,3))
                delbtn.image = photo
                delbtn.grid(row=2,column=3,padx=5,pady=2)
                
        

    def complete_task_panel(self):
        pass

    def create_task_panels(self):
        back=BackEnd()
        self.vScrollbar.pack_forget()
        self.Task_var = tk.StringVar()
        name_label = tk.Label(self.canvas, text = 'TASK', font=('calibre',10, 'bold'))
        name_entry = tk.Entry(self.canvas,textvariable = self.Task_var, font=('calibre',10,'normal'))
        
        sub_btn=tk.Button(self.canvas,text = 'Submit',command=lambda : back.create_task(self.Task_var.get(),Datecal.get_date()))
        DateLabel = tk.Label(self.canvas, text = 'Date', font=('calibre',10, 'bold'))
        Datecal = Calendar(self.canvas, font="Arial 8", selectmode='day', locale='en_US',cursor="hand1", 
                        year=date.today().year, month=date.today().month, day=date.today().day)

        name_label.grid(row=0,column=0,padx=(100,20),pady=(50,10))
        name_entry.grid(row=0,column=1,padx=(20,20),pady=(50,10))
        DateLabel.grid(row=1,column=0,padx=(100,20),pady=(10,10))
        Datecal.grid(row=1,column=1,padx=(50,20),pady=(10,20))
        sub_btn.grid(row=2,column=0,columnspan=2,padx=(0,0))

        

    def center_panels(self):
        self.center_panel=tk.Frame(self,width=800,height=500,highlightbackground="purple",highlightthickness=2)
        self.center_panel.grid(row=2,column=1,padx=10,pady=10)
        self.canvas = tk.Canvas(self.center_panel,width=700,height=300,borderwidth=0,bg="white")
        self.process_panel = tk.Frame(self.canvas,bg="gray")
        self.vScrollbar = tk.Scrollbar(self.center_panel,orient="vertical",command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vScrollbar.set)

        self.vScrollbar.pack(side="right",fill="y")
        self.canvas.pack(side="left",fill="both",expand=True)
        self.canvas_window = self.canvas.create_window((4,4),window=self.process_panel,anchor="nw",tags="self.process_panel")

        self.process_panel.bind("<Configure>", self.onFrameConfigure)                       
        self.canvas.bind("<Configure>", self.onCanvasConfigure)                       
            
        self.process_panel.bind('<Enter>', self.onEnter)                                
        self.process_panel.bind('<Leave>', self.onLeave)                                

        self.onFrameConfigure(None)                                                 

    def onFrameConfigure(self, event):                                              
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))                 

    def onCanvasConfigure(self, event):
        '''Reset the canvas window to encompass inner frame when required'''
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width = canvas_width)            

    def onMouseWheel(self, event):                                                  
        if platform.system() == 'Windows':
            self.canvas.yview_scroll(int(-1* (event.delta/120)), "units")
        elif platform.system() == 'Darwin':
            self.canvas.yview_scroll(int(-1 * event.delta), "units")
        else:
            if event.num == 4:
                self.canvas.yview_scroll( -1, "units" )
            elif event.num == 5:
                self.canvas.yview_scroll( 1, "units" )
    
    def onEnter(self, event):                                                       
        if platform.system() == 'Linux':
            self.canvas.bind_all("<Button-4>", self.onMouseWheel)
            self.canvas.bind_all("<Button-5>", self.onMouseWheel)
        else:
            self.canvas.bind_all("<MouseWheel>", self.onMouseWheel)

    def onLeave(self, event):                                                       
        if platform.system() == 'Linux':
            self.canvas.unbind_all("<Button-4>")
            self.canvas.unbind_all("<Button-5>")
        else:
            self.canvas.unbind_all("<MouseWheel>")

class BackEnd():
    def __init__(self) -> None:
        pass

    def del_button(self,Id,n):
        #messagebox.showinfo("Welcome to del button"+str(n),  "Hi I'm your message") 
        data = db.Delete_Data(Id)
        if data == False:
            print("Error !!! Unable to Delete")
            self.Show_Message("Error !!!","Unable to Delete")
            app.process(n)
            return None
        else:
            print("Succesfully Delete")
            self.Show_Message("Message","Succesfully Delete")
            app.process(n)
            return data
        
        


    def progress_task(self):
        data = db.Get_Data_By_IsComplete()
        if data == False:
            print("Error !!! Unable to Get Data")
            self.Show_Message("Error !!!","Unable To Get Data")
            return None
        else:
            print("Retrieve Data")
            return data

    def get_complete_task(self):
        data = db.Get_Data_By_IsComplete(True)
        if data == False:
            print("Error !!! Unable to Get Data")
            self.Show_Message("Error !!!","Unable To Get Data")
            return None
        else:
            print("Retrieve Data")
            return data
        
    def get_task_history(self):
        data = db.Get_All_Data()
        if data == False:
            print("Error !!! Unable to Get Data")
            self.Show_Message("Error !!!","Unable To Get Data")
            return None
        else:
            print("Retrieve Data")
            return data

    def check_button(self,Id):
        data = db.Update_Data(Id,True)
        if data == False:
            print("Error !!! Unable to Update")
            self.Show_Message("Error !!!","Unable To Update")
            return None
        else:
            print("Succesfully Update")
            self.Show_Message("Message","Succesfully Update")
            app.process(1)
            return data

    def create_task(self,TaskData,Date):
        data = db.Get_Last_Id()
        LastId= data[0][0]
        if LastId == None:
            LastId= 0
            curr_date = date.today().strftime("%m/%d/%y")
            LastTaskNo = 0
        else:
            curr_date = date.today().strftime("%m/%d/%y")
            data = db.Get_Last_TaskNo(curr_date)
            LastTaskNo = data[0][0]
            if data == None:
                LastTaskNo=0

        if db.Insert_Data(LastId+1,LastTaskNo+1,TaskData,Date,False) == False:
            print("Error !!! Unable to Insert Data")
            self.Show_Message("Error !!!","Unable To Insert Data")
        else:
            print("Succesfully Insert Data")
            self.Show_Message("Message","Succesfully Insert Data")

    def Show_Message(self,message,data):
        messagebox.showinfo(message, data)


class TaskEntry():
    def __init__(self) -> None:
        pass


class DBConnection():
    def __init__(self) -> None:
        self.db_file = 'database.db'
        schema_file = 'schema.sql'
        try:
            if os.path.exists(self.db_file):
                print('Database already exists. Exiting...')
            else:
                with open(schema_file, 'r') as rf:
                    # Read the schema from the file
                    schema = rf.read()
                
                with sqlite3.connect(self.db_file) as conn:
                    print('Created the connection!')
                    # Execute the SQL query to create the table
                    conn.executescript(schema)
                    print('Created the Table! Now inserting')
                    conn.executescript("""
                                    insert into Task (Id, TaskNo, TaskDetail,Date,IsComplete)
                                    values
                                    (0,0,"Sample Task Data" ,'2019-10-10',True);
                                    """)
                    print('Inserted values into the table!')
                print('Closed the connection!')
            #return True
        except:
            #return False
            pass


    def Show_Data(self):
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                            select * from Task
                            """)
                for row in cursor.fetchall():
                    Id, TaskNo, TaskDetail,Date,IsComplete = row
                    print(f'{Id} {TaskNo} {TaskDetail} {Date} {IsComplete}')
            return True
        except:
            return False
        
    
    def Get_All_Data(self):
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                            select * from Task ;
                            """)
                return cursor.fetchall()
        except:
            return False


    def Get_Data_By_IsComplete(self,IsComplete=False):
        try:
            curr_date = date.today().strftime("%m/%d/%y")
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                query="""
                select * from Task Where IsComplete="""+str(IsComplete)+""" and Date=\'"""+curr_date+"""\';
                            """
                cursor.execute(query)
                return cursor.fetchall()
        except:
            return False


    def Get_Data_By_Id(self,Id):
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                            select * from Task Where Id="""+ str(Id)+""";
                            """)
                return cursor.fetchall()
        except:
            return False


    def Get_Last_Id(self):
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                            select MAX(Id) from Task;
                            """)
                return cursor.fetchall()
        except:
            return False


    def Get_Last_TaskNo(self,Date):
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                            select MAX(TaskNo) from Task Where Date=\'"""+ str(Date)+"""\';
                            """)
                return cursor.fetchall()
        except Exception as e:
            print(e)
            return False


    def Insert_Data(self,Ids,TaskNos,TaskDetails,Dates,IsCompletes):
        try:
            with sqlite3.connect(self.db_file) as conn:
                print('Created the connection!')
                cursor=conn.cursor()
                query = """
                                insert into Task (Id, TaskNo, TaskDetail,Date,IsComplete)
                                values
                                ("""+str(Ids)+""","""+str(TaskNos)+""",\'"""+TaskDetails+"""\' ,\'"""+Dates+"""\',"""+str(IsCompletes)+""");
                                """
                cursor.execute(query)
                print('Inserted values into the table!')
            return True
        except Exception as e:
            print(e)
            return False


    def Update_Data(self,Id,IsComplete):
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                            update Task Set IsComplete="""+str(IsComplete)+""" where Id="""+str(Id)+""";
                            """)
            return True
        except:
            return False


    def Delete_Data(self,Id):
        try:
            with sqlite3.connect(self.db_file) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                                DELETE FROM Task WHERE Id="""+str(Id)+""";
                    """) 
            return True
        except:
            return False

if __name__ == "__main__":
    db = DBConnection()
    app = App()
    db.Show_Data()
    #print(db.Get_Data_By_Id(1))
    app.mainloop()