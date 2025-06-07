# tests/test_logout.py

from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_logout(page):
    login = LoginPage(page)
    login.load()
    login.login("Admin", "admin123")

    # Open dropdown and click logout
    page.click("i.oxd-userdropdown-icon")
    page.click("a:has-text('Logout')")

    # Confirm we're back at the login page
    page.wait_for_selector("input[name='username']")
    assert page.url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
