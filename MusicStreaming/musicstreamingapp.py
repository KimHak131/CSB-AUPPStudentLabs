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
import csv

class Song:
    def __init__(self, title, artist, album, genre, length):
        self.title = title
        self.artist = artist 
        self.album = album
        self.genre = genre
        self.length = length

class MusicLibrary:
    def __init__(self):
        self.library = {}

    def add_song(self, song):
        if song.title not in self.library:
            self.library[song.title] = song
      
    def get_songs_by_artist(self, artist):
        return [song for song in self.library.values() if song.artist == artist] 
    
    def get_songs_by_album(self, album):
        return [song for song in self.library.values() if song.album == album]
    def get_songs_by_genre(self, genre):
        return [song for song in self.library.values() if song.genre == genre]
    def get_songs_by_title(self, title):
        return [song for song in self.library.values() if song.title == title]
    
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
    def remove_song(self, song):
        if song in self.songs:
            self.songs.pop(song)
    def reorder_songs(self, new_order):
        if len(new_order) != len(self.songs) or len(set(new_order)) != len(new_order):
            print("Invalid order. Please provide a valid order.")
            return
        self.songs = [self.songs[i - 1] for i in new_order]
        
    def display_playlist(self):
        print(f"Playlist: {self.name}")
        for i, song in enumerate (self.songs, start=1):
            print(f"{i}. {song.title} - {song.artist}")


# Read data from CSV file and populate the music library
music_library = MusicLibrary()

with open('D:/Spring Y2/Computer Science B/CountEachLetter/CSB-AUPPStudentLabs/MusicStreaming/MusicLibrary.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        song = Song(
            title=row['Title'],
            artist=row['Artist'],
            album=row['Album'],
            genre=row['Genre'],
            length=int(row['Length'])
        )
        music_library.add_song(song)

# Create a playlist
my_playlist = Playlist("My Playlist 1")

# Add songs to the playlist
my_playlist.add_song(music_library.library['Just the Way You Are'])
my_playlist.add_song(music_library.library['Love The Way You Lie'])

# Display the playlist
my_playlist.display_playlist()

# Display songs by Artist 1
songs_by_artist_1 = music_library.get_songs_by_artist("Artist 1")
print(f"\nSongs by Artist 1:")
for song in songs_by_artist_1:
    print(f"{song.title} - {song.album}")
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
