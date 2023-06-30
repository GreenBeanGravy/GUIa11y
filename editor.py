import json
import tkinter as tk
from tkinter import messagebox, Entry, Toplevel, StringVar
from accessible_output2.outputs.auto import Auto
import os

# Load config data from the JSON file
with open("config.json") as file:
    config = json.load(file)

current_section = None

output = Auto()

# Function to update the elements listbox
def update_elements_list(section_index):
    listbox_elements.delete(0, tk.END)
    for element in config["sections"][section_index]["elements"]:
        listbox_elements.insert(tk.END, element["name"])

def create_section():
    top = Toplevel(root)
    top.title("Create Section")
    top.focus_force()

    section_name_var = StringVar()

    def handle_enter(event):
        process_section_creation(section_name_var.get(), top)

    label = tk.Label(top, text="Enter the name for the new section:")
    label.pack()
    entry = Entry(top, textvariable=section_name_var)
    entry.pack()
    entry.focus_set()
    entry.bind("<Return>", handle_enter)

    def speak_section_name(event):
        output.speak("Enter the name for the new section.")

    def handle_escape(event):
        output.speak("Canceled")
        top.destroy()

    top.bind("<Escape>", handle_escape)

    entry.configure(textvariable=section_name_var)
    entry.bind("<FocusIn>", speak_section_name)
    entry.after(100, lambda: output.speak("Enter the name for the new section."))

    def speak_updated_text(*args):
        name = section_name_var.get()
        if name.strip():
            output.speak(f"Name: {name}")

    section_name_var.trace_add("write", speak_updated_text)

    # Event binding to speak the text in the text field of the section name
    entry.bind("<KeyRelease>", lambda event: output.speak(entry.get()))

# Function to process the creation of a new section
def process_section_creation(section_name, top):
    if section_name:
        section = {"name": section_name, "elements": []}
        config["sections"].append(section)
        update_section_buttons()
        update_elements_list(len(config["sections"]) - 1)
        save_config()
        output.speak(f"New section created: {section_name}")
        top.destroy()

# Function to create a new element
def create_element():
    top = Toplevel(root)
    top.title("Create Element")
    top.focus_force()

    element_name_var = StringVar()
    element_x_var = StringVar()
    element_y_var = StringVar()

    def handle_enter(event):
        process_element_creation(element_name_var.get(), element_x_var.get(), element_y_var.get(), top)

    label_name = tk.Label(top, text="Enter the name for the new element:")
    label_name.pack()
    entry_name = Entry(top, textvariable=element_name_var)
    entry_name.pack()
    entry_name.focus_set()
    entry_name.bind("<Return>", handle_enter)

    label_x = tk.Label(top, text="Enter the X coordinate for the new element:")
    label_x.pack()
    entry_x = Entry(top, textvariable=element_x_var)
    entry_x.pack()
    entry_x.bind("<Return>", handle_enter)

    label_y = tk.Label(top, text="Enter the Y coordinate for the new element:")
    label_y.pack()
    entry_y = Entry(top, textvariable=element_y_var)
    entry_y.pack()
    entry_y.bind("<Return>", handle_enter)

    def speak_element_name(event):
        output.speak("Enter the name for the new element.")

    def handle_escape(event):
        output.speak("Canceled")
        top.destroy()

    top.bind("<Escape>", handle_escape)

    entry_name.configure(textvariable=element_name_var)
    entry_name.bind("<FocusIn>", speak_element_name)
    entry_name.after(100, lambda: output.speak("Enter the name for the new element."))

    def speak_element_x(event):
        output.speak("Enter the X coordinate for the new element.")

    entry_x.configure(textvariable=element_x_var)
    entry_x.bind("<FocusIn>", speak_element_x)

    def speak_element_y(event):
        output.speak("Enter the Y coordinate for the new element.")

    entry_y.configure(textvariable=element_y_var)
    entry_y.bind("<FocusIn>", speak_element_y)

    def speak_updated_text(*args):
        name = element_name_var.get()
        x = element_x_var.get()
        y = element_y_var.get()
        message = ""
    
        if name.strip():
            message += f"Name: {name}, "
        else:
            message += "Name, Blank. "
    
        if x.strip():
            message += f"X: {x}, "
        else:
            message += "X, Blank. "
    
        if y.strip():
            message += f"Y: {y}"
        else:
            message += "Y, Blank"
    
        output.speak(message)

    element_name_var.trace_add("write", speak_updated_text)
    element_x_var.trace_add("write", speak_updated_text)
    element_y_var.trace_add("write", speak_updated_text)

