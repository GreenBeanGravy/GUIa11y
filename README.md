# GUIa11y
A tool that tries to add universal accessibility to all GUIs alike for individuals who are blind or visually impaired. GUIa11y works by allowing users to create "elements" and "sections". Think of a section as a folder, with elements in that section being individual files (not literally). Each element has a name, an X coordinate, and a Y coordinate stored within itself. Each element acts as a macro that moves your mouse to the defined X and Y coordinates, invokes a left click, and refocuses the main window.

An editor is provided that allows speedy editing of the config.json file, which is now completely accessible! The editor outputs to NVDA, but also works even if no screen reader is open. The Editor provides its own GUI for editing the config.json file faster. You can can add, edit, or remove sections and elements using the Editor, or by directly modifying the config.json file. Currently the acessible editor does not support creating "shortcuts" but that hasn't been entirely introduced yet, stay tuned! :)

### TODO
* Make keybinds easily customizable
* Add the ability to change the level of opaque-ness of the tkinter window
* Add a toggle for "Descriptive Speech" which would provide enhanced feedback through the screenreader on sections and elements

# GUIa11y Keybinds
- **Left Arrow Key**: Move to the previous section.
- **Right Arrow Key**: Move to the next section.
- **Up Arrow Key**: Move to the previous element in the current section.
- **Down Arrow Key**: Move to the next element in the current section.
- **Return Key / Space Bar**: Click the selected element.
- **F6 Key**: Closes the script.
- **F7 Key**: Run image comparison (currently does nothing with no images in the image_library folder)

# Editor Keybinds
- **Left Arrow Key**: Move to the previous section.
- **Right Arrow Key**: Move to the next section.
- **Up Arrow Key**: Move to the previous element in the current section.
- **Down Arrow Key**: Move to the next element in the current section.
- **Space Bar**: Click the selected element.
- **Enter**: Submit values when creating sections/elements.
- **Tab**: Used to navigate the different text boxes when creating a new element.
- **F5**: Creates a new section.
- **F6**: Creates a new element in the currently selected section.
- **F7**: Not been tested, supposed to create a new element using the current position of the mouse in the currently selected section.
- **F8**: Closes the script.

## Dependencies

- Python 3.6 or later
- accessible_output2
- pyautogui
- keyboard
- OpenCV (cv2)
- numpy

## Usage

1. Install the required dependencies using pip:
```
pip install accessible_output2 pyautogui keyboard opencv-python numpy
```
Run GUIa11y.py:
```
py GUIa11y.py
```

## Configuration
The config.json file is used to store information in the form of sections and elements. The config.json file contains an array of sections, each with a name and an array of elements.

### Example:

```
{
  "sections": [
    {
      "name": "Section 1",
      "elements": [
        {
          "name": "Element 1",
          "x": 100,
          "y": 100
        },
        {
          "name": "Element 2",
          "x": 200,
          "y": 200
        }
      ]
    },
    {
      "name": "Section 2",
      "elements": [
        {
          "name": "Element 3",
          "x": 300,
          "y": 300
        },
        {
          "name": "Element 4",
          "x": 400,
          "y": 400
        }
      ]
    }
  ]
}
```
