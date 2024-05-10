import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

loginWindow = ctk.CTk()
loginWindow.title("Welcome To Login")
loginWindow.geometry("1000x700")

def regiPage():
    loginWindow.destroy()
    import regi_mariadb_bcrypts

loginFrame = ctk.CTkFrame(loginWindow,
                          width=100,
                          height=100,
                          border_width=2,
                          fg_color=("#2A3132"),
                          border_color=("#90AFC5"))
loginFrame.pack(expand=True)

usernameLabel = ctk.CTkLabel(loginFrame,
                             text="Username:",
                             width=100,
                             height=50,
                             corner_radius=5,
                             text_color="#336B87",
                             font=("helvatica",30),
                             anchor="center")
usernameLabel.grid(row=0,
                   column=0,
                   padx=5,
                   pady=30)
usernameEntry = ctk.CTkEntry(loginFrame,
                             width=550,
                             placeholder_text="username please",
                             height=50,
                             corner_radius=5,
                             text_color="#A43820",
                             font=("helatica",30))
usernameEntry.grid(row=0,
                   column=1,
                   padx=20,
                   pady=30)

passwordLabel = ctk.CTkLabel(loginFrame,
                             text="Password:",
                             width=100,
                             height=50,
                             corner_radius=5,
                             text_color="#336B87",
                             font=("helvatica",30),
                             anchor="center")
passwordLabel.grid(row=1,
                   column=0,
                   padx=5,
                   pady=30)
passwordEntry = ctk.CTkEntry(loginFrame,
                             width=550,
                             placeholder_text="password please",
                             height=50,
                             corner_radius=5,
                             text_color="#A43820",
                             font=("helatica",30),
                             show="*")
passwordEntry.grid(row=1,
                   column=1,
                   padx=20,
                   pady=30)

loginButton = ctk.CTkButton(loginFrame,
                            text="Login",
                            height=30,
                            width=250,
                            border_width=5,
                            border_spacing=5,
                            fg_color="#34A853",
                            border_color="black",
                            text_color="black",
                            font=("Helvatica",30),
                            hover=True)
loginButton.grid(row=2,
                 columnspan=2,
                 padx=0,
                 pady=(5,10))
regiButton = ctk.CTkButton(loginFrame,
                           text="Registration",
                           height=30,
                           width=250,
                           border_width=5,
                           border_spacing=5,
                           fg_color="#BA5536",
                           border_color="black",
                           text_color="black",
                           font=("Helvatica",30),
                           hover=True,
                           command=regiPage)
regiButton.grid(row=3,
                columnspan=2,
                padx=0,
                pady=(5,10),
                )

loginWindow.mainloop()