# Function to create a new element from the mouse position
def create_element_from_mouse():
    element_x, element_y = root.winfo_pointerxy()  # get mouse position

    top = Toplevel(root)
    top.title("Create Element")
    top.focus_force()

    element_name_var = StringVar()

    def handle_enter(event):
        process_element_creation(element_name_var.get(), str(element_x), str(element_y), top)

    label_name = tk.Label(top, text="Enter the name for the new element:")
    label_name.pack()
    entry_name = Entry(top, textvariable=element_name_var)
    entry_name.pack()
    entry_name.focus_set()
    entry_name.bind("<Return>", handle_enter)

    def speak_element_name(event):
        output.speak("Enter the name for the new element.")

    def handle_escape(event):
        output.speak("Canceled")
        top.destroy()

    top.bind("<Escape>", handle_escape)

    entry_name.configure(textvariable=element_name_var)
    entry_name.bind("<FocusIn>", speak_element_name)
    entry_name.after(100, lambda: output.speak("Enter the name for the new element."))

    def speak_updated_text(*args):
        name = element_name_var.get()
        if name.strip():
            output.speak(f"Name: {name}")

    element_name_var.trace_add("write", speak_updated_text)

    # Event binding to speak the text in the text field of the section name
    entry_name.bind("<KeyRelease>", lambda event: output.speak(entry_name.get()))

# Function to process the creation of a new element
def process_element_creation(element_name, element_x, element_y, top):
    if element_name and element_x and element_y:
        try:
            element_x = int(element_x)
            element_y = int(element_y)
            element = {"name": element_name, "x": element_x, "y": element_y}
            config["sections"][current_section]["elements"].append(element)
            update_elements_list(current_section)
            save_config()
            output.speak(f"New element created: {element_name}")
            top.destroy()
            update_elements_list(current_section)
            listbox_elements.selection_set(0)
            read_selected_element()
        except ValueError:
            messagebox.showerror("Error", "Invalid coordinate value")
            top.destroy()
            update_elements_list(current_section)
            listbox_elements.selection_set(0)
            read_selected_element()
    else:
        messagebox.showerror("Error", "Missing input value")

# Function to delete the current element/section
def delete_selected():
    global current_section  # Add this line to declare current_section as a global variable
    selected_element = listbox_elements.curselection()
    if selected_element:
        selected_element_index = selected_element[0]
        element_name = config["sections"][current_section]["elements"][selected_element_index]["name"]
        result = confirm_delete("element", element_name)
        if result:
            del config["sections"][current_section]["elements"][selected_element_index]
            update_elements_list(current_section)
            output.speak(f"Element deleted: {element_name}")
            save_config()
    else:
        section_name = config["sections"][current_section]["name"]
        result = confirm_delete("section", section_name)
        if result:
            del config["sections"][current_section]
            update_section_buttons()
            listbox_elements.delete(0, tk.END)
            output.speak(f"Section deleted: {section_name}")
            save_config()

            if len(config["sections"]) > 0:
                current_section = 0
                update_elements_list(current_section)
                listbox_elements.selection_set(0)
                read_selected_element()
            else:
                current_section = None

    # Call the autoselect_first_section function after an element or section is deleted
    autoselect_first_section()

# Function to confirm the deletion of an element/section
def confirm_delete(item_type, item_name):
    confirmation = messagebox.askquestion("Confirm Deletion", f"Are you sure you want to delete the {item_type}: {item_name}?")
    return confirmation == "yes"

# Function to update the section buttons
def update_section_buttons():
    for button in section_buttons:
        button.destroy()
    section_buttons.clear()
    for section_index, section in enumerate(config["sections"]):
        button = tk.Button(frame_sections, text=section["name"], command=lambda index=section_index: update_elements_list(index))
        button.pack(side=tk.TOP, padx=5, pady=5)
        section_buttons.append(button)

# Function to save the changes to the config file
def save_config():
    with open("config.json", "w") as file:
        json.dump(config, file, indent=4)

