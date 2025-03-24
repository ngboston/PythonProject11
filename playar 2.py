import tkinter as tk
import pygame
from tkinter import filedialog, messagebox

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.playlist = []
        self.current_song = 0

    def add_song(self, song):
        self.playlist.append(song)

    def play(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_song])
            pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def stop(self):
        pygame.mixer.music.stop()

    def next_song(self):
        if self.playlist:
            self.current_song = (self.current_song + 1) % len(self.playlist)
            self.play()

    def previous_song(self):
        if self.playlist:
            self.current_song = (self.current_song - 1) % len(self.playlist)
            self.play()

class GUI:
    def __init__(self, player):
        self.player = player
        self.window = tk.Tk()
        self.window.title("Музичний плеєр")
        self.create_widgets()

    def create_widgets(self):
        self.play_button = tk.Button(self.window, text="Відтворити", command=self.play_song)
        self.play_button.pack()

        self.pause_button = tk.Button(self.window, text="Пауза", command=self.pause_song)
        self.pause_button.pack()

        self.stop_button = tk.Button(self.window, text="Стоп", command=self.stop_song)
        self.stop_button.pack()

        self.next_button = tk.Button(self.window, text="Наступна", command=self.next_song_gui)
        self.next_button.pack()

        self.previous_button = tk.Button(self.window, text="Попередня", command=self.previous_song_gui)
        self.previous_button.pack()

        self.add_button = tk.Button(self.window, text="Додати пісню", command=self.add_song_gui)
        self.add_button.pack()

    def play_song(self):
        self.player.play()

    def pause_song(self):
        self.player.pause()

    def stop_song(self):
        self.player.stop()

    def next_song_gui(self):
        self.player.next_song()

    def previous_song_gui(self):
        self.player.previous_song()

    def add_song_gui(self):
        song = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if song:
            self.player.add_song(song)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    player = MusicPlayer()
    gui = GUI(player)
    gui.run()