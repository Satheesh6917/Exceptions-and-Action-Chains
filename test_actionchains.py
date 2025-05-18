from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import time

# Positive Case
def test_chains():
    driver = webdriver.Chrome()
    driver.get("https://jqueryui.com/droppable/")
    driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, ".demo-frame"))

    source = driver.find_element(By.ID, "draggable")
    target = driver.find_element(By.ID, "droppable")
    action = ActionChains(driver)

    action.drag_and_drop(source, target).perform()
    time.sleep(5)
    driver.quit()

# Negative Case
def test_chains_negative_case():
    try:
        driver = webdriver.Chrome()
        driver.get("https://jqueryui.com/droppable/")
        driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, ".demo-frame"))

        try:
            # Intentionally using wrong ID to trigger exception
            source = driver.find_element(By.ID, "invalid-draggable")
            target = driver.find_element(By.ID, "droppable")
            action = ActionChains(driver)
            action.drag_and_drop_by_offset(source, 150, 30).perform()
            print("Drag-and-drop executed successfully.")

        except NoSuchElementException as e:
            print(f"Element not found: {e}")

        except WebDriverException as e:
            print(f"WebDriver exception occurred: {e}")

        time.sleep(3)

    except Exception as e:
        print(f"Unexpected error occurred: {e}")

    finally:
         driver.quit()
