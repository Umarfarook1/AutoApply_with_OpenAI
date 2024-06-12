# Job Application Form Automation

This project automates the process of filling out a job application form using Selenium and OpenAI's GPT-3.5-turbo API to generate realistic dummy data.

# AI Agent for Form Automation

## Introduction
This project automates the process of filling out a job application form using Selenium for web automation and OpenAI's GPT-3 for generating realistic dummy data.

## Project Description

This project demonstrates the automation of a job application form submission using Python, Selenium, and OpenAI's GPT-3.5-turbo model. The script generates realistic dummy data for the application form using OpenAI's API and automates the process of filling out the form and submitting it using Selenium WebDriver.

## Features

- **Data Generation**: Automatically generates realistic dummy data for form fields.
- **Web Automation**: Uses Selenium WebDriver to fill out and submit the job application form.
- **Error Handling**: Implements error handling for common issues such as element not found, timeouts, and click interception.
- **Logging**: Provides detailed logging to track the process flow and debug issues.
- **File Upload**: Automates the file upload process for the resume section of the application form.
- 
## Approach
1. **Data Generation**:
   - Used OpenAI's GPT-3 to generate realistic dummy data for the form fields.
2. **Web Automation**:
   - Utilized Selenium WebDriver to interact with the form elements and fill them with the generated data.
   - Handled file upload using `pyautogui`.

## Other Approaches
- **Puppeteer (Node.js)**:
  - A headless browser automation tool that could have been used.
- **BeautifulSoup (Python)**:
  - Suitable for web scraping but less ideal for interactive form submission.

## Why This Approach
- **Selenium**:
  - Chosen for its robustness and wide adoption for web automation.
  - Supports a variety of browsers and has extensive documentation.
- **OpenAI GPT-3**:
  - Provides high-quality, contextually appropriate dummy data generation.
- **Challenges**:
  - Handling dynamic web elements and ensuring reliable form submission.
  - Managed by incorporating explicit waits and error handling in the script.

## Usage
1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt


## Features

- Generates realistic dummy data for job applications using OpenAI's API.
- Automates the form-filling process using Selenium.
- Uploads a resume and submits the form automatically.

## Requirements

To run this project, you need to have the following software installed:

- Python 3.x
- OpenAI API key
- Google Chrome browser
- ChromeDriver


## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/Umarfarook1/job-application-automation-using-openAi-api.git
cd Umarfarook1/job-application-automation-using-openAi-api

2. **Install the required packages:**

```bash
pip install -r requirements.txt
Set your OpenAI API key:
Replace 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' with your actual OpenAI API key in the script.
