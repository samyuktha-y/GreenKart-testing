import pytest
from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.Cartpage import CartPage
from pages.Homepage import HomePage


def test_cart_page(driver):
    cart_page = CartPage(driver)
    cart_page.open_cart()

@pytest.mark.parametrize(
    ("search_text, expected_product"), [
    ("berry", "raspberry - 1/4 kg"),
    ("cucumber", "cucumber - 1 kg"),
    ("tomato", "tomato - 1 kg"),
])
def test_proceed(driver, search_text, expected_product):
    homepage = HomePage(driver)
    homepage.search_item(search_text)

    try:
        # Wait for product list to populate
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//h4"))
        )

        # Re-fetch list and check for expected product
        products = driver.find_elements(By.XPATH, "//h4")
        matched = False
        for p in products:
            try:
                if expected_product.lower() in p.text.lower():
                    print(f"DEBUG: Found matching product: {p.text}")
                    matched = True
                    break
            except StaleElementReferenceException:
                continue

        assert matched, f"{expected_product} not found in the product list"

    except TimeoutException:
        pytest.fail(f"Timed out waiting for products matching: {expected_product}")
