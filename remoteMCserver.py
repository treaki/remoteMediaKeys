import socket
import threading
from pynput.keyboard import Controller
import platform

# Initialize keyboard controller
keyboard = Controller()

# Function to handle media keys
def handle_media_key(key):
    if key == 'play_pause':
        keyboard.press(keyboard.media_play_pause)
        keyboard.release(keyboard.media_play_pause)
    elif key == 'next':
        keyboard.press(keyboard.media_next)
        keyboard.release(keyboard.media_next)
    elif key == 'previous':
        keyboard.press(keyboard.media_previous)
        keyboard.release(keyboard.media_previous)

# Function to get currently playing song (placeholder)
def get_currently_playing_song():
    if platform.system() == 'Windows':
        # Placeholder for Windows implementation
        return "Windows: Currently playing song"
    elif platform.system() == 'Linux':
        # Placeholder for Linux implementation
        return "Linux: Currently playing song"
    else:
        return "Unsupported platform"

# Function to handle client connection
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                if message in ['play_pause', 'next', 'previous']:
                    handle_media_key(message)
                elif message == 'get_song':
                    song = get_currently_playing_song()
                    client_socket.send(song.encode('utf-8'))
            else:
                break
        except:
            break
    client_socket.close()

# Server setup
def start_server(host='0.0.0.0', port=63342):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()

