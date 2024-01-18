# Importing required classes and modules
from musicstreamingapp import MusicLibrary, Playlist, Song

# Path to the CSV file for the music library
SONGS_CSV_FILE = 'library.csv'

# Create a music library instance with songs and playlists CSV files
music_library = MusicLibrary(SONGS_CSV_FILE)

# Main menu loop
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

    if choice == '1':
        # Add Song to Library
        title = input("Enter the song title: ")
        artist = input("Enter the artist: ")
        album = input("Enter the album: ")
        genre = input("Enter the genre: ")
        length = input("Enter the length: ")
        new_song = Song(title, artist, album, genre, length)
        music_library.add_song(new_song)

    elif choice == '2':
        # Create Playlist
        playlist_name = input("Enter the playlist name: ")
        music_library.add_playlist(playlist_name)

    elif choice == '3':
        # Delete Playlist
        playlist_name = input("Enter the playlist name to delete: ")
        music_library.delete_playlist(playlist_name)

    elif choice == '4':
        # Display Playlist
        playlist_name = input("Enter the playlist name to display: ")
        playlist = music_library.get_playlist_by_name(playlist_name)
        if playlist:
            playlist.display_playlist()
        else:
            print(f"Playlist '{playlist_name}' not found.")

    elif choice == '5':
        # Display Songs by Artist
        artist_name = input("Enter the artist name to display songs: ")
        songs_by_artist = music_library.get_songs_by_artist(artist_name)
        if songs_by_artist:
            print(f"\nSongs by {artist_name}:")
            for song in songs_by_artist:
                print(f"{song.title} - {song.album}")
        else:
            print(f"No songs found for {artist_name}.")

    elif choice == '6':
        # Delete Song from Library
        song_title = input("Enter the song title to delete: ")
        music_library.remove_song(song_title)

    elif choice == '7':
        # Exit
        print("Exiting the Music Library Menu. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
