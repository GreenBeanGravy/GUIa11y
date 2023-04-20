import tkinter as tk
from tkinter import ttk, simpledialog
import json

def load_config(file_path):
    with open(file_path, "r") as file:
        config = json.load(file)
    return config

def save_config(file_path, config):
    with open(file_path, "w") as file:
        json.dump(config, file, indent=2)

config_file = "config.json"
config = load_config(config_file)

root = tk.Tk()
root.title("Config Editor")

frame_sections = ttk.Frame(root)
frame_elements = ttk.Frame(root)
frame_details = ttk.Frame(root)

frame_sections.grid(column=0, row=0, padx=10, pady=10)
frame_elements.grid(column=1, row=0, padx=10, pady=10)
frame_details.grid(column=2, row=0, padx=10, pady=10)

listbox_sections = tk.Listbox(frame_sections)
listbox_elements = tk.Listbox(frame_elements)

listbox_sections.pack(padx=10, pady=10)
listbox_elements.pack(padx=10, pady=10)

button_add_section = ttk.Button(frame_sections, text="Add Section")
button_remove_section = ttk.Button(frame_sections, text="Remove Section")

button_add_element = ttk.Button(frame_elements, text="Add Element")
button_remove_element = ttk.Button(frame_elements, text="Remove Element")

button_add_section.pack(padx=10, pady=10)
button_remove_section.pack(padx=10, pady=10)

button_add_element.pack(padx=10, pady=10)
button_remove_element.pack(padx=10, pady=10)

def update_sections_list():
    listbox_sections.delete(0, tk.END)
    for section in config["sections"]:
        listbox_sections.insert(tk.END, section["name"])

button_update_elements = ttk.Button(frame_sections, text="Update Elements")
current_section_index = -1

def update_elements_list(event=None):
    global current_section_index
    selected_section = listbox_sections.curselection()
    
    if event:
        if not selected_section:
            return
        current_section_index = selected_section[0]

    if current_section_index == -1:
        return

    listbox_elements.delete(0, tk.END)
    elements = config["sections"][current_section_index]["elements"]
    for element in elements:
        listbox_elements.insert(tk.END, element["name"])

    listbox_sections.selection_set(current_section_index)

listbox_sections.bind("<<ListboxSelect>>", update_elements_list)
button_update_elements.config(command=update_elements_list)
button_update_elements.pack(padx=10, pady=10)

def display_element_details(event):
    selected_element = listbox_elements.curselection()
    if not selected_element:
        return

    selected_element = selected_element[0]
    element = config["sections"][current_section_index]["elements"][selected_element]
    
    element_name.set(element["name"])
    element_x.set(element["x"])
    element_y.set(element["y"])

element_name = tk.StringVar()
element_x = tk.IntVar()
element_y = tk.IntVar()

label_name = ttk.Label(frame_details, text="Name:")
entry_name = ttk.Entry(frame_details, textvariable=element_name)

label_x = ttk.Label(frame_details, text="X:")
entry_x = ttk.Entry(frame_details, textvariable=element_x)

label_y = ttk.Label(frame_details, text="Y:")
entry_y = ttk.Entry(frame_details, textvariable=element_y)

label_name.grid(column=0, row=0, padx=10, pady=10)
entry_name.grid(column=1, row=0, padx=10, pady=10)

label_x.grid(column=0, row=1, padx=10, pady=10)
entry_x.grid(column=1, row=1, padx=10, pady=10)

label_y.grid(column=0, row=2, padx=10, pady=10)
entry_y.grid(column=1, row=2, padx=10, pady=10)

def add_section():
    section_name = simpledialog.askstring("Add Section", "Enter section name:")
    if section_name:
        config["sections"].append({"name": section_name, "elements": []})
        save_config(config_file, config)
        update_sections_list()

def remove_section():
    selected_section = listbox_sections.curselection()
    if selected_section:
        config["sections"].pop(selected_section[0])
        save_config(config_file, config)
        update_sections_list()

def add_element():
    global current_section_index
    if current_section_index == -1:
        return
    element_name = simpledialog.askstring("Add Element", "Enter element name:")
    if element_name:
        element_x = simpledialog.askinteger("Add Element", "Enter element X coordinate:")
        element_y = simpledialog.askinteger("Add Element", "Enter element Y coordinate:")
        element = {"name": element_name, "x": element_x, "y": element_y}
        config["sections"][current_section_index]["elements"].append(element)
        save_config(config_file, config)
        update_elements_list()

def remove_element():
    global current_section_index
    selected_element = listbox_elements.curselection()
    if current_section_index != -1 and selected_element:
        config["sections"][current_section_index]["elements"].pop(selected_element[0])
        save_config(config_file, config)
        update_elements_list()

button_add_section.config(command=add_section)
button_remove_section.config(command=remove_section)
button_add_element.config(command=add_element)
button_remove_element.config(command=remove_element)

listbox_elements.bind("<<ListboxSelect>>", display_element_details)

update_sections_list()

root.mainloop()