import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.title("Welcome To Registration")
window.geometry("1000x700")

regiFrame = ctk.CTkFrame(window,
                          width=100,
                          height=100,
                          border_width=2,
                          fg_color=("#2A3132"),
                          border_color=("#90AFC5"))
regiFrame.pack(expand=True)

nameLabel = ctk.CTkLabel(regiFrame,
                             text="Name:",
                             width=100,
                             height=50,
                             corner_radius=5,
                             text_color="#336B87",
                             font=("helvatica",30),
                             anchor="center")
nameLabel.grid(row=0,
                   column=0,
                   padx=5,
                   pady=30)
nameEntry = ctk.CTkEntry(regiFrame,
                             width=550,
                             placeholder_text="name please",
                             height=50,
                             corner_radius=5,
                             text_color="#A43820",
                             font=("helatica",30))
nameEntry.grid(row=0,
                   column=1,
                   padx=20,
                   pady=30)


usernameLabel = ctk.CTkLabel(regiFrame,
                             text="Username:",
                             width=100,
                             height=50,
                             corner_radius=5,
                             text_color="#336B87",
                             font=("helvatica",30),
                             anchor="center")
usernameLabel.grid(row=1,
                   column=0,
                   padx=5,
                   pady=30)
usernameEntry = ctk.CTkEntry(regiFrame,
                             width=550,
                             placeholder_text="username please",
                             height=50,
                             corner_radius=5,
                             text_color="#A43820",
                             font=("helatica",30))
usernameEntry.grid(row=1,
                   column=1,
                   padx=20,
                   pady=30)

passwordLabel = ctk.CTkLabel(regiFrame,
                             text="Password:",
                             width=100,
                             height=50,
                             corner_radius=5,
                             text_color="#336B87",
                             font=("helvatica",30),
                             anchor="center")
passwordLabel.grid(row=2,
                   column=0,
                   padx=5,
                   pady=30)
passwordEntry = ctk.CTkEntry(regiFrame,
                             width=550,
                             placeholder_text="password please",
                             height=50,
                             corner_radius=5,
                             text_color="#A43820",
                             font=("helatica",30),
                             show="*")
passwordEntry.grid(row=2,
                   column=1,
                   padx=20,
                   pady=30)

confirmpasswordLabel = ctk.CTkLabel(regiFrame,
                             text="Confirm password:",
                             width=100,
                             height=50,
                             corner_radius=5,
                             text_color="#336B87",
                             font=("helvatica",30),
                             anchor="center")
confirmpasswordLabel.grid(row=3,
                   column=0,
                   padx=5,
                   pady=30)
confirmpasswordEntry = ctk.CTkEntry(regiFrame,
                             width=550,
                             placeholder_text="confirm password please",
                             height=50,
                             corner_radius=5,
                             text_color="#A43820",
                             font=("helatica",30),
                             show="*")
confirmpasswordEntry.grid(row=3,
                   column=1,
                   padx=20,
                   pady=30)

emailLabel = ctk.CTkLabel(regiFrame,
                             text="Email:",
                             width=100,
                             height=50,
                             corner_radius=5,
                             text_color="#336B87",
                             font=("helvatica",30),
                             anchor="center")
emailLabel.grid(row=4,
                   column=0,
                   padx=5,
                   pady=30)
emailEntry = ctk.CTkEntry(regiFrame,
                             width=550,
                             placeholder_text="email please",
                             height=50,
                             corner_radius=5,
                             text_color="#A43820",
                             font=("helatica",30))
emailEntry.grid(row=4,
                   column=1,
                   padx=20,
                   pady=30)


loginButton = ctk.CTkButton(regiFrame,
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
loginButton.grid(row=6,
                 columnspan=2,
                 padx=0,
                 pady=(5,10))
regiButton = ctk.CTkButton(regiFrame,
                           text="Registration",
                           height=30,
                           width=250,
                           border_width=5,
                           border_spacing=5,
                           fg_color="#BA5536",
                           border_color="black",
                           text_color="black",
                           font=("Helvatica",30),
                           hover=True)
regiButton.grid(row=5,
                columnspan=2,
                padx=0,
                pady=(5,10))

window.mainloop()
