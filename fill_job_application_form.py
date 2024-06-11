import time
import logging
import openai
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# OpenAI API Key
openai.api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_dummy_data():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "user", "content": """Generate realistic dummy data for a job application form including:
                1. First name
                2. Middle name
                3. Last name
                4. Street address
                5. Street address line 2
                6. City
                7. State
                8. Postal code
                9. Email
                10. Phone number
                11. LinkedIn profile
                12. A short comment about AI Agents/LLMs
                13. A short comment about Web Automation
                14. A short comment about reversing a LinkedList
                15. Cover letter
                Return the data in JSON format.
                """}
            ]
        )
        raw_data = response.choices[0].message.content.strip()
        logging.info("Raw API Response: %s", raw_data)  # Print raw API response for debugging

        try:
            # Fix: Correctly format the JSON string if needed
            if raw_data.startswith('```') and raw_data.endswith('```'):
                raw_data = raw_data.strip('```')
            data = json.loads(raw_data)
            logging.info("Parsed Data: %s", data)  # Print parsed data for debugging
            return {
                'first_name': data.get('first_name', ''),
                'middle_name': data.get('middle_name', ''),
                'last_name': data.get('last_name', ''),
                'street_address': data.get('street_address', ''),
                'street_address_line_2': data.get('street_address_line_2', ''),
                'city': data.get('city', ''),
                'state': data.get('state', ''),
                'postal_code': data.get('postal_code', ''),
                'email': data.get('email', ''),
                'phone_number': data.get('phone_number', ''),
                'linkedin_profile': data.get('linkedin_profile', ''),
                'ai_agents_comment': data.get('ai_agents_comment', ''),
                'web_automation_comment': data.get('web_automation_comment', ''),
                'linked_list_comment': data.get('linked_list_comment', ''),
                'cover_letter': data.get('cover_letter', '')
            }
        except json.JSONDecodeError as e:
            logging.error("Failed to parse JSON response: %s", e)
            return None
    except Exception as e:
        logging.error("Failed to generate dummy data: %s", e)
        return None

def fill_form(driver, resume_path, data):
    try:
        logging.info("Opening the form URL")
        driver.get("https://form.jotform.com/241617189501153")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "form")))

        logging.info("Filling out the form with dummy data")

        driver.find_element(By.NAME, "q11_fullName[first]").send_keys(data['first_name'])
        driver.find_element(By.NAME, "q11_fullName[middle]").send_keys(data['middle_name'])
        driver.find_element(By.NAME, "q11_fullName[last]").send_keys(data['last_name'])
        driver.find_element(By.NAME, "q16_currentAddress[addr_line1]").send_keys(data['street_address'])
        driver.find_element(By.NAME, "q16_currentAddress[addr_line2]").send_keys(data['street_address_line_2'])
        driver.find_element(By.NAME, "q16_currentAddress[city]").send_keys(data['city'])
        driver.find_element(By.NAME, "q16_currentAddress[state]").send_keys(data['state'])
        driver.find_element(By.NAME, "q16_currentAddress[postal]").send_keys(data['postal_code'])
        driver.find_element(By.NAME, "q12_emailAddress").send_keys(data['email'])
        driver.find_element(By.NAME, "q13_phoneNumber13[full]").send_keys(data['phone_number'])
        driver.find_element(By.NAME, "q19_linkedin").send_keys(data['linkedin_profile'])
        driver.find_element(By.NAME, "q24_writeSomething").send_keys(data['ai_agents_comment'])
        driver.find_element(By.NAME, "q25_writeSomething25").send_keys(data['web_automation_comment'])
        driver.find_element(By.NAME, "q23_reverseA").send_keys(data['linked_list_comment'])
        driver.find_element(By.NAME, "q22_coverLetter").send_keys(data['cover_letter'])

        logging.info("Uploading the resume")
        upload_button = driver.find_element(By.XPATH, "//input[@type='file']")
        upload_button.send_keys(resume_path)

        logging.info("Submitting the form")
        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "input_9")))
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)  # Scroll into view if needed
        time.sleep(1)  # Wait for scrolling to take effect

        try:
            submit_button.click()
        except ElementClickInterceptedException:
            logging.warning("Element click intercepted, attempting JavaScript click")
            driver.execute_script("arguments[0].click();", submit_button)

        logging.info("Form submitted successfully")
        time.sleep(5)  # Wait to ensure form submission

    except NoSuchElementException as e:
        logging.error(f"Element not found: {e}")
    except TimeoutException as e:
        logging.error(f"Page load timeout: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Initialize WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        resume_path = r"C:\Users\umarf\intership-AI_Agent\sample-resume\UMAR FAROOK GURRAMKONDA.pdf"
        # Generate dummy data using OpenAI API
        dummy_data_response = generate_dummy_data()
        if dummy_data_response:
             # Fill the form with generated dummy data
            fill_form(driver, resume_path, dummy_data_response)
        else:
            logging.error("Failed to generate dummy data")
    finally:
        logging.info("Closing the WebDriver")
        driver.quit()
