import random
import string

BASE_URL = "https://stellarburgers.nomoreparties.site"

# Тестовые пользователи
VALID_EMAIL = "test_user@example.com"
VALID_PASSWORD = "Password123"
VALID_NAME = "TestUser"

INVALID_EMAIL = "invalid_email"
INVALID_PASSWORD = "123"

# Сообщения об ошибках
ERROR_INCORRECT_PASSWORD = "Некорректный пароль"
ERROR_INCORRECT_EMAIL = "Некорректный email"

# Функция для генерации уникального email
def generate_unique_email() -> str:
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return f"autotest_{random_string}@example.com"
