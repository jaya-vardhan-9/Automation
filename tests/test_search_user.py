# orangehrm-automation/tests/test_search_user.py

from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_search_user(page):
    login = LoginPage(page)
    login.load()
    login.login("Admin", "admin123")

    admin = AdminPage(page)
    admin.search_user("john123")  # change if your username is different

    assert page.locator("div.oxd-table-row").is_visible()
