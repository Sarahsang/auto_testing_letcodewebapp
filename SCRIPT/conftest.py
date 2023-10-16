
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Data.data import USERNAME, PASSWORD
from Base.base import BaseSetup

@pytest.fixture(scope="module")
def setup():
    """
    Pytest fixture to set up the WebDriver.
    
    Yields:
        WebDriver: The WebDriver instance.
    """
    try:
        driver = BaseSetup.initialize_driver()  # use BaseSetup for WebDriver
        driver.implicitly_wait(10)
        yield driver
    except Exception as e:
        print(f"Exception occurred during setup: {e}")
        raise
    finally:
        driver.quit()


@pytest.fixture(scope="function")
def login(setup):
    # Navigate to login page
    login_button = WebDriverWait(setup, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Sign In"))
    )
    login_button.click()

    # Input username using ActionChains
    username_field = WebDriverWait(setup, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    actions = ActionChains(setup)
    actions.move_to_element(username_field).click().send_keys(USERNAME).perform()

    # Input password using ActionChains
    password_field = WebDriverWait(setup, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_field.clear()
    actions = ActionChains(setup)
    actions.move_to_element(password_field).click().send_keys(PASSWORD).perform()

    # Click login
    login_submit = WebDriverWait(setup, 10).until(
        EC.presence_of_element_located((By.NAME, "signon"))
    )
    login_submit.click()

    # yield
    # # Logout
    # logout_button = WebDriverWait(setup, 10).until(
    #     EC.element_to_be_clickable((By.LINK_TEXT, "Sign Out"))
    # )
    # logout_button.click()
