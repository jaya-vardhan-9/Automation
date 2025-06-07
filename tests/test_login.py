from pages.login_page import LoginPage

def test_login_successfully(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("Admin", "admin123")

    page.wait_for_selector("text=Dashboard")
    assert "dashboard" in page.url.lower()
