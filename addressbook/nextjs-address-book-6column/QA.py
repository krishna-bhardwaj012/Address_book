from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Start the browser
driver = webdriver.Chrome()

# Open the Address Book app
driver.get("http://localhost:3000")  # Update the URL if needed
time.sleep(2)

# Test Data
test_contact = {
    "name": "demo",
    "phone": "demo",
    "email": "mr.arindamkhan@gmail.com",
    "address": "Salt lake kolkata",
    "city": "Kolkata",
    "zip": "10001"
}

# Locate input fields and enter data
driver.find_element(By.NAME, "name").send_keys(test_contact["name"])
driver.find_element(By.NAME, "phone").send_keys(test_contact["phone"])
driver.find_element(By.NAME, "email").send_keys(test_contact["email"])
driver.find_element(By.NAME, "address").send_keys(test_contact["address"])
driver.find_element(By.NAME, "city").send_keys(test_contact["city"])
driver.find_element(By.NAME, "zip").send_keys(test_contact["zip"])

# Click "Add" button
driver.find_element(By.XPATH, "//button[contains(text(),'Add')]").click()
time.sleep(2)

# Verify if the contact was added
contacts = driver.find_elements(By.TAG_NAME, "li")
assert any(test_contact["name"] in contact.text for contact in contacts), "Contact not added!"

# Edit the first contact
contacts[0].find_element(By.XPATH, ".//button[contains(text(),'Edit')]").click()
time.sleep(1)

# Modify the name
name_field = driver.find_element(By.NAME, "name")
name_field.clear()
name_field.send_keys("John Updated")
driver.find_element(By.XPATH, "//button[contains(text(),'Add')]").click()
time.sleep(2)

# Verify the contact was updated
contacts = driver.find_elements(By.TAG_NAME, "li")
assert any("John Updated" in contact.text for contact in contacts), "Contact update failed!"

# Delete the first contact
contacts[0].find_element(By.XPATH, ".//button[contains(text(),'Delete')]").click()
time.sleep(2)

# Verify if the contact was deleted
contacts = driver.find_elements(By.TAG_NAME, "li")
assert not any("John Updated" in contact.text for contact in contacts), "Contact deletion failed!"

# Close the browser
driver.quit()
