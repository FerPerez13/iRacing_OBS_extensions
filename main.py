import tkinter as tk
import login
import models.member_profile as m_profile
class Main_UI(tk.Frame):
    """Docstring."""
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title("Main Window")
        self.parent.resizable(False, False)

        # Create a label
        self.name = tk.Label(self.parent, text=m_profile.name)
        self.name.pack()

        # Create a label
        self.road_sr = tk.Label(self.parent, text="ROAD SR " + m_profile.sportscar_sr)
        self.road_sr.pack()

        # Create a label
        self.oval_sr = tk.Label(self.parent, text="OVAL SR " + m_profile.formula_sr)
        self.oval_sr.pack()

        # Create a label
        self.road = tk.Label(self.parent, text="ROAD " + m_profile.sportscar)
        self.road.pack()

        # Create a label
        self.oval = tk.Label(self.parent, text="OVAL " + m_profile.formula)
        self.oval.pack()

    def update_labels(self):
        self.name.config(text=m_profile.name)
        self.road_sr.config(text="ROAD SR " + m_profile.sportscar_sr)
        self.oval_sr.config(text="OVAL SR " + m_profile.formula_sr)
        self.road.config(text="ROAD " + m_profile.sportscar)
        self.oval.config(text="OVAL " + m_profile.formula)

def show_main_window():
    root = tk.Tk()
    root.geometry("500x500")
    app = Main_UI(parent=root)
    app.mainloop()
