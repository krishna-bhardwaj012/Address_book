from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("http://localhost:3000")
time.sleep(3)  # Wait for the page to load

# Function to add a new contact
def add_contact(name, phone, address):
    driver.find_element(By.NAME, "name").send_keys(name)
    driver.find_element(By.NAME, "phone").send_keys(phone)
    driver.find_element(By.NAME, "address").send_keys(address)
    driver.find_element(By.XPATH, "//button[text()='Add']").click()
    time.sleep(2)

# Function to edit first contact
def edit_first_contact():
    driver.find_element(By.XPATH, "//button[text()='Edit']").click()
    time.sleep(2)
    driver.find_element(By.NAME, "name").send_keys(" Updated")
    driver.find_element(By.XPATH, "//button[text()='Add']").click()
    time.sleep(2)

# Function to delete first contact
def delete_first_contact():
    driver.find_element(By.XPATH, "//button[text()='Delete']").click()
    time.sleep(2)

# Test sequence
add_contact("Rishi", "9471662600", "Banglore")
add_contact("Suraj", "9471662601", "Banglore")
add_contact("Ravi", "9471662602", "Banglore")
edit_first_contact()
delete_first_contact()
# Close the WebDriver
driver.quit()
# Note: Ensure that the web server is running and the page is accessible at http://localhost:3000