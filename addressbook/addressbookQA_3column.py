from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start the Chrome browser
driver = webdriver.Chrome()

# Open the local HTML file
driver.get(r"file:///E:/addressbook/addressbook/addressbook_3column.html")  # Make sure this path is correct

# Wait until the form is loaded
wait = WebDriverWait(driver, 10)

# Test Data (3 Entries)
test_data = [
    ("Rishi", "9471662600", "Banglore"),
    ("Suraj", "9471662601", "Banglore"),
    ("Ravi", "9471662602", "Banglore"),
]

for test_name, test_phone, test_address in test_data:
    print(f"Testing with: {test_name}, {test_phone}, {test_address}")

    # Wait for form inputs
    name_input = wait.until(EC.presence_of_element_located((By.ID, "name")))
    phone_input = wait.until(EC.presence_of_element_located((By.ID, "number")))
    address_input = wait.until(EC.presence_of_element_located((By.ID, "address")))
    add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add']")))
    reset_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Reset']")))
    contact_list = wait.until(EC.presence_of_element_located((By.ID, "contactList")))

    # Fill the form and add contact
    name_input.send_keys(test_name)
    phone_input.send_keys(test_phone)
    address_input.send_keys(test_address)
    add_button.click()
    time.sleep(1)

    # Verify contact is added
    contacts = contact_list.find_elements(By.TAG_NAME, "li")
    assert any(test_name in contact.text for contact in contacts), "Contact not added!"

    # Click the latest contact
    contacts[-1].click()
    time.sleep(1)

    # Re-locate the fields (they may reload)
    name_input = driver.find_element(By.ID, "name")
    phone_input = driver.find_element(By.ID, "number")
    address_input = driver.find_element(By.ID, "address")

    # Verify values
    assert name_input.get_attribute("value") == test_name, "Name does not match!"
    assert phone_input.get_attribute("value") == test_phone, "Phone does not match!"
    assert address_input.get_attribute("value") == test_address, "Address does not match!"

    # Reset and verify
    reset_button.click()
    time.sleep(1)
    assert name_input.get_attribute("value") == "", "Name not cleared!"
    assert phone_input.get_attribute("value") == "", "Phone not cleared!"
    assert address_input.get_attribute("value") == "", "Address not cleared!"

    print(f"Test {test_name} passed!\n")

print("✅ All tests passed successfully!")
time.sleep(300)

# Delete all contacts using JavaScript
print("Deleting all contacts...")
driver.execute_script("contacts = []; updateList();")

# driver.quit()
