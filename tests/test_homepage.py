import pytest
from pages.Homepage import HomePage


def test_search_item(driver):
    search_item_input = HomePage(driver)
    search_item_input.search_item("ber")

    # Wait for the product name to load, then validate it
    product_name = search_item_input.get_product_name().lower()
    assert "ber" in product_name


def test_search_and_add(driver):
    search_item_name = HomePage(driver)
    search_item_name.search_item("berry")
    search_item_name.increment_item()  # Increment the product quantity


def test_search_and_cart(driver):
    search_product = HomePage(driver)
    search_product.search_item("cucumber")


    product_name = search_product.get_product_name().lower()
    assert "cucumber" in product_name

    search_product.add_to_cart()  # Add the product to the cart
