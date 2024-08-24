import tkinter as tk

import tkinter as tk

def greet():
    if entry.get() == "":  # If no name is entered, ask for the name
        label.config(text="What is your name?")
    else:  # If a name is entered, greet the user
        user_input = entry.get()
        label.config(text=f"Hello, {user_input}!")

# Create the main window
root = tk.Tk()
root.title("My Tkinter App")

# Create a label
label = tk.Label(root, text="What is your name?")
label.pack()

# Create an entry widget
entry = tk.Entry(root)
entry.pack()

# Create a button
greet_button = tk.Button(root, text="Greet", command=greet)
greet_button.pack()

# Run the application
root.mainloop()