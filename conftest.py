import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service



@pytest.fixture
def driver():
    service_obj = Service("C:\\Users\\Samyuktha\\Documents\\chrome driver\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.implicitly_wait(5)

    assert "GreenKart" in driver.title

    yield driver

    driver.quit()