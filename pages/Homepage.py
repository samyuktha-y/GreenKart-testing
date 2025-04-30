from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.search_bar = (By.XPATH, "//input[@class='search-keyword']")
        self.search_button = (By.CSS_SELECTOR, "button[class='search-button']")
        self.add_quantity = (By.XPATH, "//a[@class='increment']")
        self.product_name = (By.XPATH, "//h4[@class='product-name']")
        self.add_to_cart_button = (By.XPATH, "//button[text()='ADD TO CART']")

    def search_item(self, input_value):
        self.driver.find_element(*self.search_bar).clear()
        self.driver.find_element(*self.search_bar).send_keys(input_value)
        self.driver.find_element(*self.search_button).click()

        # Wait until product name contains the searched text
        input_value_lower = input_value.lower()

        WebDriverWait(self.driver, 10).until(
            lambda driver: input_value_lower in driver.find_element(*self.product_name).text.lower()
        )

        # Now locate the product freshly
        product_element = self.driver.find_element(*self.product_name)
        product_text = product_element.text.lower()

        print(f"DEBUG: Product Text: {product_text}")

        assert input_value_lower in product_text, f"Expected '{input_value_lower}' in '{product_text}'"

    def increment_item(self):
        self.driver.find_element(*self.add_quantity).click()

    def add_to_cart(self):
        # Wait until the Add to Cart button is clickable
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.add_to_cart_button)
        )
        self.driver.find_element(*self.add_to_cart_button).click()

    def get_product_name(self):
        # Wait until product name is visible before returning text
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.product_name)
        )
        return self.driver.find_element(*self.product_name).text


