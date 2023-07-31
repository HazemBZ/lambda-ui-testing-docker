import os
import json
from selenium import webdriver


from pyvirtualdisplay import Display
from pyvirtualdisplay.smartdisplay import SmartDisplay
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service









def lambda_handler(event, context):
    global error
    'Lambda Handler'
    print('#===> Inside Handler')
    print(event)


    enable_display = True
    error = ''

    try:

        ## ===== Chrome part =====
        chrome_options = ChromeOptions()

        service = Service(executable_path='/opt/driver/chromedriver')

        if not enable_display:
            chrome_options.add_argument('--headless')
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.binary_location = '/opt/chrome/chrome-linux/chrome'
        chrome_options.add_argument("--no-zygote")
        chrome_options.add_argument("--single-process")
        chrome_options.add_argument("--remote-debugging-port=9222")

        print('## {DISPLAY}: ', os.environ['DISPLAY'])
        print('#==== Starting emu display')
        print('## {DISPLAY}: ', os.environ['DISPLAY'])

        print('#==== Starting chrome Driver')
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get("https://example.com/")
        print(driver.find_element(by=By.XPATH, value="//html").text)
        print('#==== Stopping emu display')


    except Exception as e:
        error = e
        print(e)


    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": "finished executing",
            "error": str(error)
        })
    }
