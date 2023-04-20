import json
import tkinter as tk
from accessible_output2.outputs.auto import Auto
import pyautogui
import keyboard
import cv2
import numpy as np
import os

# Load config data from the JSON file
with open("config.json") as file:
    config = json.load(file)

output = Auto()

# Function to update the elements listbox
def update_elements_list(section_index):
    listbox_elements.delete(0, tk.END)
    for element in config["sections"][section_index]["elements"]:
        listbox_elements.insert(tk.END, element["name"])

def take_screenshot():
    if keyboard.is_pressed('F12'):
        screenshot = pyautogui.screenshot()
        process_screenshot(screenshot)
        return False
    elif keyboard.is_pressed('F7'):
        return True
    return False

def process_screenshot(screenshot):
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
    best_match = None
    best_score = float('inf')

    for filename in os.listdir("image_library"):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            image_path = os.path.join("image_library", filename)
            library_image = cv2.imread(image_path, 0)
            
            # Resize library image to match the dimensions of the screenshot
            library_image_resized = cv2.resize(library_image, (screenshot_gray.shape[1], screenshot_gray.shape[0]))
            
            score = compare_images(screenshot_gray, library_image_resized)
            if score < best_score:
                best_score = score
                best_match = filename

    if best_match:
        output.speak(f"I think you are in {best_match}")

def compare_images(image1, image2):
    err = np.sum((image1.astype("float") - image2.astype("float")) ** 2)
    err /= float(image1.shape[0] * image1.shape[1])
    return err

# Function to switch between sections
def change_section(event):
    if event.keysym == "Left":
        direction = -1
    elif event.keysym == "Right":
        direction = 1
    else:
        return

    global current_section
    current_section = (current_section + direction) % len(config["sections"])

    section_name = config["sections"][current_section]["name"]
    output.speak(section_name)
    update_elements_list(current_section)
    listbox_elements.focus_set()
    root.after(500, lambda: (listbox_elements.selection_set(0), read_selected_element()))

# Function to navigate through elements
def change_element(event):
    if event.keysym != "Up" and event.keysym != "Down":
        return

    root.after(50, read_selected_element)

def read_selected_element():
    selected_element = listbox_elements.curselection()
    if not selected_element:
        return

    selected_element = selected_element[0]
    element_name = config["sections"][current_section]["elements"][selected_element]["name"]
    output.speak(element_name)

    x, y = config["sections"][current_section]["elements"][selected_element]["x"], config["sections"][current_section]["elements"][selected_element]["y"]
    pyautogui.moveTo(x, y)

def click_element(event):
    selected_element = listbox_elements.curselection()
    if not selected_element:
        return
    selected_element = selected_element[0]
    element = config["sections"][current_section]["elements"][selected_element]
    pyautogui.click(element["x"], element["y"])

# Create and configure the main window
root = tk.Tk()
root.title("Audio Access")
root.geometry("500x300")

frame_sections = tk.Frame(root)
frame_sections.pack(side=tk.LEFT, padx=10, pady=10)

frame_elements = tk.Frame(root)
frame_elements.pack(side=tk.LEFT, padx=10, pady=10)

# Add section buttons
section_buttons = []
for section in config["sections"]:
    button = tk.Button(frame_sections, text=section["name"], command=lambda s=section: update_elements_list(s["index"]))
    button.pack(side=tk.TOP, padx=5, pady=5)
    section_buttons.append(button)

# Add elements listbox
listbox_elements = tk.Listbox(frame_elements)
listbox_elements.pack(side=tk.LEFT, padx=5, pady=5)

# Add scrollbar to the listbox
scrollbar_elements = tk.Scrollbar(frame_elements)
scrollbar_elements.pack(side=tk.LEFT, fill=tk.Y)
listbox_elements.config(yscrollcommand=scrollbar_elements.set)
scrollbar_elements.config(command=listbox_elements.yview)

# Set the initial section and update the elements list
current_section = 0
update_elements_list(current_section)

# Bind arrow keys for navigation
root.bind("<Left>", change_section)
root.bind("<Right>", change_section)
root.bind("<Up>", change_element)
root.bind("<Down>", change_element)
root.bind("<Return>", click_element)
root.bind("<space>", click_element)

root.attributes('-alpha', 0.01)  # Make the window almost invisible, but still interactable

def main_loop():
    while True:
        root.update_idletasks()
        root.update()
        if take_screenshot():
            break

# Run the main loop
main_loop()