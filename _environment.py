class Environment:

    def __init__(self, server_and_port):
        self.server_and_port = server_and_port
        self._user = 'none'
        self._password = 'none'

    @property
    def user(self):
        return self._user

    @property
    def password(self):
        return self._password

    @user.setter
    def user(self, value):
        self._user = value

    @password.setter
    def password(self, value):
        self._password = value

uat = Environment('uat')

environments = {}
environments['uat'] = uat