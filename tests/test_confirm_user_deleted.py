# tests/test_confirm_user_deleted.py

from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_confirm_user_deleted(page):
    login = LoginPage(page)
    login.load()
    login.login("Admin", "admin123")

    admin = AdminPage(page)
    user_still_exists = admin.is_user_present("john123")

    assert user_still_exists is False
