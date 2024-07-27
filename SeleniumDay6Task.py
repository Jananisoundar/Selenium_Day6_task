import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def initialize_driver():
    """Initialize the Chrome driver."""
    driver = webdriver.Chrome()
    return driver


def open_instagram_page(driver, url):
    """Open the Instagram page and wait for it to load."""
    driver.get(url)
    time.sleep(5)  # Wait for the page to load


def get_followers_count(driver):
    """Get the count of followers from the Instagram page."""
    return driver.find_element(By.XPATH,"//button[text() = ' followers']").text


def get_following_count(driver):
    """Get the count of following from the Instagram page."""
    return driver.find_element(By.XPATH,"//button[text() = ' following']").text


def close_driver(driver):
    """Close the WebDriver."""
    driver.quit()


def main():
    url = "https://www.instagram.com/guviofficial/"
    driver = initialize_driver()

    try:
        open_instagram_page(driver, url)
        followers = get_followers_count(driver)
        print("Total number of followers:", followers)

        time.sleep(5)  # Wait before getting the following count

        following = get_following_count(driver)
        print("Total number of following:", following)
    finally:
        close_driver(driver)


if __name__ == "__main__":
    main()
