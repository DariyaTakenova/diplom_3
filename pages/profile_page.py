from pages.base_page import BasePage
from locators import ProfilePageLocators

class ProfilePage(BasePage):
    # Проверка отображения профиля
    def is_profile_visible(self):
        return self.is_visible(ProfilePageLocators.PROFILE_HEADER)
