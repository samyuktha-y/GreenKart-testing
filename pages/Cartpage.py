from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_button = (By.CSS_SELECTOR, "img[alt='Cart']")
        self.proceed_button = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")

    def open_cart(self):
        self.driver.find_element(*self.cart_button).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*self.cart_button).click()
        # Wait until the Proceed button is clickable
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.proceed_button)
        )
        self.driver.find_element(*self.proceed_button).click()
