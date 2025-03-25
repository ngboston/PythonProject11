import os
import json
import hashlib
import time
import subprocess

class Song:
    def __init__(self, name, duration, author, format):
        self.name = name
        self.duration = duration
        self.author = author
        self.format = format

    def __str__(self):
        return f"{self.name} - {self.author} ({self.duration}) [{self.format}]"

class Library:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def delete_song(self, song_name):
        self.songs = [song for song in self.songs if song.name != song_name]

    def display_songs(self):
        if not self.songs:
            print("Library is empty.")
        else:
            for song in self.songs:
                print(song)

    def get_song_by_name(self, song_name):
        for song in self.songs:
            if song.name == song_name:
                return song
        return None

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song_name):
        self.songs = [song for song in self.songs if song.name != song_name]

    def display_playlist(self):
        if not self.songs:
            print(f"Playlist '{self.name}' is empty.")
        else:
            print(f"Playlist '{self.name}':")
            for song in self.songs:
                print(f"  - {song}")

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.playlists = {}

    def verify_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest() == self.password

class UserManager:
    def __init__(self, filename="users.json"):
        self.filename = filename
        self.users = self.load_users()

    def load_users(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                return {username: User(username, password) for username, password in data.items()}
        else:
            return {}

    def save_users(self):
        data = {user.username: user.password for user in self.users.values()}
        with open(self.filename, "w") as f:
            json.dump(data, f)

    def add_user(self, username, password):
        if username in self.users:
            return False
        self.users[username] = User(username, password)
        self.save_users()
        return True

    def get_user(self, username):
        return self.users.get(username)

def play_audio(filepath):
    try:
        if os.name == 'nt':
            os.startfile(filepath)
        elif os.name == 'posix':
            subprocess.Popen(['xdg-open', filepath])
        else:
            print("Unsupported operating system.")
    except Exception as e:
        print(f"Error playing audio: {e}")
def main():
    user_manager = UserManager()
    library = Library()

    library.add_song(Song("Song 1", "3:30", "Artist A", "mp3"))
    library.add_song(Song("Song 2", "4:15", "Artist B", "wav"))
    library.add_song(Song("Song 3", "2:50", "Artist C", "ogg"))

    current_user = None

    while True:
        if current_user:
            print(f"\nLogged in as {current_user.username}")
            print("1. Play Song")
            print("2. Create Playlist")
            print("3. View Playlists")
            print("4. Add Song to Playlist")
            print("5. Remove Song from Playlist")
            print("6. Library")
            print("7. Logout")
            choice = input("Enter your choice: ")

            if choice == "1":
                song_name = input("Enter song name to play: ")
                song = library.get_song_by_name(song_name)
                if song:
                    filepath = song.name + "." + song.format
                    if os.path.exists(filepath):
                        play_audio(filepath)
                    else:
                        print(f"File {filepath} does not exist.")
                else:
                    print("Song not found.")
            elif choice == "2":
                playlist_name = input("Enter playlist name: ")
                if playlist_name not in current_user.playlists:
                    current_user.playlists[playlist_name] = Playlist(playlist_name)
                    print(f"Playlist '{playlist_name}' created.")
                else:
                    print(f"Playlist '{playlist_name}' already exists.")

            elif choice == "3":
                if current_user.playlists:
                    for playlist in current_user.playlists.values():
                        playlist.display_playlist()
                else:
                    print("No playlists found.")

            elif choice == "4":
                playlist_name = input("Enter playlist name: ")
                song_name = input("Enter song name to add: ")
                song = library.get_song_by_name(song_name)
                if playlist_name in current_user.playlists and song:
                    current_user.playlists[playlist_name].add_song(song)
                    print(f"Song '{song_name}' added to playlist '{playlist_name}'.")
                else:
                    print("Playlist or song not found.")

            elif choice == "5":
                playlist_name = input("Enter playlist name: ")
                song_name = input("Enter song name to remove: ")
                if playlist_name in current_user.playlists:
                    current_user.playlists[playlist_name].remove_song(song_name)
                    print(f"Song '{song_name}' removed from playlist '{playlist_name}'.")
                else:
                    print("Playlist not found.")
            elif choice == "6":
                library.display_songs()
            elif choice == "7":
                current_user = None
            else:
                print("Invalid choice.")
        else:
            print("\n1. Login")
            print("2. Register")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                user = user_manager.get_user(username)
                if user and user.verify_password(password):
                    current_user = user
                    print("Login successful.")
                else:
                    print("Invalid username or password.")
            elif choice == "2":
                username = input("Username: ")
                password = input("Password: ")
                if user_manager.add_user(username, password):
                    print("Registration successful.")
                else:
                    print("Username already taken.")
            elif choice == "3":
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    main()