
"""Сборщик классов страниц"""


class Index():
    """Модуль главной страницы"""
    def __init__(self):
        self.template = "index.html"
        self.title = "Дом"
        self.info = "ПАНЕЛЬ УПРАВЛЕНИЯ"
        self.temp = "-"
    
    def update(self):
        """Обновление данных в элементе класса"""
        pass

class Login():
    """Форма авторизации без регистрации"""
    def __init__(self):
        self.template = "login.html"
        self.title = "Авторизация"
        self.info = "Авторизация в систему дома"

class Help():
    """Модуль страницы помощи и аннотаций"""
    def __init__(self):
        self.template = "help.html"
        self.title = "Помощь"
        self.info = "Аннотации к функционалу сайта"
        

        