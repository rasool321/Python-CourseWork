import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("My First GUI")
window.geometry("300x200")

# Add a label
label = tk.Label(window, text="Hello Bestie!")
button = tk.Button(window,text='button')

label.pack()
button.pack()
# Run the app
window.mainloop()