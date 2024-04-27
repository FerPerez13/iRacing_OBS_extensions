import threading

import customtkinter

import iracing_calls

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

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


def show_main_window():
    def switch_event():
        timer_thread = TimerThread(60)
        progress_bar_update.set(0)
        if switch.get() == "on":
            timer_thread.start()
            progress_bar_update.start()
        else:
            timer_thread.stop()
            progress_bar_update.stop()

    app = customtkinter.CTk()
    app.geometry("900x400")
    app.title("iRacing OBS Extensions")
    app.resizable(False, False)

    profile_stats_label = customtkinter.CTkLabel(app, text="Estadisticas piloto")
    profile_stats_label.place(relx=0.1, rely=0.1, anchor=customtkinter.CENTER)

    switch_var = customtkinter.StringVar(value="off")
    switch = customtkinter.CTkSwitch(app, text="auto", command=switch_event, variable=switch_var, onvalue="on",
                                     offvalue="off")
    switch.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

    progress_bar_update = customtkinter.CTkProgressBar(app, orientation="horizontal")
    progress_bar_update.place(relx=0.65, rely=0.1, anchor=customtkinter.CENTER)

    button_force_update = customtkinter.CTkButton(app, text="Force Update",
                                                  command=iracing_calls.update_member_profile)
    button_force_update.place(relx=0.9, rely=0.1, anchor=customtkinter.CENTER)

    app.mainloop()
