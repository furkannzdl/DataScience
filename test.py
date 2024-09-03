from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


# Set up the WebDriver
service = Service('/Users/furkanozdal/Downloads/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get("https://kayit.deu.edu.tr/")

# Log in to the system
username = driver.find_element(By.NAME, "user")
password = driver.find_element(By.NAME, "pass")

username.send_keys("mustafafurkan.ozdal")
password.send_keys("Okulguide001")

login_button = driver.find_element(By.NAME, "tamam")
login_button.click()


"""
# Navigate to the course registration page
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "course_registration_link"))
).click()

# Select courses
course1 = driver.find_element(By.ID, "course1_checkbox")
course2 = driver.find_element(By.ID, "course2_checkbox")

course1.click()
course2.click()

# Submit registration
submit_button = driver.find_element(By.ID, "submit_registration_button")
submit_button.click()

# Handle success or failure
try:
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "success_message"))
    )
    print("Registration Successful:", success_message.text)
except:
    print("Registration Failed")

# Close the WebDriver"""
driver.quit()
