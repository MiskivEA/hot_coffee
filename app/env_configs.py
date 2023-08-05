from environs import Env


class ProjectEnv:
    env = Env()
    env.read_env()

    def get_env(self, key):
        return self.env(key)


class DatabaseConfig(ProjectEnv):
    connection_string = 'postgresql+asyncpg://{0}:{1}@{2}:{3}/{4}'
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.__user = self.get_env('POSTGRES_USER')
        self.__password = self.get_env('POSTGRES_PASSWORD')
        self.__host = self.get_env('DB_HOST')
        self.__port = self.get_env('DB_PORT')
        self.__name = self.get_env('DB_NAME')

    def __str__(self):
        return f'DB_URL {self.__name}'

    def __call__(self):
        return f'{self.connection_string.format(*self.__dict__.values())}'


class JWTConfig(ProjectEnv):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.__secret = self.get_env('JWT_SECRET')

    def __call__(self, *args, **kwargs):
        return f'{self.__secret}'


class UserManagerSecret(ProjectEnv):

    def __init__(self):
        self.__secret = self.get_env('USER_MANAGER_SECRET')

    def __call__(self, *args, **kwargs):
        return f'{self.__secret}'


def get_db_url():
    db_conf = DatabaseConfig()
    return db_conf()


def get_jwt_secret():
    jwt_conf = JWTConfig()
    return jwt_conf()


def get_user_manager_secret():
    ums = UserManagerSecret()
    return ums()
