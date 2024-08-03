from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup WebDriver (Chrome example)
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to FitPeo Homepage
    driver.get('https://fitpeo.com')

    # Step 2: Navigate to Revenue Calculator Page
    revenue_calculator_link = driver.find_element(By.LINK_TEXT, 'Revenue Calculator')
    revenue_calculator_link.click()

    # Step 3: Scroll Down to the Slider section
    slider = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'revenue-slider'))  # Replace with actual ID
    )

    # Step 4: Adjust the Slider to 820
    driver.execute_script("arguments[0].setAttribute('value', 820)", slider)

    # Step 5: Update the Text Field to 560
    text_field = driver.find_element(By.ID, 'text-field')  # Replace with actual ID
    text_field.clear()
    text_field.send_keys('560')

    # Validate that the slider has moved to 560
    assert slider.get_attribute('value') == '560', "Slider value did not update correctly"

    # Step 6: Select CPT Codes
    cpt_codes = ['CPT-99091', 'CPT-99453', 'CPT-99454', 'CPT-99474']
    for code in cpt_codes:
        checkbox = driver.find_element(By.XPATH, f"//input[@value='{code}']")
        if not checkbox.is_selected():
            checkbox.click()

    # Step 7: Validate Total Recurring Reimbursement
    reimbursement = driver.find_element(By.ID, 'total-reimbursement')  # Replace with actual ID
    assert reimbursement.text == '$110700', "Total Recurring Reimbursement is incorrect"

finally:
    # Close the browser
    driver.quit()
