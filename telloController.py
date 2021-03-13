#importing all the library
from pynput import keyboard
import sys
import tkinter as tk
import easytello as tello

#initializing global variables
dist = 20 #drone movement distance
angle = 45 #drone rotation angle in degrees 
takeoff = True #takeoff status

master = tk.Tk() #instantiation of Tkinter class
drone = tello.Tello() #instantiation of Tello class

#callback function for setting dist and angle
def parameter_sel():
    global dist 
    global angle
    dist = dist_var.get() #gets the input from the GUI slider
    angle = angle_var.get() #gets the input from the GUI slider 

#callback function for updating the battery information
def bat_info_callback():
    bat_info.set("Drone Status:\n" + "Battery = " + str(drone.get_battery()) + " %")

#callback function for takeoff and landing the drone 
def takeoff_callback():
    global takeoff #declaring takeoff as a global variable
    if takeoff:
        drone.takeoff()
        takeoff = False
    else:
        drone.land()
        takeoff = True

#callback function for camera stream
def camera_callback():
        drone.streamon()

#Tkinter variables to receive data from the GUI 
dist_var = tk.IntVar()
angle_var = tk.IntVar()
bat_info = tk.StringVar()
bat_info.set("Drone Status:\n" + "Battery = " + str(drone.get_battery()) + " %")
takeoff_info = tk.StringVar()

#GUI creation using Tkinter functions from tk instance
label = tk.Label(master, textvariable= bat_info)
label.pack()
scale1 = tk.Scale(orient = 'horizontal', from_ = 20, to = 100, variable = dist_var)
scale2 = tk.Scale(orient = 'horizontal', from_ = 1, to = 360, variable = angle_var)
scale1.pack()
scale2.pack()
button1 = tk.Button(master, text = "Update distance(cm) and angle(degree)", command=parameter_sel)
button1.pack()
button3 = tk.Button(master, text = "Update battery info", command=bat_info_callback)
button3.pack()
button2 = tk.Button(master, text = "Takeoff/Land", command=takeoff_callback)
button2.pack()
button3 = tk.Button(master, text = "Camera ON", command=camera_callback)
button3.pack()

#printing the default dist and angle 
print("Drone standard distance: ", dist)
print("Drone standard angle: ", angle)

#defining a callback function for the Tello drone controller 
def release_callback(key):
    global takeoff
    global stream
    global dist
    
    try:
        if format(key.char) == 'w':
            drone.forward(dist)
            
        elif format(key.char) == 's':
            drone.back(dist)

        elif format(key.char) == 'a':
            drone.left(dist)

        elif format(key.char) == 'd':
            drone.right(dist)

        elif format(key.char) == 'q':
            drone.ccw(angle)

        elif format(key.char) == 'e':
            drone.cw(angle)

        elif format(key.char) == 't':
            if takeoff == True:
                drone.takeoff()
                takeoff = False
            else:
                drone.land()
                takeoff = True
    
    except AttributeError:
        print("Stopped listening to the keyboard")
        drone.land()
        drone.streamoff()
        print("Exiting the Program...")
        sys.exit(0)

#release_callback function is set a parameter to Listener function
listener = keyboard.Listener(on_release=release_callback)
#starts the listener thread
listener.start()
#starts the Tkinter main loop
master.mainloop()