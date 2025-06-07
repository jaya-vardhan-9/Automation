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
        self.page.wait_for_timeout(300000)

    def search_user(self, username):
        self.page.click("text=Admin")
        self.page.wait_for_selector("input[name='username']")
        self.page.fill("input[name='username']", username)
        self.page.click("button:has-text('Search')")
        self.page.wait_for_timeout(100000)  # give it time to render results

    def edit_user(self, username, new_role):
        self.search_user(username)
        self.page.click(f"text={username}")
        self.page.wait_for_selector("label:has-text('User Role')")
        self.page.click("label:has-text('User Role') + div")
        self.page.click(f"text={new_role}")
        self.page.click("button:has-text('Save')")
        self.page.wait_for_timeout(100000)

    def get_user_role_from_table(self, username):
        self.search_user(username)
        self.page.wait_for_selector("div.oxd-table-row")
        role_selector = f"div.oxd-table-cell:has-text('{username}') >> xpath=../../div[3]"
        return self.page.locator(role_selector).inner_text()
    
    def delete_user(self, username):
        self.search_user(username)
        self.page.wait_for_selector("div.oxd-table-row")
        self.page.click("i.oxd-icon.bi-trash")  # Trash icon
        self.page.wait_for_selector("button:has-text('Yes, Delete')")
        self.page.click("button:has-text('Yes, Delete')")
        self.page.wait_for_timeout(100000)

    def is_user_present(self, username):
        self.search_user(username)
        self.page.wait_for_timeout(100000)
        return self.page.locator("div.oxd-table-row").count() > 0

    def try_add_duplicate_user(self, username):
        # ✅ Wait for dashboard to fully load (very important on EC2/headless)
        self.page.wait_for_selector("h6:has-text('Dashboard')", timeout=10000)

        # ✅ Click on the "Admin" menu from sidebar
        self.page.click("span:has-text('Admin')")

        # ✅ Wait for Admin > User Management page to load
        self.page.wait_for_selector("h6:has-text('System Users')", timeout=10000)

        # ✅ Click the "Add" button
        self.page.click("button:has-text('Add')")
        self.page.wait_for_selector("h6:has-text('Add User')", timeout=10000)

        # ✅ Fill out the form
        self.page.fill("input[placeholder='Type for hints...']", "Paul Collings")
        self.page.wait_for_timeout(1000)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")

        self.page.locator("div.oxd-select-wrapper").nth(0).click()
        self.page.locator("div[role='option']:has-text('Admin')").click()

        self.page.fill("input[name='username']", username)
        self.page.fill("input[type='password']", "Admin123!")
        self.page.fill("input[type='password'] >> nth=1", "Admin123!")

        # ✅ Submit form
        self.page.click("button:has-text('Save')")

        # ✅ Wait for duplicate error
        self.page.wait_for_selector("span:has-text('Already exists')", timeout=10000)




    def get_duplicate_error(self):
        return self.page.locator("span.oxd-input-field-error-message").inner_text()