# Function to switch between sections
def change_section(event):
    global current_section
    if event.keysym == "Left" and current_section > 0:
        current_section -= 1
    elif event.keysym == "Right" and current_section < len(config["sections"]) - 1:
        current_section += 1
    else:
        return

    section_name = config["sections"][current_section]["name"]
    output.speak(section_name)
    update_elements_list(current_section)
    listbox_elements.focus_set()
    root.after(500, lambda: (listbox_elements.selection_set(0), read_selected_element()))

# Function to navigate through elements
def change_element(event):
    if event.keysym == "Up":
        move_element_selection(-1)
    elif event.keysym == "Down":
        move_element_selection(1)

def move_element_selection(direction):
    selected_element = listbox_elements.curselection()
    if not selected_element:
        return

    selected_element = selected_element[0]
    new_element = selected_element + direction
    if 0 <= new_element < listbox_elements.size():
        listbox_elements.selection_clear(0, tk.END)
        listbox_elements.selection_set(new_element)
        listbox_elements.activate(new_element)
        listbox_elements.see(new_element)

    read_selected_element()

def read_selected_element():
    selected_element = listbox_elements.curselection()
    if not selected_element:
        return

    selected_element = selected_element[0]
    element = config["sections"][current_section]["elements"][selected_element]
    element_name = element["name"]
    element_x = element["x"]
    element_y = element["y"]
    output.speak(f"{element_name}, X: {element_x}, Y: {element_y}")

# Function to click the element
def click_element(event):
    selected_element = listbox_elements.curselection()
    if not selected_element:
        return
    selected_element = selected_element[0]
    element = config["sections"][current_section]["elements"][selected_element]

    output.speak("Element clicked")
    save_config()

# Function to terminate the program
def terminate_program(event):
    root.destroy()

# Function to handle the delete key press
def handle_delete_key(event):
    delete_selected()

# Function to auto-select the first section and its first element
def autoselect_first_section():
    global current_section
    if len(config["sections"]) > 0:
        current_section = 0
        update_elements_list(current_section)
        listbox_elements.selection_set(0)
        read_selected_element()

# Function to focus the message boxes when they appear
def focus_messagebox():
    root.focus_force()

# Create and configure the main window
root = tk.Tk()
root.title("Config Editor")
root.geometry("500x300")

frame_sections = tk.Frame(root)
frame_sections.pack(side=tk.LEFT, padx=10, pady=10)

frame_elements = tk.Frame(root)
frame_elements.pack(side=tk.LEFT, padx=10, pady=10)

frame_controls = tk.Frame(root)
frame_controls.pack(side=tk.LEFT, padx=10, pady=10)

# Add elements listbox
listbox_elements = tk.Listbox(frame_elements)
listbox_elements.pack(side=tk.LEFT, padx=5, pady=5)

# Add scrollbar to the listbox
scrollbar_elements = tk.Scrollbar(frame_elements)
scrollbar_elements.pack(side=tk.LEFT, fill=tk.Y)
listbox_elements.config(yscrollcommand=scrollbar_elements.set)
scrollbar_elements.config(command=listbox_elements.yview)

# Add section buttons
section_buttons = []
for section_index, section in enumerate(config["sections"]):
    button = tk.Button(frame_sections, text=section["name"], command=lambda index=section_index: update_elements_list(index))
    button.pack(side=tk.TOP, padx=5, pady=5)
    section_buttons.append(button)

# Call the autoselect_first_section function
autoselect_first_section()

# Set focus to the elements listbox
listbox_elements.focus_set()

# Speak the name of the first section and first element after a delay
root.after(1000, lambda: output.speak(config["sections"][0]["name"]))
root.after(1500, lambda: output.speak(config["sections"][0]["elements"][0]["name"]))

# Bind arrow keys for navigation
root.bind("<Left>", change_section)
root.bind("<Right>", change_section)
root.bind("<Up>", change_element)
root.bind("<Down>", change_element)
root.bind("<Return>", click_element)
root.bind("<space>", click_element)

# Bind keybinds for additional functionalities
root.bind("<F5>", lambda event: create_section())
root.bind("<F6>", lambda event: create_element())
root.bind("<F7>", lambda event: create_element_from_mouse())
root.bind("<F8>", terminate_program)

# Bind delete key for removing elements/sections
root.bind("<Delete>", handle_delete_key)

# Bind focus event to focus the message boxes
root.bind("<FocusIn>", lambda event: focus_messagebox())

# Run the main loop
root.mainloop()
