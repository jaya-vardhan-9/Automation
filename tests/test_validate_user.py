# orangehrm-automation/tests/test_validate_user.py

from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_validate_updated_user_role(page):
    login = LoginPage(page)
    login.load()
    login.login("Admin", "admin123")

    admin = AdminPage(page)
    role = admin.get_user_role_from_table("john123")  # use the username you edited

    assert role.strip() == "ESS"
