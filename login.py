import customtkinter
from PIL import Image
import iracing_calls
import models.login as loginModel
import main

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("300x300")
app.title("iRacing OBS Extensions")
app.resizable(False, False)

def login():
    loginModel.username = username_entry.get()
    loginModel.password = password_entry.get()
    try:
        iracing_calls.try_login()
        app.withdraw()
        main.show_main_window()
    except Exception as e:
        print(e)


image = Image.open("images/iracing.png")
image = image.resize((225, 50))
imageCtk = customtkinter.CTkImage(image, image, (225, 40))
imageLabel = customtkinter.CTkLabel(app, image=imageCtk, text="")
imageLabel.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)

username_entry = customtkinter.CTkEntry(app, placeholder_text="Username")
username_entry.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

password_entry = customtkinter.CTkEntry(app, placeholder_text="Password", show="*")
password_entry.place(relx=0.5, rely=0.55, anchor=customtkinter.CENTER)

button = customtkinter.CTkButton(app, text="Click me", command=login)
button.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

save_login = customtkinter.CTkCheckBox(app, text="Save login")
save_login.place(relx=0.5, rely=0.85, anchor=customtkinter.CENTER)

app.mainloop()
