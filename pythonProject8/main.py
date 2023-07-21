import os
from tkinter import *
from PIL import Image, ImageTk

# Define the GUI
root = Tk()
root.title("Part Image Viewer")
part_name_label = Label(root, text="Enter Part Name:")
part_name_label.pack(side=LEFT)
part_name_entry = Entry(root)
part_name_entry.pack(side=LEFT)

# Define the function for opening the image file
def open_image_file(event):
    part_name = part_name_entry.get()
    image_path = os.path.join("path/to/image/directory", part_name + ".jpg")
    image = Image.open(image_path)
    image.show(fullscreen=True)

# Define the event listener
part_name_entry.bind("<Return>", open_image_file)

# Run the program
root.mainloop()
