import tkinter as tk
import login
import models.member_profile as m_profile
import iracing_calls
import threading

class TimerThread(threading.Thread):
    def __init__(self, interval):
        threading.Thread.__init__(self)
        self.interval = interval
        self.daemon = True  # Ensure thread ends when main program ends
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            iracing_calls.update_member_profile()
            threading.Event().wait(self.interval)

    def stop(self):
        self.running = False

class Main_UI(tk.Frame):
    """Docstring."""
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title("Main Window")
        self.parent.resizable(False, False)

        # create label to display member profile
        self.member_profile_label = tk.Label(self.parent, text="Member Profile")
        self.member_profile_label.pack()

        # create button to start timer to update member profile
        self.start_button = tk.Button(self.parent, text="Start Process", command=self.start_member_profile_update_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(self.parent, text="Stop Process", command=self.stop_member_profile_update_timer)
        self.stop_button.pack()

        # create button to call iracing_calls.update_member_profile()
        self.update_button = tk.Button(self.parent, text="Update Member Profile", command=iracing_calls.update_member_profile)
        self.update_button.pack()

    def start_member_profile_update_timer(self):
        self.timer_thread = TimerThread(0)
        self.timer_thread.start()


    def stop_member_profile_update_timer(self):
        if self.timer_thread:
            self.timer_thread.stop()
            self.timer_thread = None

def show_main_window():
    root = tk.Tk()
    root.geometry("500x500")
    app = Main_UI(parent=root)
    app.mainloop()
