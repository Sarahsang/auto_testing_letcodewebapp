from selenium import webdriver

class BaseSetup:

    @staticmethod
    def initialize_driver(browser="chrome"):
        """
        Initialize the WebDriver based on the browser choice.

        Args:
            browser (str): The browser to use ("chrome" or "firefox").

        Returns:
            WebDriver: The initialized WebDriver instance.

        Raises:
            ValueError: If the browser is not supported.
        """
        try:
            if browser == "chrome":
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"]) # disable automation info bar
                chrome_options.add_experimental_option('useAutomationExtension', False) # disable automation info bar
                chrome_options.add_argument("--disable-autofill-keyboard-accessory-view[8]") # disable autofill
                #chrome_options.add_argument('blink-settings=imagesEnabled=false')  # disable image loading
                #chrome_options.add_argument('--ignore-certificate-errors') # ignore certificate errors
                #chrome_options.add_argument('--headless') # run in headless mode
                driver = webdriver.Chrome(options=chrome_options)
            elif browser == "firefox":
                driver = webdriver.Firefox()
            else:
                raise ValueError(f"Unsupported browser: {browser}") # raise error if browser is not supported
            
            driver.get("https://letcode.in/test") # navigate to home page
            driver.maximize_window()
            return driver
        except Exception as e:
            print(f"Exception occurred while initializing driver for {browser}: {e}")
            if driver:
                driver.quit()
            raise

'''more:
Screenshot capabilities:For capturing screenshots automatically when a test fails.
'''