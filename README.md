# MOUSE CONTROL USING HAND GESTURE

This is a small piece code that allows the users to convert their hand gestures into commands fot the cursor
## Getting Started

To access all of the files I recommend you fork this repo and then clone it locally. Instructions on how to do this can be found here: https://help.github.com/en/github/getting-started-with-github/fork-a-repo

### Prerequisites

You wil need to install the following onto your machine:
python 3.6
opencv-python
pyautogui

### Installing

Follow the given commands to intall the libraries

Say what the step will be

```
pip install opencv-python
pip install pyautogui
```

## Extra info

If you are using an inbuilt camera then the code will run just fine 
if you are using an external camera, change the following:
```
cap = cv2.VideoCapture(0)
```
to
```
cap = cv2.VideoCapture(1)

```
