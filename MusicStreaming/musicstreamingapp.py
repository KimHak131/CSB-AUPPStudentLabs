"""
You are part of a team developing a new music streaming app called "MFun." Your task is to design the core functionality that manages the user's music library and playlist creation. Consider the following requirements:

Music library:
Needs to store a collection of songs and their associated metadata (title, artist, album, genre, length).
Must efficiently retrieve songs by various criteria (artist, album, genre, title).
Must prevent duplicate song entries.

Playlists:
Users can create unlimited playlists.
Each playlist can contain any number of songs, but a song cannot be added multiple times to the same playlist.
Songs can be added, removed, or reordered within playlists.
The app should display songs in the order they were added to the playlist.

Which data structure model(s) would you choose to implement the music library and playlist features? Explain your choices, considering the characteristics of each data structure and the specific requirements of the application.

Data structures to consider:
       Tuples, Sets, Lists, Dictionaries, Trees, Graphs, Stacks, Queues
"""
# Prototype code, you can follow different implementation process

# Using tuples as data structures
import pandas as pd
import csv

class Song:
    def __init__(self, title, artist, album, genre, length):
        self.title = title
        self.artist = artist 
        self.album = album
        self.genre = genre
        self.length = length

# Inside the MusicLibrary class

class MusicLibrary:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.load_library()

    def load_library(self):
        try:
            # Load songs and playlists from CSV file
            df_songs = pd.read_csv(self.csv_file)
            self.library = df_songs.values.tolist()
            self.playlists = []

            # Create indexes for efficient song retrieval
            self.artist_index = {}
            self.album_index = {}
            self.genre_index = {}
            self.title_index = {}

            for song_data in self.library:
                song = Song(*song_data)

                # Update indexes
                self.artist_index.setdefault(song.artist, []).append(song_data)
                self.album_index.setdefault(song.album, []).append(song_data)
                self.genre_index.setdefault(song.genre, []).append(song_data)
                self.title_index.setdefault(song.title, []).append(song_data)

        except FileNotFoundError:
            self.library = []
            self.playlists = []
            self.artist_index = {}
            self.album_index = {}
            self.genre_index = {}
            self.title_index = {}

    def save_library(self):
        # Save songs to CSV file
        df_songs = pd.DataFrame(self.library, columns=["Title", "Artist", "Album", "Genre", "Length"])
        df_songs.to_csv(self.csv_file, index=False)

    def add_song(self, song):
        song_tuple = (song.title, song.artist, song.album, song.genre, song.length)
        if song_tuple not in self.library:
            self.library.append(song_tuple)

            # Update indexes
            self.artist_index.setdefault(song.artist, []).append(song_tuple)
            self.album_index.setdefault(song.album, []).append(song_tuple)
            self.genre_index.setdefault(song.genre, []).append(song_tuple)
            self.title_index.setdefault(song.title, []).append(song_tuple)

            self.save_library()
            print(f"{song.title} added to your library")

    def add_playlist(self, playlist_name):
        playlist = Playlist(playlist_name)
        if playlist not in self.playlists:
            self.playlists.append(playlist)
            self.save_playlists_to_csv()  # Save playlists to CSV
            print(f"Playlist '{playlist_name}' added successfully.")
        else:
            print(f"Playlist '{playlist_name}' already exists.")
    
    def add_playlist(self, playlist_name):
        playlist = Playlist(playlist_name)
        if playlist not in self.playlists:
            self.playlists.append(playlist)
            self.save_playlists_to_csv()  # Save playlists to CSV
            print(f"Playlist '{playlist_name}' added successfully.")
            
            # Add songs to the playlist
            self.add_song_to_playlist(playlist)
        else:
            print(f"Playlist '{playlist_name}' already exists.")

    def save_playlists_to_csv(self):
        with open('playlists.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for playlist in self.playlists:
                for song in playlist.songs:
                    writer.writerow([song.title, song.artist, song.album, song.genre, song.length, playlist.name])
            
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

        # Update indexes
        self.artist_index = {}
        self.album_index = {}
        self.genre_index = {}
        self.title_index = {}

        for song_data in self.library:
            song = Song(*song_data)

            # Update indexes
            self.artist_index.setdefault(song.artist, []).append(song_data)
            self.album_index.setdefault(song.album, []).append(song_data)
            self.genre_index.setdefault(song.genre, []).append(song_data)
            self.title_index.setdefault(song.title, []).append(song_data)

        self.save_library()
        print(f"{title} removed from your library")


# Assuming you have a CSV file named 'playlist.csv'

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




# Create song examples
# song1 = Song("Song 1", "Artist 1", "Album 1", "Genre 1", 180)
# song2 = Song("Song 2", "Artist 2", "Album 2", "Genre 2", 210)

# # Add songs to the music library
# music_library.add_song(song1)
# music_library.add_song(song2)

# # Create a playlist
# playlist1 = Playlist("My Playlist 1")

# # Add songs to the playlist
# playlist1.add_song(song1)
# playlist1.add_song(song2)

# # Display the playlist
# playlist1.display_playlist()

# # Display songs by Artist 1
# songs_by_artist_1 = music_library.get_songs_by_artist("Artist 1")
# print("\nSongs by Artist 1:")
# for song in songs_by_artist_1:
    # print(f"{song.title} - {song.album}")


# Read data from CSV file and populate the music library

# Usage

# Display songs by Artist 1
# songs_by_artist_1 = music_library.get_songs_by_artist("Artist 1")
# print(f"\nSongs by Artist 1:")
# for song in songs_by_artist_1:
#     print(f"{song.title} - {song.album}")
# Main Requirement:
# Create song example
# Create a music library
# Add songs to the music library
# Get songs by artist
# Create playlists
# Add songs to playlists
# Display playlists
# Searching for songs by artist


# Sample Output:
# Playlist: My Playlist 1
# 1. Song 1 - Artist 1
# 2. Song 2 - Artist 2

# Songs by Artist 1:
# Song 1 - Album 1
