# tests/test_delete_user.py

from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_delete_user(page):
    login = LoginPage(page)
    login.load()
    login.login("Admin", "admin123")

    admin = AdminPage(page)
    admin.delete_user("john123")
