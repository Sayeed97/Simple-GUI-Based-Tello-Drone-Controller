# Brief
Tello Drone is an impressive and programmable drone perfect for education. You can easily learn programming languages such as Scratch, Python, and Swift. A simple GUI was implemented to control the drone movement, direction, angle, takeoff, land and camera. The above was done by getting the user input through a text box and by writing a call back functions for dedicated buttons. 

# Tested Environment
The program was tested in Spyder environment (Python3).

# Tello Drone Features
- 720 HD Transmission
- 5 MP Camera 
- 13 min Flight Time
- Precise Hovering
- Mulitple Flight Modes 
- SDK Support

# Libraries Used

```
   Library for drone control: eastTello
   Library for GUI creation: tkinter
   Library for Keyboard access: pynput
   Library for Program control: sys
```  
- pip command to install easyTello is `pip install easytello`
- pip command to install tkinter is `pip install tk`
- pip command to install pynput is `pip install pynput`
- pip command to install sys is `pip install os-sys`

# Code Sequence
- Declared the required variables
- Instantiated all the required classes
- Wrote call back functions for dedicated buttons
- GUI packing was done that is all the various parts of the GUI like buttons, text box and labels 
- Defined a key release call back function for keyboard
- Exception for the keyboard listener function was written
- Start the keyboard listener thread
- Start the tkinter GUI master mainloop

# How to run the code
The code should be able to run in any python3 environment. 

Run *telloController.py*

Note: Before you run the code make sure you have your tello drone connected with your laptop WiFi. 
