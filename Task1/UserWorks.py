import json
from Users import User
from Errors import AccesErorr, LevelError


class UserWorkshop:
    user_list = set()

    def __init__(self):
        UserWorkshop.load_users()
        pass

    @staticmethod
    def load_users(path: str = 'users.json'):
        with open(path, 'r', encoding='UTF-8') as f:
            user_dict = json.load(f)
        for level, user_list in user_dict.items():
            for id, name in user_list.items():
                UserWorkshop.user_list.add(User(name, str(id), str(level)))

    def login(self, name: str, id: str) -> str:
        login_user = User(name, id)
        for user in UserWorkshop.user_list:
            if login_user == user:
                return user.level
        else:
            raise AccesErorr()

    def create_user(self, name: str, id: str, level: str):
        cur_name, cur_id = input("Введите имя авторизированного пользователя и его id через пробел").split()        #авторизация пользователя (который есть в базе)
        if current_level := self.login(cur_name, cur_id):
            if int(current_level) > int(level):
                return User(name, id, level)
            else:
                raise LevelError(current_level, level)


