# tests/test_add_duplicate_user.py

from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_add_duplicate_user(page):
    login = LoginPage(page)
    login.load()
    login.login("Admin", "admin123")

    admin = AdminPage(page)
    admin.try_add_duplicate_user("Admin")  # This user already exists
