import tkinter as tk
import json
import os
from datetime import date, timedelta

misc_tasks = []
general_tasks = []
room_tasks = []
 
Task_File = os.path.join(os.path.dirname(__file__), "tasks.json")

def load_tasks():
    if os.path.exists(Task_File):
        with open(Task_File) as f:
            return json.load(f)
    return []

def save_tasks():
    with open(Task_File, "w") as f:
        json.dump(misc_tasks, f)

misc_tasks = load_tasks()
def openMisc():
    misc = tk.Toplevel()
    misc.title("Miscellaneous tasks")
    misc.geometry("1000x1000")
    misc.config(bg="lavender")
    tk.Label(misc, text="Miscellaneous Tasks",
             font=("Comfortaa", 40, "bold", "underline"),
             bg="lavender", fg="black").place(x=300, y=300)
    y = 400
    for i in misc_tasks: 
        due = date.fromisoformat(i["due"])
        while i["repeat"] and due < date.today():
            due += timedelta(days=i["frequency"])
            i["due"] = due.isoformat()
        days_left = (due - date.today()).days
        if days_left > 0:
            text = f"{i['task']} - Due in {days_left} days" 
            color = "#77DD77"
        elif days_left == 0:
            text = f"{i['task']} - Due today" 
            color = "#FDFD96"
        else:
            text = f"{i['task']} - Overdue by {-days_left} days" 
            color = "#FF6B6B"
        Task_List = tk.Listbox(misc, font=("Comfortaa", 20), bg="lavender", fg=color)
        Task_List.place(x=400, y=y)
        Task_List.insert(tk.END, text)
        Task_List.config(height=Task_List.size())
        y += 50

    def delete_task(task):
        selection = Task_List.curselection()
        if not selection:
            return
        else:
            misc_tasks.pop(Task_List.curselection()[0])
            save_tasks()
            misc.destroy()
            openMisc()


    delete_button = tk.Button(misc, text = "delete task", command=lambda: delete_task(misc_tasks[Task_List.curselection()[0]]))
    delete_button.place(x=400, y=y)
 
 
def openRoom():
    room = tk.Toplevel()
    room.title("Room tasks")
    room.geometry("1000x1000")
    room.config(bg="lavender")
    tk.Label(room, text="Room Tasks",
             font=("Comfortaa", 40, "bold", "underline"),
             bg="lavender", fg="black").place(x=400, y=300)
    y = 400
    for i in room_tasks:
        due = date.fromisoformat(i["due"])
        while i["repeat"] and due < date.today():
            due += timedelta(days=i["frequency"])
            i["due"] = due.isoformat()
        days_left = (due - date.today()).days
        if days_left > 0:
            text = f"{i['task']} - Due in {days_left} days"
            color = "#77DD77"
        elif days_left == 0:
            text = f"{i['task']} - Due today"
            color = "#FDFD96"
        else:
            text = f"{i['task']} - Overdue by {-days_left} days"
            color = "#FF6B6B"
        Task_List = tk.Listbox(room, font=("Comfortaa", 20), bg="lavender", fg=color)
        Task_List.place(x=400, y=y)
        Task_List.insert(tk.END, text)
        Task_List.config(height=Task_List.size())
        y += 50

    def delete_task(task):
        selection = Task_List.curselection()
        if not selection:
            return
        else:
            room_tasks.pop(Task_List.curselection()[0])
            save_tasks()
            room.destroy()
            openRoom()

    delete_button = tk.Button(room, text="delete task", command=lambda: delete_task(room_tasks[Task_List.curselection()[0]]))
    delete_button.place(x=400, y=y)


