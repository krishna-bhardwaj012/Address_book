from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to your WebDriver (update with actual path)
driver = webdriver.Chrome()

# Open the HTML file (update the path if needed)
driver.get(r"C:\xampp\htdocs\addressbook\addressbook_4column.html")  # Update this path

# Locate input fields and buttons
name_input = driver.find_element(By.ID, "name")
email_input = driver.find_element(By.ID, "email")
phone_input = driver.find_element(By.ID, "number")
address_input = driver.find_element(By.ID, "address")
add_button = driver.find_element(By.XPATH, "//button[text()='Add']")
reset_button = driver.find_element(By.XPATH, "//button[text()='Reset']")
contact_list = driver.find_element(By.ID, "contactList")

# Test Data (3 Entries)
test_data = [
    ("Arindam", "1234567890", "Kolkata"),
    ("Arindam_test", "9876543210", "Barddhaman"),
    ("Alex", "555667788", "Delhi")
]

# Run tests 3 times with different data
for test_name, test_email, test_phone, test_address in test_data:
    print(f"Testing with: {test_name}, {test_email}, {test_phone}, {test_address}")

    # Add a contact
    name_input.send_keys(test_name)
    email_input.send_keys(test_email)
    phone_input.send_keys(test_phone)
    address_input.send_keys(test_address)
    add_button.click()
    time.sleep(1)  # Wait for update

    # Verify the contact is added
    contacts = contact_list.find_elements(By.TAG_NAME, "li")
    assert any(test_name in contact.text for contact in contacts), "Contact not added!"

    # Click on the last added contact to view details
    contacts[-1].click()
    time.sleep(1)

    # Verify details
    assert name_input.get_attribute("value") == test_name, "Name does not match!"
    assert email_input.get_attribute("value") == test_email, "Email does not match!"
    assert phone_input.get_attribute("value") == test_phone, "Phone does not match!"
    assert address_input.get_attribute("value") == test_address, "Address does not match!"

    # Reset fields
    reset_button.click()
    time.sleep(1)

    # Verify fields are cleared
    assert name_input.get_attribute("value") == "", "Name field not cleared!"
    assert email_input.get_attribute("value") == "", "Email field not cleared!"
    assert phone_input.get_attribute("value") == "", "Phone field not cleared!"
    assert address_input.get_attribute("value") == "", "Address field not cleared!"

    print(f"Test {test_name} passed!\n")

print("All tests passed successfully!")

# Close the browser
#driver.quit()
