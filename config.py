import os


class Config(object):

    def getlocalip():
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 1))
        local_ip_address = s.getsockname()[0]
        return local_ip_address

    localip = getlocalip()
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SERVER_NAME = localip + ":8080"
    print(SERVER_NAME)