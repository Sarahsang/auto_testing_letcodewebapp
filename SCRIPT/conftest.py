import pytest
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