def openGeneral():
    general = tk.Toplevel()
    general.title("General tasks")
    general.geometry("1000x1000")
    general.config(bg="lavender")
    tk.Label(general, text="General Tasks",
             font=("Comfortaa", 40, "bold", "underline"),
             bg="lavender", fg="black").place(x=400, y=300)
    y = 400
    for i in general_tasks:
        due = date.fromisoformat(i["due"])
        while i["repeat"] and due < date.today():
            due += timedelta(days=i["frequency"])
            i["due"] = due.isoformat()
        days_left = (due - date.today()).days
        if days_left > 0:
            text = f"{i['task']} - Due in {days_left} days"
            color = "#77DD77"
        elif days_left == 0:
            text = f"{i['task']} - Due today"
            color = "#FDFD96"
        else:
            text = f"{i['task']} - Overdue by {-days_left} days"
            color = "#FF6B6B"
        Task_List = tk.Listbox(general, font=("Comfortaa", 20), bg="lavender", fg=color)
        Task_List.place(x=400, y=y)
        Task_List.insert(tk.END, text)
        Task_List.config(height=Task_List.size())
        y += 50

    def delete_task(task):
        selection = Task_List.curselection()
        if not selection:
            return
        else:
            general_tasks.pop(Task_List.curselection()[0])
            save_tasks()
            general.destroy()
            openGeneral()

    delete_button = tk.Button(general, text="delete task", command=lambda: delete_task(general_tasks[Task_List.curselection()[0]]))
    delete_button.place(x=400, y=y)


def open_misc_entry():
    misc_entry = tk.Toplevel()
    misc_entry.title("Add Task")
    misc_entry.geometry("1000x1000")
    misc_entry.config(bg="lavender")
    tk.Label(misc_entry, text="Add Task",
             font=("Comfortaa", 40, "bold", "underline"),
             bg="lavender", fg="black").place(x=400, y=300)
    return misc_entry

def open_room_entry():
    room_entry = tk.Toplevel()
    room_entry.title("Add Task")
    room_entry.geometry("1000x1000")
    room_entry.config(bg="lavender")
    tk.Label(room_entry, text="Add Task",
             font=("Comfortaa", 40, "bold", "underline"),
             bg="lavender", fg="black").place(x=400, y=300)
    return room_entry

def open_general_entry():
    general_entry = tk.Toplevel()
    general_entry.title("Add Task")
    general_entry.geometry("1000x1000")
    general_entry.config(bg="lavender")
    tk.Label(general_entry, text="Add Task",
             font=("Comfortaa", 40, "bold", "underline"),
             bg="lavender", fg="black").place(x=400, y=300)
    return general_entry
 
def openAdd():
    add = tk.Toplevel()
    add.title("Add Task")
    add.geometry("1000x1000")
    add.config(bg="lavender")
    tk.Label(add, text="Add Task",
             font=("Comfortaa", 40, "bold", "underline"),
             bg="lavender", fg="black").place(x=400, y=300)
 
    addList = tk.Listbox(add, font=("Comfortaa", 20, "bold"),
                         bg="lavender", fg="black",
                         selectbackground="black", selectforeground="white")
    addList.place(x=375, y=400)
    addList.insert(tk.END, "Miscellaneous Tasks")
    addList.insert(tk.END, "Room Tasks")
    addList.insert(tk.END, "General Tasks")
    addList.config(height=addList.size())
    addList.bind("<Double-1>", lambda event: on_add_list_double_click(addList, add))
 

