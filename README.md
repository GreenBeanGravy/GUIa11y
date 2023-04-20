# GUIa11y
A tool that tries to add universal accessibility to all GUIs alike for individuals who are blind or visually impaired. Currently, the tool is not set up for any specific GUI. This repository is currently here to allow me to push changes as they come out. This page will be properly updated in the future as I work towards the first release. If you end up reading this before I remove it in the first release, make sure to Watch this repository and Star it! This is a big project and you won't want to miss it. I plan on using this to add GUI accessibility to the game Fortnite in the future.

Currently, you can navigate the tkinter GUI window (though it's opacity is set to 0.01 so it is practically invisible) using the arrow keys. The left and right arrow keys change between sections, and the up and down arrow keys change between the elements within those sections. An editor is provided that allows speedy editing of the config.json file, though it is not accessible yet. The config.json file can also be edited manually. The script outputs to NVDA, but also works even if no screen reader is open.

Below is a template I will be using for the future README:

# GUIa11y

The project aims to make all GUIs alike accessible to visually impaired users by providing screenreader output. It consists of two main files: `GUIa11y.py` and `editor.py`.

## GUIa11y.py

This script helps visually impaired users navigate through a GUI by providing spoken feedback. You can navigate through sections and elements using the arrow keys. GUIa11y also can take a temporary screenshot of your screen, compare it to a library of images, and provide spoken feedback based on what part of a GUI it thinks you are on.

### Dependencies

- Python 3.6 or later
- accessible_output2
- pyautogui
- keyboard
- OpenCV (cv2)
- numpy

### Usage

1. Install the required dependencies using pip:
```
pip install accessible_output2 pyautogui keyboard opencv-python numpy
```
Run GUIa11y.py:
```
py GUIa11y.py
```

## Editor.py
The Editor provides its own GUI for editing the config.json file faster. You can can add, edit, or remove sections and elements using the Editor, or by directly modifying the config.json file.

### Usage

Run editor.py:

```
py editor.py
```

## Configuration
The config.json file is used to store information in the form of sections and elements. Think of a section as a folder, with elements in that section being individual files (not literally). The config.json file contains an array of sections, each with a name and an array of elements. Each element has a name, an X coordinate, and a Y coordinate stored within itself.

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
