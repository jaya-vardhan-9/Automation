import time

class AdminPage:
    def __init__(self, page):
        self.page = page
        self.admin_menu = "a[href='/web/index.php/admin/viewAdminModule']"
        self.add_button = "button:has-text('Add')"
        self.user_role_dropdown = "(//div[@class='oxd-select-text-input'])[1]"
        self.user_role_option_admin = "//div[@role='option']//span[text()='Admin']"
        self.employee_name_input = "//input[@placeholder='Type for hints...']"
        self.status_dropdown = "(//div[@class='oxd-select-text-input'])[2]"
        self.status_option_enabled = "//div[@role='option']//span[text()='Enabled']"
        self.username_input = "(//input[@class='oxd-input oxd-input--active'])[2]"
        self.password_input = "(//input[@type='password'])[1]"
        self.confirm_password_input = "(//input[@type='password'])[2]"
        self.save_button = "button:has-text('Save')"

    def go_to_admin_page(self):
        self.page.click(self.admin_menu)
        self.page.wait_for_selector(self.add_button)

    def add_user(self, employee_name, username, password):
        self.page.click(self.add_button)
        self.page.wait_for_selector(self.user_role_dropdown)

        self.page.click(self.user_role_dropdown)
        self.page.click(self.user_role_option_admin)

        self.page.fill(self.employee_name_input, employee_name)
        time.sleep(1)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

        self.page.click(self.status_dropdown)
        self.page.click(self.status_option_enabled)

        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.fill(self.confirm_password_input, password)

        self.page.click(self.save_button)
        self.page.wait_for_timeout(2000)
