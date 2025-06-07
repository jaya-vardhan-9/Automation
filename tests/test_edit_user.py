# orangehrm-automation/tests/test_edit_user.py

from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_edit_user(page):
    login = LoginPage(page)
    login.load()
    login.login("Admin", "admin123")

    admin = AdminPage(page)
    admin.edit_user("john123", "ESS")  # change username if needed
