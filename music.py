from youtubesearchpython import VideosSearch
import webbrowser, random
import customtkinter as app

app.set_appearance_mode("dark")
window = app.CTk()
window.title("KayfiyatMusic")
window.geometry("400X350")

kayfiyatlar = {
    "xursand": "beliver",
    "xafa": "sad music",
    "energetik": "attantion",
    "charchagan": "relaxing music"
}

def play_video(query):
    video_id = VideosSearch(query, limit=5).result().get("result")[random.randrange(5)]["id"]
    youtube_video_url = f"https://www.youtube.com/watch?v={video_id}"
    webbrowser.open(youtube_video_url)

def start():
    kayfiyat = kayfiyat_tanlovi.get()
    play_video(kayfiyatlar.get(kayfiyat))


yozuv = app.CTkLabel(window, text="Kayfiyatingiz qanday?", font=("Arial", 18))
yozuv.pack(pady=20)

kayfiyat_tanlovi = app.StringVar()
for kayfiyat in kayfiyatlar.keys():
    radio_button = app.CTkRadioButton(window, text=kayfiyat, variable=kayfiyat_tanlovi,value=kayfiyat,
                                    font=("Arial", 16))
    radio_button.pack(anchor=app.CENTER, pady=10, padx=10)

play_button = app.CTkButton(window, text="Play")
play_button.pack(side=app.TOP, padx=90, pady=20)
play_button.configure(command=start)

window.mainloop()