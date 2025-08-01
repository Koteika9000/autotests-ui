from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.focus() # Фокусируемся на поле ввода

    # После фокусировки в поле, команды для управления клавиатурой отдаются не локатору, а всей странице
 
    # Цикл по вводу символов
    for char in "user@gmail.com":
        page.keyboard.type(char, delay=100)

    # Выберем весь текст в поле (CTRL + A)
    page.keyboard.press("ControlOrMeta+A") # Такая команда для совместимости с MacOS

    page.wait_for_timeout(5000)