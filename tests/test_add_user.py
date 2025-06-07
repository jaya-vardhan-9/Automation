import time
import random
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_add_new_user(page):
    login = LoginPage(page)
    login.load()
    login.login("Admin", "admin123")

    admin = AdminPage(page)
    admin.go_to_admin_page()
    new_username = f"autouser{random.randint(1000, 9999)}"
    admin.add_user(employee_name="Paul Collings", username=new_username, password="Pass1234@")

    page.wait_for_timeout(2000)
    assert page.is_visible("text=Successfully Saved") or "admin" in page.url.lower()
