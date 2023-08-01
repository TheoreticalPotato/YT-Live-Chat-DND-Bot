import customtkinter as ctk
import threading
from tts import *

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("800x600")
app.title("D&D Dashboard")

def startTTS():
    ttsThread = threading.Thread(target=tts)
    ttsThread.start()

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill="both", expand=True)

barbLabel = ctk.CTkLabel(master=frame, justify=ctk.LEFT, text="Barbarian", font=ctk.CTkFont(size=20, weight='bold'))
barbLabel.pack(pady=10, padx=10)
barbLabel.place(relx=0.08, rely=0.03)

barbChoose = ctk.CTkButton(master=frame, command=newBarb, text="Choose Barbarian")
barbChoose.pack(pady=10, padx=10)
barbChoose.place(relx=0.05, rely=0.1)


wizLabel = ctk.CTkLabel(master=frame, justify=ctk.LEFT, text="Wizard", font=ctk.CTkFont(size=20, weight='bold'))
wizLabel.pack(pady=10, padx=10)
wizLabel.place(relx=0.45, rely=0.03)

wizChoose = ctk.CTkButton(master=frame, command=newWiz, text="Choose Wizard")
wizChoose.pack(pady=10, padx=10)
wizChoose.place(relx=0.4, rely=0.1)


rogueLabel = ctk.CTkLabel(master=frame, justify=ctk.LEFT, text="Rogue", font=ctk.CTkFont(size=20, weight='bold'))
rogueLabel.pack(pady=10, padx=10)
rogueLabel.place(relx=0.8, rely=0.03)

rogueChoose = ctk.CTkButton(master=frame, command=newRogue, text="Choose Rogue")
rogueChoose.pack(pady=10, padx=10)
rogueChoose.place(relx=0.74, rely=0.1)


startButton = ctk.CTkButton(master=frame, command=startTTS, text="START")
startButton.place(relx=0.4, rely=0.5)

app.mainloop()