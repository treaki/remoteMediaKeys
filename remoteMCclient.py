import socket

def send_media_key(host, port, key):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client.send(key.encode('utf-8'))
    client.close()

def get_currently_playing_song(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client.send('get_song'.encode('utf-8'))
    song = client.recv(1024).decode('utf-8')
    client.close()
    return song

if __name__ == "__main__":
    host = 'localhost'  # Change to the server's IP address
    port = 73381

    # Send media key event
    send_media_key(host, port, 'play_pause')

    # Get currently playing song
    song = get_currently_playing_song(host, port)
    print(f"Currently playing: {song}")

