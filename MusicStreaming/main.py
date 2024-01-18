import pandas as pd
import csv

class Song:
    def __init__(self, title, artist, album, genre, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.length = length

class MusicLibrary:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.load_library()

    def load_library(self):
        try:
            df_songs = pd.read_csv(self.csv_file)
            self.library = df_songs.values.tolist()
            self.playlists = []
            self.build_indexes()
        except FileNotFoundError:
            self.library = []
            self.playlists = []
            self.build_indexes()

    def save_library(self):
        df_songs = pd.DataFrame(self.library, columns=["Title", "Artist", "Album", "Genre", "Length"])
        df_songs.to_csv(self.csv_file, index=False)

    def build_indexes(self):
        self.artist_index = {}
        self.album_index = {}
        self.genre_index = {}
        self.title_index = {}
        for song_data in self.library:
            song = Song(*song_data)
            self.artist_index.setdefault(song.artist, []).append(song_data)
            self.album_index.setdefault(song.album, []).append(song_data)
            self.genre_index.setdefault(song.genre, []).append(song_data)
            self.title_index.setdefault(song.title, []).append(song_data)

    def add_song(self, song):
        song_tuple = (song.title, song.artist, song.album, song.genre, song.length)
        if song_tuple not in self.library:
            self.library.append(song_tuple)
            self.build_indexes()
            self.save_library()
            print(f"{song.title} added to your library")

    def add_playlist(self, playlist_name):
        playlist = Playlist(playlist_name)
        if playlist not in self.playlists:
            self.playlists.append(playlist)

    def delete_playlist(self, playlist_name):
        playlist_to_delete = None
        for playlist in self.playlists:
            if playlist.name == playlist_name:
                playlist_to_delete = playlist
                break

        if playlist_to_delete:
            self.playlists.remove(playlist_to_delete)
            print(f"{playlist_name} deleted successfully.")
        else:
            print(f"{playlist_name} not found. Unable to delete.")

    def get_playlist_by_name(self, playlist_name):
        for playlist in self.playlists:
            if playlist.name == playlist_name:
                return playlist
        return None

    def get_songs_by_artist(self, artist):
        return [Song(*song_data) for song_data in self.artist_index.get(artist, [])]

    def get_songs_by_album(self, album):
        return [Song(*song_data) for song_data in self.album_index.get(album, [])]

    def get_songs_by_genre(self, genre):
        return [Song(*song_data) for song_data in self.genre_index.get(genre, [])]

    def get_songs_by_title(self, title):
        return [Song(*song_data) for song_data in self.title_index.get(title, [])]

    def remove_song(self, title):
        self.library = [song for song in self.library if song[0] != title]
        self.build_indexes()
        self.save_library()
        print(f"{title} removed from your library")

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, music_library, title):
        song = music_library.get_songs_by_title(title)
        if song:
            if song[0] not in self.songs:
                self.songs.append(song[0])
                print(f"{song[0].title} added to {self.name}")
            else:
                print(f"{song[0].title} is already in {self.name}")
        else:
            print(f"{title} not found in the music library. Please add the song to the library first.")

    def remove_song(self, title):
        for song in self.songs:
            if song.title == title:
                self.songs.remove(song)
                print(f"{title} removed from {self.name}")
                return
        print(f"{title} not found in {self.name}")

    def reorder_songs(self, new_order):
        if len(new_order) != len(self.songs) or len(set(new_order)) != len(new_order):
            print("Invalid order. Please provide a valid order.")
            return
        self.songs = [self.songs[i - 1] for i in new_order]

    def display_playlist(self):
        print(f"Playlist: {self.name}")
        for i, song in enumerate(self.songs, start=1):
            print(f"{i}. {song.title} - {song.artist}")

    def save_to_csv(self, csv_file):
        with open(csv_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for song in self.songs:
                writer.writerow([song.title, song.artist, song.album, song.genre, song.length, self.name])

# Example Usage:

# Specify the CSV file name
csv_file = "music_library.csv"

# Create an instance of MusicLibrary
music_library = MusicLibrary(csv_file)

# While loop for user interaction
while True:
    print("\n===== Music Library Menu =====")
    print("1. Add Song to Library")
    print("2. Create Playlist")
    print("3. Delete Playlist")
    print("4. Display Playlist")
    print("5. Display Songs by Artist")
    print("6. Delete Song from Library")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        title = input("Enter song title: ")
        artist = input("Enter artist name: ")
        album = input("Enter album name: ")
        genre = input("Enter genre: ")
        length = int(input("Enter song length (in seconds): "))
        new_song = Song(title, artist, album, genre, length)
        music_library.add_song(new_song)

    elif choice == "2":
        playlist_name = input("Enter playlist name: ")
        music_library.add_playlist(playlist_name)
        print(f"{playlist_name} playlist added to your library!")

    elif choice == "3":
        playlist_name = input("Enter the name of the playlist to delete: ")
        music_library.delete_playlist(playlist_name)

    elif choice == "4":
        playlist_name = input("Enter playlist name: ")
        playlist = music_library.get_playlist_by_name(playlist_name)

        if playlist:
            playlist.display_playlist()
        else:
            print(f"{playlist_name} not found. Please input the correct playlist name.")

    elif choice == "5":
        artist_name = input("Enter artist name: ")
        songs_by_artist = music_library.get_songs_by_artist(artist_name)
        print(f"\nSongs by {artist_name}:")
        for song in songs_by_artist:
            print(f"{song.title} - {song.album}")

    elif choice == "6":
        title_to_delete = input("Enter the title of the song to delete: ")
        music_library.remove_song(title_to_delete)
        print(f"{title_to_delete} removed from your library.")

    elif choice == "7":
        print("Exiting the Music Library. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
