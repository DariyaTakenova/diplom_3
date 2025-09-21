import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from data import Data


@allure.feature("Навигация")
class TestNavigation:

    @allure.story("Переход в личный кабинет")
    def test_go_to_profile(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        with allure.step("Войти в аккаунт"):
            main_page.click_login_button()
            login_page.login(Data.REGISTERED_EMAIL, Data.VALID_PASSWORD)

        with allure.step("Перейти в личный кабинет"):
            main_page.click_profile_button()

        with allure.step("Проверить, что открылась страница профиля"):
            assert profile_page.is_profile_page_opened(), "Не открылся личный кабинет"

    @allure.story("Переход из личного кабинета в конструктор")
    def test_go_from_profile_to_constructor(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        with allure.step("Войти в аккаунт и перейти в профиль"):
            main_page.click_login_button()
            login_page.login(Data.REGISTERED_EMAIL, Data.VALID_PASSWORD)
            main_page.click_profile_button()

        with allure.step("Перейти в конструктор"):
            profile_page.click_constructor_button()

        with allure.step("Проверить, что открылся конструктор"):
            assert main_page.is_constructor_opened(), "Конструктор не открылся из профиля"

    @allure.story("Переход по клику на логотип Stellar Burgers")
    def test_go_to_main_from_profile_by_logo(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        with allure.step("Войти и перейти в личный кабинет"):
            main_page.click_login_button()
            login_page.login(Data.REGISTERED_EMAIL, Data.VALID_PASSWORD)
            main_page.click_profile_button()

        with allure.step("Кликнуть на логотип Stellar Burgers"):
            profile_page.click_logo()

        with allure.step("Проверить, что открылась главная страница"):
            assert main_page.is_main_page_opened(), "Главная страница не открылась по клику на логотип"

    @allure.story("Выход из аккаунта")
    def test_logout(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        with allure.step("Войти и перейти в личный кабинет"):
            main_page.click_login_button()
            login_page.login(Data.REGISTERED_EMAIL, Data.VALID_PASSWORD)
            main_page.click_profile_button()

        with allure.step("Нажать кнопку 'Выход'"):
            profile_page.click_logout_button()

        with allure.step("Проверить, что открылась форма входа"):
            assert login_page.is_login_form_visible(), "Форма входа не открылась после выхода"
