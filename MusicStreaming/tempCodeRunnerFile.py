def get_playlist_by_name(self, playlist_name):
        for playlist in self.playlists:
            if playlist.name == playlist_name:
                return playlist
        return None