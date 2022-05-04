# Create a window

# importing tkinter gui
import tkinter as tk

#creating window
window=tk.Tk()

#setting tkinter window size(Width and Hight)
window.geometry("%dx%d" % (100, 200))

# mainloop() is simply a method in the main window that executes what we wish to execute in an application (lets Tkinter to start running the application). As the name implies it will loop forever until the user exits the window or waits for any events from the user.
window.mainloop()