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

def get_server_hostname(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    hostname = client.recv(1024).decode('utf-8')
    client.close()
    return hostname

if __name__ == "__main__":
    host = 'localhost'  # Initial connection to get the server's hostname
    port = 63342

    # Get the server's hostname
    server_hostname = get_server_hostname(host, port)
    print(f"Server hostname: {server_hostname}")

    # Use the server's hostname to send media key event
    send_media_key(server_hostname, port, 'play_pause')

    # Example: Send volume up command
    send_media_key(server_hostname, port, 'volume_up')

    # Example: Send volume down command
    send_media_key(server_hostname, port, 'volume_down')

    # Example: Send mute command
    send_media_key(server_hostname, port, 'volume_mute')

    # Get currently playing song
    song = get_currently_playing_song(server_hostname, port)
    print(f"Currently playing: {song}")

