#!/usr/bin/env python3

import socket
import threading
import subprocess
import platform

# Function to handle media keys using xdotool
def handle_media_key(key):
    if key == 'play_pause':
        subprocess.run(['xdotool', 'key', 'XF86AudioPlay'])
    elif key == 'next':
        subprocess.run(['xdotool', 'key', 'XF86AudioNext'])
    elif key == 'previous':
        subprocess.run(['xdotool', 'key', 'XF86AudioPrev'])
    elif key == 'volume_up':
        subprocess.run(['xdotool', 'key', 'XF86AudioRaiseVolume'])
    elif key == 'volume_down':
        subprocess.run(['xdotool', 'key', 'XF86AudioLowerVolume'])
    elif key == 'volume_mute':
        subprocess.run(['xdotool', 'key', 'XF86AudioMute'])

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
    # Send the server's hostname to the client
    hostname = socket.gethostname()
    client_socket.send(hostname.encode('utf-8'))

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                if message in ['play_pause', 'next', 'previous', 'volume_up', 'volume_down', 'volume_mute']:
                    handle_media_key(message)
                    client_socket.send(b'OK')
                elif message == 'get_song':
                    song = get_currently_playing_song()
                    client_socket.send(song.encode('utf-8'))
                elif message == 'exit':
                    break
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

