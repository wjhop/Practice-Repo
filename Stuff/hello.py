import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hello World in Cursive")

# Create a label with cursive-style font
label = tk.Label(
    root,
    text="Hello World",
    font=("Lucida Handwriting", 32),  # Cursive-like font
    fg="black"
)
label.pack(pady=50, padx=50)

# Run the application
root.mainloop()
