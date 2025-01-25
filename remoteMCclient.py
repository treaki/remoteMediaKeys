#!/usr/bin/env python3

import socket
import argparse

def send_media_key(client_socket, key):
    client_socket.send(key.encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    return response

def get_currently_playing_song(client_socket):
    client_socket.send('get_song'.encode('utf-8'))
    song = client_socket.recv(1024).decode('utf-8')
    return song

def get_server_hostname(client_socket):
    hostname = client_socket.recv(1024).decode('utf-8')
    return hostname

def main(host, port, commands):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Get the server's hostname
    server_hostname = get_server_hostname(client_socket)
    print(f"Server hostname: {server_hostname}")

    for command in commands:
        if command in ['play_pause', 'next', 'previous', 'volume_up', 'volume_down', 'volume_mute']:
            response = send_media_key(client_socket, command)
            print(f"Command '{command}' sent. Response: {response}")
        elif command == 'get_song':
            song = get_currently_playing_song(client_socket)
            print(f"Currently playing: {song}")

    client_socket.send('exit'.encode('utf-8'))
    client_socket.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Remote Media Control Client')
    parser.add_argument('--host', default='localhost', help='Server hostname or IP address')
    parser.add_argument('--port', type=int, default=63342, help='Server port number')
    parser.add_argument('commands', nargs='+', choices=['play_pause', 'next', 'previous', 'volume_up', 'volume_down', 'volume_mute', 'get_song'], help='Commands to send to the server')

    args = parser.parse_args()
    main(args.host, args.port, args.commands)

