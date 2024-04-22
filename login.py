import tkinter as tk
from PIL import Image, ImageTk
import main
import iracing_calls
import models.login as login

class Login_UI(tk.Frame):
    """Docstring."""
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title("iRacing OBS Extensions - iRacing Authentication")
        self.parent.resizable(False, False)

        # Imagen de portada con una url de internet
        image = Image.open("images/iracing.png")
        image = image.resize((225, 50))
        self.image = ImageTk.PhotoImage(image)
        self.label = tk.Label(self.parent, image=self.image)
        self.label.pack()

        # Spacer
        self.spacer = tk.Label(self.parent, text="")
        self.spacer.pack()

        # Create username label and entry
        self.username_label = tk.Label(self.parent, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.parent)
        self.username_entry.pack()

        # Spacer
        self.spacer = tk.Label(self.parent, text="")
        self.spacer.pack()

        # Create password label and entry
        self.password_label = tk.Label(self.parent, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.parent, show="*")
        self.password_entry.pack()

        # Spacer
        self.spacer = tk.Label(self.parent, text="")
        self.spacer.pack()

        # Create login button
        self.login_button = tk.Button(self.parent, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        login.username = self.username_entry.get()
        login.password = self.password_entry.get()

        # Hide the login window
        iracing_calls.try_login()
        self.parent.withdraw()

if __name__ == "__main__":
    ROOT = tk.Tk()
    ROOT.geometry("300x300")
    APP = Login_UI(parent=ROOT)

    main.show_main_window()

    APP.mainloop()
    ROOT.destroy()
