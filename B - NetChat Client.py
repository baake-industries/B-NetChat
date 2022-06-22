import socket
import threading

print('B - NetChat Client ver 1.8')
print('(c) copyright 2022 Baake Industries, Inc.')
print('~')
print('           @@@@@@')
print('       @@@@@@@@@@@@')
print('   @@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@    @@@@@@@')
print(' @@@@@@@      @@@@@@')
print('  @@@@@@   @@@@@@@@')
print('   @@@@@@@@@@@@@@@@@@@@')
print('    @@@@@@@@@@    @@@@@@@@')
print('     @@@@@@@      @@@@@@@@')
print('      @@@@@@   @@@@@@@@@@@')
print('       @@@@@@@@@@@@@@@@')
print('        @@@@@@@@@@@@')
print('         @@@@@@@@')
print('~')

class Client:
    def __init__(self):
        self.create_connection()

    def create_connection(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        self.username = input('Your pseudonym : ')
        print('Waiting for server ...')

        while 1:

            try:
                host = '82.64.124.73'
                port = 8088
                self.s.connect((host,port))
                print('Done.')
                print('~')
                print('Welcome to B - NetChat ! ')
                print('~')
                break

            except:
                print("Couldn't connect to server.")

        self.s.send(self.username.encode())
        message_handler = threading.Thread(target=self.handle_messages,args=())
        message_handler.start()
        input_handler = threading.Thread(target=self.input_handler,args=())
        input_handler.start()

    def handle_messages(self):

        while 1:
            print(self.s.recv(1204).decode())

    def input_handler(self):

        while 1:
            self.s.send((self.username+' - '+input()).encode())

client = Client()