def on_add_list_double_click(addList, add):
    selection = addList.get(addList.curselection())
    if selection == "Miscellaneous Tasks":
        misc_entry = open_misc_entry()
        M_task = tk.Entry(misc_entry, font=("Comfortaa", 20), bg="lavender", fg="black")
        M_task.insert(0, "Enter task here")
        M_task.place(x=400, y=500)
        M_frequency = tk.Entry(misc_entry, font=("Comfortaa", 20), bg="lavender", fg="black",)
        M_frequency.insert(0, "Enter frequency in days here")
        M_frequency.place(x=400, y=600)
        Repeat_var = tk.BooleanVar()
        Repeat = tk.Checkbutton(misc_entry, variable = Repeat_var, text="Repeat", font=("Comfortaa", 20), bg="lavender", fg="black")
        Repeat.place(x=400, y=700)

        def submit_misc_task():
                task = M_task.get()
                try:
                    M_freq = int(M_frequency.get())
                except ValueError:
                    return
                due = date.today() + timedelta(days=M_freq)
                misc_tasks.append({"task": M_task.get(), "frequency": M_freq, "repeat": Repeat_var.get(), "due": due.isoformat()})
                save_tasks()
                misc_entry.destroy()
        Insert_button = tk.Button(misc_entry, text="Submit", command=submit_misc_task, font=("Comfortaa", 20), bg="black", fg="white")
        Insert_button.place(x=580, y=690)
    elif selection == "Room Tasks":
        room_entry = open_room_entry()
        R_task = tk.Entry(room_entry, font=("Comfortaa", 20), bg="lavender", fg="black")
        R_task.insert(0, "Enter task here")
        R_task.place(x=400, y=500)
        R_frequency = tk.Entry(room_entry, font=("Comfortaa", 20), bg="lavender", fg="black",)
        R_frequency.insert(0, "Enter frequency in days here")
        R_frequency.place(x=400, y=600)
        Repeat_var = tk.BooleanVar()
        Repeat = tk.Checkbutton(room_entry, variable = Repeat_var, text="Repeat", font=("Comfortaa", 20), bg="lavender", fg="black")
        Repeat.place(x=400, y=700)

        def submit_room_task():
            task = R_task.get()
            try:
                R_freq = int(R_frequency.get())
            except ValueError:
                return
            due = date.today() + timedelta(days=R_freq)
            room_tasks.append({"task": R_task.get(), "frequency": R_freq, "repeat": Repeat_var.get(), "due": due.isoformat()})
            save_tasks()
            room_entry.destroy()
        Insert_button = tk.Button(room_entry, text="Submit", command=submit_room_task, font=("Comfortaa", 20), bg="black", fg="white")
        Insert_button.place(x=580, y=690)

    elif selection == "General Tasks":
        general_entry = open_general_entry()
        G_task = tk.Entry(general_entry, font=("Comfortaa", 20), bg="lavender", fg="black")
        G_task.insert(0, "Enter task here")
        G_task.place(x=400, y=500)
        G_frequency = tk.Entry(general_entry, font=("Comfortaa", 20), bg="lavender", fg="black")
        G_frequency.insert(0, "Enter frequency in days here")
        G_frequency.place(x=400, y=600)
        Repeat_var = tk.BooleanVar()
        Repeat = tk.Checkbutton(general_entry, variable = Repeat_var, text="Repeat", font=("Comfortaa", 20), bg="lavender", fg="black")
        Repeat.place(x=400, y=700)
        

        def submit_general_task():
            task = G_task.get()
            try:
                G_freq = int(G_frequency.get())
            except ValueError:
                return
            due = date.today() + timedelta(days=G_freq)
            general_tasks.append({"task": G_task.get(), "frequency": G_freq, "repeat": Repeat_var.get(), "due": due.isoformat()})
            save_tasks()
            general_entry.destroy()

        Insert_button = tk.Button(general_entry, text="Submit", command=submit_general_task, font=("Comfortaa", 20), bg="black", fg="white")
        Insert_button.place(x=580, y=690)

        

 
def openHome():
    homePage = tk.Tk()
    homePage.title("Responsibilities")
    homePage.geometry("1000x1000")
    homePage.config(bg="lavender")
 
    tk.Label(homePage, text="Responsibilities",
             font=("Comfortaa", 40, "bold", "underline"),
             bg="lavender", fg="black").place(x=300, y=300)
 
    tk.Button(homePage, text="Misc. Tasks", command=openMisc,
              padx=22, pady=10, bg="black", fg="grey",
              relief="ridge", activebackground="white").place(x=300, y=450)
    tk.Button(homePage, text="Room Tasks", command=openRoom,
              padx=22, pady=10, bg="black", fg="grey",
              relief="ridge", activebackground="white").place(x=600, y=450)
    tk.Button(homePage, text="General Tasks", command=openGeneral,
              padx=22, pady=10, bg="black", fg="grey",
              relief="ridge", activebackground="white").place(x=300, y=600)
    tk.Button(homePage, text="Add Task", command=openAdd,
              padx=22, pady=10, bg="black", fg="grey",
              relief="ridge", activebackground="white").place(x=600, y=600)
 
    homePage.mainloop()
 
 
if __name__ == "__main__":
    openHome()
 
