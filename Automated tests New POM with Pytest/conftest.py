import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

@pytest.fixture
def driver(browser):
    if browser == "chrome":
        options = Options()
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(options=options)
    elif browser == "edge":
        options = EdgeOptions()
        options.use_chromium = True
        driver = webdriver.Edge(options=options)
        driver.maximize_window()
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.get("https://puppies-closet.com/evidencija/login.php")

    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Specify the browser (chrome, edge, or firefox)")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")