import tkinter as tk
import json
import os
from datetime import date, timedelta

misc_tasks = []
general_tasks = []
room_tasks = []

 
Task_File = os.path.join(os.path.dirname(__file__), "Tasks.json")

def load_tasks():
    if os.path.exists(Task_File):
        with open(Task_File) as f:
            return json.load(f)
    return {}

def save_tasks():
    with open(Task_File, "w") as f:
        json.dump({"misc": misc_tasks, "general": general_tasks, "room": room_tasks}, f)

tasks_data = load_tasks()
misc_tasks = tasks_data.get("misc", [])
general_tasks = tasks_data.get("general", [])
room_tasks = tasks_data.get("room", [])
categories = {"misc": misc_tasks, "general": general_tasks, "room": room_tasks}

def openCategory(title, category):
    tasks = categories[category]
    window = tk.Toplevel()
    window.title(title)
    window.geometry("1000x1000")
    window.config(bg="lavender")
    tk.Label(window, text=title,
             font=("Comfortaa", 40, "bold", "underline"),
             bg="lavender", fg="black").place(x=300, y=300)
    Task_list = tk.Listbox(window, font=("Comfortaa", 20), bg="lavender")
    Task_list.place(x=400, y=400)
    for i in tasks: 
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
        Task_list.insert(tk.END, text,)
        Task_list.itemconfig(tk.END, fg=color)
    Task_list.config(height = Task_list.size())
        
    def delete_task():
        selection = Task_list.curselection()
        if not selection:
            return
        else:
            tasks.pop(selection[0])
            save_tasks()
            window.destroy()
            openCategory(title, category)


    delete_button = tk.Button(window, text = "delete task", command=delete_task)
    delete_button.place(x=280, y= 400)
 
def open_entry():
    entry = tk.Toplevel()
    entry.title("Add Task")
    entry.geometry("1000x1000")
    entry.config(bg="lavender")
    tk.Label(entry, text="Add Task",
             font=("Comfortaa", 40, "bold", "underline"),
             bg="lavender", fg="black").place(x=400, y=300)
    return entry


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
    options = {"Miscellaneous Tasks": "misc", "Room Tasks": "room", "General Tasks": "general"}
    selection = addList.get(addList.curselection())
    option_selected = options.get(selection)
    if not selection:
        return
    add.destroy()
    entry = open_entry()
    task_entry = tk.Entry(entry, font=("Comfortaa", 20), bg="lavender", fg="black")
    task_entry.insert(0, "Enter task here")
    task_entry.place(x=400, y=500)
    frequency_entry = tk.Entry(entry, font=("Comfortaa", 20), bg="lavender", fg="black")
    frequency_entry.insert(0, "Enter frequency in days here")
    frequency_entry.place(x=400, y=600)

    repeat_var = tk.BooleanVar()
    repeat_check = tk.Checkbutton(entry, variable=repeat_var, text="Repeat", font=("Comfortaa", 20), bg="lavender", fg="black")
    repeat_check.place(x=400, y=700)

    def submit_task():
        task = task_entry.get()
        try:
            freq = int(frequency_entry.get())
        except ValueError:
            return
        due = date.today() + timedelta(days=freq)
        categories[option_selected].append({"task": task, "frequency": freq, "repeat": repeat_var.get(), "due": due.isoformat()})
        save_tasks()
        entry.destroy()
    Insert_button = tk.Button(entry, text="Submit", command=submit_task, font=("Comfortaa", 20), bg="black", fg="white")
    Insert_button.place(x=580, y=690)
    

 
def openHome():
    homePage = tk.Tk()
    homePage.title("Responsibilities")
    homePage.geometry("1000x1000")
    homePage.config(bg="lavender")
 
    tk.Label(homePage, text="Responsibilities",
             font=("Comfortaa", 40, "bold", "underline"),
             bg="lavender", fg="black").place(x=300, y=300)
 
    tk.Button(homePage, text="Misc. Tasks", command= lambda: openCategory("Misc. Tasks", "misc"),
              padx=22, pady=10, bg="black", fg="grey",
              relief="ridge", activebackground="white").place(x=300, y=450)
    tk.Button(homePage, text="Room Tasks", command= lambda: openCategory("Room Tasks", "room"),
              padx=22, pady=10, bg="black", fg="grey",
              relief="ridge", activebackground="white").place(x=600, y=450)
    tk.Button(homePage, text="General Tasks", command= lambda: openCategory("General Tasks", "general"),
              padx=22, pady=10, bg="black", fg="grey",
              relief="ridge", activebackground="white").place(x=300, y=600)
    tk.Button(homePage, text="Add Task", command=openAdd,
              padx=22, pady=10, bg="black", fg="grey",
              relief="ridge", activebackground="white").place(x=600, y=600)
 
    homePage.mainloop()
 
 
if __name__ == "__main__":
    openHome()
 
