import tkinter as tk
import sys


def show_message_in_gui(message, duration):
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.title("streamLink - Message")
    root.geometry("600x400")

    label = tk.Label(root, text=message, font=("Arial", 72), justify='center')
    label.pack(side='top', fill='both', expand=True)
    label.bind("<1>", quit)  # When messagebox is clicked the script will exit

    root.after(duration * 1000, root.destroy)
    root.mainloop()


def quit(event):
    sys.exit()
