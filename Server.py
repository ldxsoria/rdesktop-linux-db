class Server:

    def __init__(self,name,ip,username,password):
        self._name = name
        self._ip = ip
        self._username = username
        self._password = password

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, name):
            self._name = name


        @property
        def ip(self):
            return self._ip

        @ip.setter
        def ip(self, ip):
            self._ip = ip


        @property
        def username(self):
            return self._username

        @username.setter
        def username(self, username):
            self._username = username


        @property
        def password(self):
            return self._password

        @password.setter
        def password(self, password):
            self._password = password

    def __str__(self):
        return f'IP:{self._ip}Username:{self._username} Password: {self._password}'


if __name__ == '__main__':
    server1 = Server('wten','192.6.31.46','soporte@maristas.local','C0mpaq')
    print(server1)
