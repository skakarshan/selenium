from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Set the path to the Chromedriver
DRIVER_PATH = '/Users/akarshan/Downloads/chromedriver-mac-arm64/chromedriver'

# Initialize the Chrome driver
service = Service(executable_path=DRIVER_PATH)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the URL
driver.get('https://google.com')

page_source = driver.page_source
 
# Print the page source
print(page_source)

# It's a good practice to close the browser when done
driver.quit()