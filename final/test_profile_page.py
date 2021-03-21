import time

import pytest

from final.pages.main_page import MainPage
from final.pages.profile_page import ProfilePage, EditProfilePage, DeleteProfilePage

main_page_url = "http://selenium1py.pythonanywhere.com/"
profile_page_url = "http://selenium1py.pythonanywhere.com/accounts/profile/"


class TestProfilePage:

    @pytest.mark.parametrize("first_name, last_name", [
        ("edited_first_name", "edited_last_name"),
        ("edited_first_name", ""),
        ("", "edited_last_name"),
        ("", "")])
    def test_user_can_edit_profile_name(self, browser, register_new_user, first_name, last_name):
        # Arrange
        register_new_user()
        main_page = MainPage(browser, "http://selenium1py.pythonanywhere.com/")
        main_page.go_to_account_page()

        # Act
        profile_page = ProfilePage(browser, browser.current_url)
        profile_page.go_to_edit_profile()
        edit_profile_page = EditProfilePage(browser, browser.current_url)
        edit_profile_page.edit_name(first_name, last_name)

        # Assert
        profile_page.should_be_profile_updated_message()

    def test_user_can_delete_profile(self, browser, register_new_user):
        # Arrange
        email, password = register_new_user()
        main_page = MainPage(browser, "http://selenium1py.pythonanywhere.com/")
        main_page.go_to_account_page()

        # Act
        profile_page = ProfilePage(browser, browser.current_url)
        profile_page.go_to_delete_profile()
        delete_profile_page = DeleteProfilePage(browser, browser.current_url)
        delete_profile_page.confirm_delete_profile(password)

        # Assert
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_deleted_profile_message()