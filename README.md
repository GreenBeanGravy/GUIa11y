# FortniteA11y
A tool that tries to add extra accessibility to the online game Fortnite for individuals who are blind or visually impaired. Currently, the tool does not function in game. This repository is currently here to allow me to push changes as they come out. This page will be properly updated in the future as I work towards the first release. If you end up reading this before I remove it in the first release, make sure to Watch this repository and Star it! This is a big project and you won't want to miss it.

Currently, you can navigate the tkinter GUI window (though it's opacity is set to 0.01 so it is practically invisible) using the arrow keys. The left and right arrow keys change between sections, and the up and down arrow keys change between the elements within those sections. An editor is provided that allows speedy editing of the config.json file, though it is not accessible yet. The config.json file can also be edited manually. The script outputs to NVDA but also works even if no screen reader is open.

Below is a template I will be using for the future README:

# FortniteA11y

The project aims to make Fortnite more accessible for visually impaired users by providing screenreader output for the game's user interface. It consists of two main files: `FortniteA11y.py` and `editor.py`.

## FortniteA11y.py

This script helps visually impaired users navigate through the Fortnite user interface by providing audio feedback for the selected elements. Users can navigate through sections and elements using the arrow keys. The script also takes screenshots and compares them to a library of images to provide context about the current game screen.

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
Run FortniteA11y.py:
```
python FortniteA11y.py
```

### Editor.py
This script provides a graphical interface for editing the config.json file, which contains information about sections and elements in the Fortnite user interface. You can can add, edit, and remove sections and elements using the editor, or by directly modifying the config.json file.

## Usage

Run editor.py:

```
python editor.py
```

### Configuration
The config.json file is used to store information about sections and elements in the Fortnite user interface. The file contains an array of sections, each with a name and an array of elements. Each element has a name, an X coordinate, and a Y coordinate stored within itself.

##Example:

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
