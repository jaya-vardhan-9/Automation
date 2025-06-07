class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = "input[name='username']"
        self.password_input = "input[name='password']"
        self.login_button = "button[type='submit']"

    def load(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.page.wait_for_selector(self.username_input, timeout=30000)

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

