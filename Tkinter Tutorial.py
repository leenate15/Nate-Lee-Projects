from tkinter import *

# Create Tk object which is just an empty window
root = Tk()

# # Text in Tkinter is known as a label
# theLabel = Label(root, text='Hello World')

# # Simple way to "pack in" everything - simple organization
# theLabel.pack()

# Create two frames in the root window
topFrame = Frame(root)
topFrame.pack() # Do not need to explicitly place when other objects/frames are

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

# Create buttons
button1 = Button(topFrame, text='Button 1', fg='red') # fg is color parameter - stands for foreground
button2 = Button(topFrame, text='Button 2', fg='blue') 
button3 = Button(topFrame, text='Button 3', fg='green')
button4 = Button(bottomFrame, text='Button 3', fg='purple')

button1.pack(side=LEFT) # Things automatically stack vertically - explicitly specify alignment of objects
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

# Has the GUI window continuously on the screen (without this, the computer will flash the window on the screen and close it out)
root.mainloop()