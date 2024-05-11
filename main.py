import threading

import customtkinter

import iracing_calls

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")


class ProfileTimerThread(threading.Thread):
    def __init__(self, interval):
        threading.Thread.__init__(self)
        self.interval = interval
        self.daemon = True  # Ensure thread ends when main program ends
        self.running = False

    def run(self):
        print("🟢 Start Profile Thread")
        self.running = True
        while self.running:
            iracing_calls.update_member_profile()
            threading.Event().wait(self.interval)

    def stop(self):
        print("🛑 Stop Profile Thread")
        self.running = False


class LastRaceTimerThread(threading.Thread):
    def __init__(self, interval):
        threading.Thread.__init__(self)
        self.interval = interval
        self.daemon = True  # Ensure thread ends when main program ends
        self.running = False

    def run(self):
        print("🟢 Start Last Race Thread")
        self.running = True
        while self.running:
            iracing_calls.get_last_results()
            threading.Event().wait(self.interval)

    def stop(self):
        print("🛑 Stop Last Race Thread")
        self.running = False


def show_main_window():
    def switch_profile_event():
        timer_thread = ProfileTimerThread(60)
        progress_bar_profile_update.set(0)
        if switch_profile.get() == "on":
            progress_bar_profile_update.start()
            timer_thread.start()
        else:
            progress_bar_profile_update.stop()
            timer_thread.stop()

    def switch_last_race_event():
        timer_thread = LastRaceTimerThread(60)
        progress_bar_last_race_update.set(0)
        if switch_last_race.get() == "on":
            progress_bar_last_race_update.start()
            timer_thread.start()
        else:
            progress_bar_last_race_update.stop()
            timer_thread.stop()

    app = customtkinter.CTk()
    app.geometry("900x400")
    app.title("iRacing OBS Extensions")
    app.resizable(False, False)

    # Profile Stats
    profile_stats_label = customtkinter.CTkLabel(app, text="Estadisticas piloto")
    profile_stats_label.place(relx=0.1, rely=0.1, anchor=customtkinter.CENTER)

    switch_profile_var = customtkinter.StringVar(value="off")
    switch_profile = customtkinter.CTkSwitch(
        app,
        text="auto",
        command=switch_profile_event,
        variable=switch_profile_var,
        onvalue="on",
        offvalue="off",
    )
    switch_profile.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

    progress_bar_profile_update = customtkinter.CTkProgressBar(
        app, orientation="horizontal"
    )
    progress_bar_profile_update.place(relx=0.65, rely=0.1, anchor=customtkinter.CENTER)

    button_force_update = customtkinter.CTkButton(
        app, text="Force Update", command=iracing_calls.update_member_profile
    )
    button_force_update.place(relx=0.9, rely=0.1, anchor=customtkinter.CENTER)

    # Last Race
    last_race_label = customtkinter.CTkLabel(app, text="Ultima carrera")
    last_race_label.place(relx=0.1, rely=0.2, anchor=customtkinter.CENTER)

    switch_last_race_var = customtkinter.StringVar(value="off")
    switch_last_race = customtkinter.CTkSwitch(
        app,
        text="auto",
        command=switch_last_race_event,
        variable=switch_last_race_var,
        onvalue="on",
        offvalue="off",
    )
    switch_last_race.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

    progress_bar_last_race_update = customtkinter.CTkProgressBar(
        app, orientation="horizontal"
    )
    progress_bar_last_race_update.place(
        relx=0.65, rely=0.2, anchor=customtkinter.CENTER
    )

    button_last_race_force_update = customtkinter.CTkButton(
        app, text="Force Update", command=iracing_calls.get_last_results
    )
    button_last_race_force_update.place(relx=0.9, rely=0.2, anchor=customtkinter.CENTER)

    app.mainloop()
