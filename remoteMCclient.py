import socket
import argparse

def send_media_key(client_socket, key):
    client_socket.send(key.encode('utf-8'))

def get_currently_playing_song(client_socket):
    client_socket.send('get_song'.encode('utf-8'))
    song = client_socket.recv(1024).decode('utf-8')
    return song

def get_server_hostname(client_socket):
    hostname = client_socket.recv(1024).decode('utf-8')
    return hostname

def main(host, port, command):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Get the server's hostname
    server_hostname = get_server_hostname(client_socket)
    print(f"Server hostname: {server_hostname}")

    if command == 'play_pause':
        send_media_key(client_socket, 'play_pause')
    elif command == 'next':
        send_media_key(client_socket, 'next')
    elif command == 'previous':
        send_media_key(client_socket, 'previous')
    elif command == 'volume_up':
        send_media_key(client_socket, 'volume_up')
    elif command == 'volume_down':
        send_media_key(client_socket, 'volume_down')
    elif command == 'volume_mute':
        send_media_key(client_socket, 'volume_mute')
    elif command == 'get_song':
        song = get_currently_playing_song(client_socket)
        print(f"Currently playing: {song}")

    send_media_key(client_socket, 'exit')
    client_socket.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Remote Media Control Client')
    parser.add_argument('--host', default='localhost', help='Server hostname or IP address')
    parser.add_argument('--port', type=int, default=63342, help='Server port number')
    parser.add_argument('command', choices=['play_pause', 'next', 'previous', 'volume_up', 'volume_down', 'volume_mute', 'get_song'], help='Command to send to the server')

    args = parser.parse_args()
    main(args.host, args.port, args.command)

